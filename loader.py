from typing import Union
from pyrogram import Client
from models import Channel


async def load_channel(pyrogram_client: Client, channel_id: Union[str, int]) -> Channel:
    """
    Fetches needed meta-information about channel
    :param pyrogram_client: A pyrogram client
    :param channel_id: A channel's ID
    :return: Channel
    """

    ch = await pyrogram_client.get_chat(chat_id=channel_id)

    return Channel(
        ch.photo.big_file_id if ch.photo else None,
        ch.title,
        ch.description
    )
