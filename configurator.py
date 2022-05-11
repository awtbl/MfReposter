from dataclasses import dataclass
from configparser import ConfigParser


@dataclass
class ChannelsConfig:
    """Configuration-class for Maf's channels"""
    original_channel_id: int
    duplicate_channel_id: int


@dataclass
class PyrogramConfig:
    """Configuration-class for Pyrogram"""
    api_id: int
    api_hash: str


@dataclass
class Configuration:
    """Main Config-class"""
    pyrogram: PyrogramConfig
    channels: ChannelsConfig


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
        config.getint("channels", "original"),
        config.getint("channels", "duplicate"),
    )

    return Configuration(
        pyrogram_config,
        channels_config,
    )
