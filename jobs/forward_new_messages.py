from pyrogram import Client
from pyrogram.errors import FloodWait
from configurator import ChannelsConfig
from models import Channel
from asyncio import sleep

import logging
import loader


async def forward_messages(client: Client, channels_config: ChannelsConfig):
    """
    Will forward NEW messages.
    :param client: A pyrogram client
    :param channels_config: A channels-configuration
    :return: None
    """

    logging.log(logging.INFO, "Retrieving channel's metadata")
    original_channel = await client.get_chat(channels_config.original_channel_id)

    channel = (await Channel.get_or_create(
        identifier=original_channel.id,
        defaults={
            "last_post_id": 0,
        }
    ))[0]

    duplicate_channel = await client.get_chat(chat_id=channels_config.duplicate_channel_id)

    logging.log(logging.INFO, "Getting updates...")
    news = await loader.load_new_messages(client, channel.identifier, channel.last_post_id)
    logging.info(f"{len(news)} new messages found!")

    if not news:
        return

    for message in news:
        if message.new_chat_photo:
            logging.info("New chat photo detected, updating...")
            await duplicate_channel.set_photo(photo=message.new_chat_photo.file_id)
        elif message.new_chat_title:
            logging.info("New chat title detected, updating...")
            await duplicate_channel.set_title(message.new_chat_title)
        else:
            logging.info(f"Forwarding message {message.id}")

            sleep_time = 400  # 400 seconds

            while True:
                try:
                    await message.forward(channels_config.duplicate_channel_id)
                except FloodWait:
                    logging.info(f"Floodwait, waiting {sleep_time} seconds...")
                    logging.info(f"Saving last post's ID ({message.id})")
                    channel.last_post_id = message.id
                    await channel.save()
                    await sleep(sleep_time)
                    sleep_time += 10
                    continue
                except Exception as e:
                    logging.info(f"Exception'{e}' occur during forwarding message {message.id}")
                    break

                break

    channel.last_post_id = news[-1].id
    logging.info(f"Forwarding finished, totally {len(news)} messages forwarded")
    await channel.save()
