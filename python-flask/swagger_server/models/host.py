# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util

from datetime import datetime

class Host(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, messages: Dict[str, int]=None, state: str='UP', output: str='', timestamp: str=None):  # noqa: E501
        """Host - a model defined in Swagger

        :param name: The name of this Host.  # noqa: E501
        :type name: str
        :param messages: The messages of this Host.  # noqa: E501
        :type messages: Dict[str, int]
        :param state: The state of this Host.  # noqa: E501
        :type state: str
        :param timestamp: The timestamp of this Host.  # noqa: E501
        :type timestamp: str
        """
        self.swagger_types = {
            'name': str,
            'messages': Dict[str, int],
            'state': str,
            'output': str,
            'timestamp': str
        }

        self.attribute_map = {
            'name': 'name',
            'messages': 'messages',
            'state': 'state',
            'output': 'output',
            'timestamp': 'timestamp'
        }
        self._name = name
        self._messages = messages
        self._state = state
        self._output = output
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'Host':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The host of this Host.  # noqa: E501
        :rtype: Host
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Host.

        Name of host to create  # noqa: E501

        :return: The name of this Host.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Host.

        Name of host to create  # noqa: E501

        :param name: The name of this Host.
        :type name: str
        """

        self._name = name

    @property
    def messages(self) -> Dict[str, int]:
        """Gets the messages of this Host.


        :return: The messages of this Host.
        :rtype: Dict[str, int]
        """
        return self._messages

    @messages.setter
    def messages(self, messages: Dict[str, int]):
        """Sets the messages of this Host.


        :param messages: The messages of this Host.
        :type messages: Dict[str, int]
        """

        self._messages = messages

    @property
    def state(self) -> str:
        """Gets the state of this Host.


        :return: The state of this Host.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this Host.


        :param state: The state of this Host.
        :type state: str
        """
        allowed_values = ["UP", "DOWN"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def output(self) -> str:
        """Gets the output of this Host.


        :return: The output of this Host.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output: str):
        """Sets the output of this Host.


        :param state: The output of this Host.
        :type output: str
        """
        self._output = output

    @property
    def timestamp(self) -> str:
        """Gets the timestamp of this Host.

        Last update  # noqa: E501

        :return: The timestamp of this Host.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        """Sets the timestamp of this Host.

        Last update  # noqa: E501

        :param timestamp: The timestamp of this Host.
        :type timestamp: str
        """

        self._timestamp = timestamp


    @property
    def all_good(self) -> bool:
        """Tests for all states UP / OK

        :rtype: bool
        """
        return self.state == 'UP'


    @property
    def picky(self) -> str:
        """Returns a formatted one-liner
        that can be chatted in keybase

        :rtype: str
        """
        msg = ""

        states = {
            'UP': '🟩',
            'DOWN': '🟥',
        }

        if self.state in states:
            msg = f"{states[self.state]} {msg}"

        msg = f"{msg} {self.timestamp} {self.name} #" + " #".join(self.messages.keys())
        if self.state == 'DOWN' and self.output != "":
            msg = msg + "\n\`" + (self.output)[:80] + "\`"

        return msg
