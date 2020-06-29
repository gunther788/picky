# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Service(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, state: str='OK', output: str='', timestamp: str=None, updates: int=0, sla: str='bronze', note_type: str='Problem', picky: str=None, url: str=None):  # noqa: E501
        """Service - a model defined in Swagger

        :param name: The name of this Service.  # noqa: E501
        :type name: str
        :param state: The state of this Service.  # noqa: E501
        :type state: str
        :param output: The output of this Service.  # noqa: E501
        :type output: str
        :param timestamp: The timestamp of this Service.  # noqa: E501
        :type timestamp: str
        :param updates: The updates of this Service.  # noqa: E501
        :type updates: int
        :param sla: The sla of this Service.  # noqa: E501
        :type sla: str
        :param note_type: The note_type of this Service.  # noqa: E501
        :type note_type: str
        :param picky: The picky of this Service.  # noqa: E501
        :type picky: str
        :param url: The url of this Service.  # noqa: E501
        :type url: str
        """
        self.swagger_types = {
            'name': str,
            'state': str,
            'output': str,
            'timestamp': str,
            'updates': int,
            'sla': str,
            'note_type': str,
            'picky': str,
            'url': str
        }

        self.attribute_map = {
            'name': 'name',
            'state': 'state',
            'output': 'output',
            'timestamp': 'timestamp',
            'updates': 'updates',
            'sla': 'sla',
            'note_type': 'note_type',
            'picky': 'picky',
            'url': 'url'
        }
        self._name = name
        self._state = state
        self._output = output
        self._timestamp = timestamp
        self._updates = updates
        self._sla = sla
        self._note_type = note_type
        self._picky = picky
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'Service':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The service of this Service.  # noqa: E501
        :rtype: Service
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Service.

        Short name of the service  # noqa: E501

        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Service.

        Short name of the service  # noqa: E501

        :param name: The name of this Service.
        :type name: str
        """

        self._name = name

    @property
    def state(self) -> str:
        """Gets the state of this Service.


        :return: The state of this Service.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this Service.


        :param state: The state of this Service.
        :type state: str
        """
        allowed_values = ["OK", "WARNING", "CRITICAL", "UNKNOWN"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def output(self) -> str:
        """Gets the output of this Service.

        Output of service check command  # noqa: E501

        :return: The output of this Service.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output: str):
        """Sets the output of this Service.

        Output of service check command  # noqa: E501

        :param output: The output of this Service.
        :type output: str
        """

        self._output = output

    @property
    def timestamp(self) -> str:
        """Gets the timestamp of this Service.

        Last update  # noqa: E501

        :return: The timestamp of this Service.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        """Sets the timestamp of this Service.

        Last update  # noqa: E501

        :param timestamp: The timestamp of this Service.
        :type timestamp: str
        """

        self._timestamp = timestamp

    @property
    def updates(self) -> int:
        """Gets the updates of this Service.

        Update counter  # noqa: E501

        :return: The updates of this Service.
        :rtype: int
        """
        return self._updates

    @updates.setter
    def updates(self, updates: int):
        """Sets the updates of this Service.

        Update counter  # noqa: E501

        :param updates: The updates of this Service.
        :type updates: int
        """

        self._updates = updates

    @property
    def sla(self) -> str:
        """Gets the sla of this Service.


        :return: The sla of this Service.
        :rtype: str
        """
        return self._sla

    @sla.setter
    def sla(self, sla: str):
        """Sets the sla of this Service.


        :param sla: The sla of this Service.
        :type sla: str
        """
        allowed_values = ["gold", "silver", "bronze"]  # noqa: E501
        if sla not in allowed_values:
            raise ValueError(
                "Invalid value for `sla` ({0}), must be one of {1}"
                .format(sla, allowed_values)
            )

        self._sla = sla

    @property
    def note_type(self) -> str:
        """Gets the note_type of this Service.


        :return: The note_type of this Service.
        :rtype: str
        """
        return self._note_type

    @note_type.setter
    def note_type(self, note_type: str):
        """Sets the note_type of this Service.


        :param note_type: The note_type of this Service.
        :type note_type: str
        """
        allowed_values = ["Problem", "Acknowledgement", "Recovery"]  # noqa: E501
        if note_type not in allowed_values:
            raise ValueError(
                "Invalid value for `note_type` ({0}), must be one of {1}"
                .format(note_type, allowed_values)
            )

        self._note_type = note_type

    @property
    def picky(self) -> str:
        """Gets the picky of this Service.

        Stub neatly formatted for Keybase  # noqa: E501

        :return: The picky of this Service.
        :rtype: str
        """
        return self._picky

    @picky.setter
    def picky(self, picky: str):
        """Sets the picky of this Service.

        Stub neatly formatted for Keybase  # noqa: E501

        :param picky: The picky of this Service.
        :type picky: str
        """

        self._picky = picky

    @property
    def url(self) -> str:
        """Gets the url of this Service.

        Link to this object  # noqa: E501

        :return: The url of this Service.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this Service.

        Link to this object  # noqa: E501

        :param url: The url of this Service.
        :type url: str
        """

        self._url = url
