import asyncio

import constants

from pyrogram import Client
from configurator import PyrogramConfig, load_config


def client_builder(config: PyrogramConfig) -> Client:
    """W
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

    client.start()

    return client


async def task(client, config):
    ch = await client.get_chat(config.original_channel_id)

    print(ch.id)
    print(ch.bio)

def main():
    """Heart of project"""
    config = load_config(constants.CONFIG_FILENAME)

    client = client_builder(config.pyrogram)

    asyncio.run(task(client, config.channels))


if __name__ == "__main__":
    main()
