from pyrogram import Client
from configurator import ChannelsConfig

import logging


async def update_channel_info(client: Client, channels_config: ChannelsConfig):
    """
    Updates profile
    :param client: A pyrogram client
    :param channels_config: A ChannelsConfig object
    :return: None
    """
    logging.log(level=logging.INFO, msg="Retrieving original channel's description")

    original_chat = await client.get_chat(channels_config.original_channel_id)
    duplicate_chat = await client.get_chat(channels_config.duplicate_channel_id)

    if original_chat.description != duplicate_chat.description:
        logging.log(level=logging.INFO, msg="Updating channel's description")
        await duplicate_chat.set_description(original_chat.description)

    if original_chat.title != duplicate_chat.title:
        logging.info("Updating channel's title")
        await duplicate_chat.set_title(original_chat.title)
