from __future__ import annotations
from typing import Union

import json


class Channel:
    """
    The class for containing channel's metadata like

        Channel's photo file ID
        Channel's title
        Channel's description
        Channel's last post ID
    """

    def __init__(self, photo_file_id: Union[str, None], title: str, description: Union[None, str]):
        """
        Constructor
        :param photo_file_id: A channel's profile-photo ID
        :param title: A channel's title
        :param description: A channel's description
        """

        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description

    @classmethod
    def from_json(cls, data: Union[str, dict]) -> Channel:
        """
        Returns a filled Channel
        :param data: A string or dict-object with data
        :return: Channel object
        """
        if isinstance(data, str):
            data = json.loads(data)

        return cls(**data)

    def to_dict(self) -> dict:
        return self.__dict__
