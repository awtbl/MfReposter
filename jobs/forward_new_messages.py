from pyrogram import Client
from pyrogram.errors import FloodWait
from configurator import ChannelsConfig
from models import Channel
from asyncio import sleep
from pyrogram.types import Chat

import logging
import loader


async def forward_messages(client: Client, original_channel_id: Chat, channels_config: ChannelsConfig):
    """
    Will forward NEW messages.
    :param client: A pyrogram client
    :param original_channel_id: An original channel's ID
    :param channels_config: A channels-configuration
    :return: None
    """

    logging.log(logging.INFO, "Retrieving channel's metadata")

    channel = Channel.get_or_none(
        Channel.channel_id == original_channel_id.id
    )

    if not channel:
        channel = Channel(
            channel_id=original_channel_id.id,
            last_post_id=0,
        )

    duplicate_channel = await client.get_chat(chat_id=channels_config.duplicate_channel_id)

    logging.log(logging.INFO, "Getting updates...")
    news = await loader.load_new_messages(client, channel.channel_id, channel.last_post_id)
    logging.info(f"{len(news)} new messages found!")

    if not news:
        return

    for message in news:
        if message.new_chat_photo:
            logging.info("New chat photo detected, updating...")
            await duplicate_channel.set_photo(message.new_chat_photo.file_unique_id)
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
                    channel.delete_instance()
                    channel.last_post_id = message.id
                    channel.save()
                    await sleep(sleep_time)
                    sleep_time += 10
                    continue
                except Exception as e:
                    logging.info(f"Exceptino '{e}' occured during forwarding message {message.id}")
                    break

                break

    channel.last_post_id = news[-1].id
    channel.delete_instance()
    channel.save()