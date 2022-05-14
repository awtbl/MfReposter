from typing import Union, List
from pyrogram import Client
from pyrogram.types import Message
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


async def load_new_messages(pyrogram_client: Client, channel_id: Union[str, int], lst_msg: int = 1) -> List[Message]:
    """
    Loads a list with messages from lst_msg to last message in chat!
    :param pyrogram_client: A pyrogram client
    :param channel_id: Channel's ID
    :param lst_msg: Last READIED message ID!
    :return: List with unread messages
    """
    result = []

    async for message in pyrogram_client.get_chat_history(chat_id=channel_id):
        if message.id <= lst_msg:
            break
        result.append(message)

    return result
