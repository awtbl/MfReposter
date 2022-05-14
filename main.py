import asyncio
import logging
import constants
import utils.asyncio
import jobs

from pyrogram import Client
from models import Channel, db
from configurator import PyrogramConfig, load_config


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


def init_db():
    """
    Initializes database
    :return:
    """
    db.create_tables(
        [
            Channel,
        ]
    )


async def main():
    """Heart of project"""

    init_db()
    config = load_config(constants.CONFIG_FILENAME)
    client = await client_builder(config.pyrogram)

    tasks = [
        utils.asyncio.schedule(jobs.handle_updates, config.scheduler.update_interval, client, config.channels)
    ]

    await asyncio.wait(tasks)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
