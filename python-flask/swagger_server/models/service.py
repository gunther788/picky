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
    def __init__(self, host: str=None, name: str=None, state: str='OK', output: str='', timestamp: str=''):  # noqa: E501
        """Service - a model defined in Swagger

        :param host: The host of this Service.  # noqa: E501
        :type host: str
        :param name: The name of this Service.  # noqa: E501
        :type name: str
        :param state: The state of this Service.  # noqa: E501
        :type state: str
        :param output: The output of this Service.  # noqa: E501
        :type output: str
        :param timestamp: The timestamp of this Service.  # noqa: E501
        :type timestamp: str
        """
        self.swagger_types = {
            'host': str,
            'name': str,
            'state': str,
            'output': str,
            'timestamp': str
        }

        self.attribute_map = {
            'host': 'host',
            'name': 'name',
            'state': 'state',
            'output': 'output',
            'timestamp': 'timestamp'
        }
        self._host = host
        self._name = name
        self._state = state
        self._output = output
        self._timestamp = timestamp

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
    def host(self) -> str:
        """Gets the host of this Service.

        Host this service runs on  # noqa: E501

        :return: The host of this Service.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this Service.

        Host this service runs on  # noqa: E501

        :param host: The host of this Service.
        :type host: str
        """

        self._host = host

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
