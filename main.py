import asyncio
import logging

from sqlmodel import SQLModel

import constants
import utils.asyncio
import jobs

from pyrogram import Client
from models import Channel
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker
from configurator import PyrogramConfig, DatabaseConfig, load_config
from typing import Callable, Awaitable


async def engine_factory(config: DatabaseConfig) -> AsyncEngine:
    """
    A factory for creating asynchronous SQLAlchemy's engines
    :param config: A database's configuration
    :return: Initialized engine
    """
    connection = create_async_engine(config.database_url)
    await connection.run_sync(SQLModel.metadata.create_all)
    return connection


def build_session_factory(engine: AsyncEngine) -> Callable[[], Awaitable[AsyncSession]]:
    """
    Returns an AsyncSession factory
    :param engine: Initialized SQLModel's engine
    :return: An AsyncSession factory
    """
    async def factory() -> AsyncSession:
        se = sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=True,
        )
        return await se()

    return factory


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
