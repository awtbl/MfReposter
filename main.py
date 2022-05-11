import asyncio
import json
import constants

from pyrogram import Client
from configurator import PyrogramConfig, load_config
from models import Channel


def load_channel() -> Channel:
    try:
        file = open("old_channel_data.dat")
    except FileNotFoundError:
        pass


async def client_builder(config: PyrogramConfig) -> Client:
    """
    Returns an initialized client
    :param PyrogramConfig config: A configuration-object
    :rtype: Client
    :return: Initialized client
    """

    client = Client(
        name="pyrogram",
        api_hash=config.api_hash,
        api_id=config.api_id,
    )

    await client.start()

    return client


async def main():
    """Heart of project"""
    config = load_config(constants.CONFIG_FILENAME)
    print(config.channels.original_channel_id)
    client = await client_builder(config.pyrogram)
    ch = await client.get_chat(chat_id=-1001469529464)

    print(ch.id)
    print(ch.description)
    print(ch.username)
    print(ch.title)


if __name__ == "__main__":
    asyncio.run(main())
