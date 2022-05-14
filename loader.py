from typing import Union, List
from pyrogram import Client
from pyrogram.types import Message


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

    return result[::-1]
