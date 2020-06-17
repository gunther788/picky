# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class HostMessages(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, channel: str=None, id: int=None):  # noqa: E501
        """HostMessages - a model defined in Swagger

        :param channel: The channel of this HostMessages.  # noqa: E501
        :type channel: str
        :param id: The id of this HostMessages.  # noqa: E501
        :type id: int
        """
        self.swagger_types = {
            'channel': str,
            'id': int
        }

        self.attribute_map = {
            'channel': 'channel',
            'id': 'id'
        }
        self._channel = channel
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'HostMessages':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The host_messages of this HostMessages.  # noqa: E501
        :rtype: HostMessages
        """
        return util.deserialize_model(dikt, cls)

    @property
    def channel(self) -> str:
        """Gets the channel of this HostMessages.


        :return: The channel of this HostMessages.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel: str):
        """Sets the channel of this HostMessages.


        :param channel: The channel of this HostMessages.
        :type channel: str
        """

        self._channel = channel

    @property
    def id(self) -> int:
        """Gets the id of this HostMessages.


        :return: The id of this HostMessages.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this HostMessages.


        :param id: The id of this HostMessages.
        :type id: int
        """

        self._id = id
