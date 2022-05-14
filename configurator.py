from dataclasses import dataclass
from configparser import ConfigParser
from typing import Union


@dataclass
class ChannelsConfig:
    """Configuration-class for Maf's channels"""
    original_channel_id: Union[str, int]
    duplicate_channel_id: Union[str, int]


@dataclass
class PyrogramConfig:
    """Configuration-class for Pyrogram"""
    api_id: int
    api_hash: str


@dataclass
class SchedulerConfig:
    """Configuration-class for Scheduler"""
    update_interval: int


@dataclass
class Configuration:
    """Main Config-class"""
    pyrogram: PyrogramConfig
    channels: ChannelsConfig
    scheduler: SchedulerConfig


def parse_telegram_id(config: ConfigParser, section: str, option: str) -> Union[str, int]:
    """
    Parses telegram-id
    :param ConfigParser config: A ConfigParser-object (prepared)
    :param Section section: A Section
    :param option: An option which contains telegram-id
    """

    try:
        # Firstly, try to get ID
        return config.getint(section, option)
    except ValueError:
        # If we can't parse ID as int, it is username
        return config.get(section, option)


def load_config(filename: str) -> Configuration:
    """
    Will load config
    :param str filename: A filename
    """

    config = ConfigParser()
    config.read(filename)

    pyrogram_config = PyrogramConfig(
        config.getint("pyrogram", "api_id"),
        config.get("pyrogram", "api_hash"),
    )

    channels_config = ChannelsConfig(
        parse_telegram_id(config, "channels", "original"),
        parse_telegram_id(config, "channels", "duplicate"),
    )

    scheduler_config = SchedulerConfig(
        config.getint("scheduler", "update_interval")
    )

    return Configuration(
        pyrogram_config,
        channels_config,
        scheduler_config
    )
