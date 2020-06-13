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

    def __init__(self, name: str=None, host: str=None, service: str=None, timestamp: str=None, state: str='OK'):  # noqa: E501
        """Service - a model defined in Swagger

        :param name: The name of this Service.  # noqa: E501
        :type name: str
        :param host: The host of this Service.  # noqa: E501
        :type host: str
        :param service: The service of this Service.  # noqa: E501
        :type service: str
        :param timestamp: The timestamp of this Service.  # noqa: E501
        :type timestamp: str
        :param state: The state of this Service.  # noqa: E501
        :type state: str
        """
        self.swagger_types = {
            'name': str,
            'host': str,
            'service': str,
            'timestamp': str,
            'state': str
        }

        self.attribute_map = {
            'name': 'name',
            'host': 'host',
            'service': 'service',
            'timestamp': 'timestamp',
            'state': 'state'
        }

        self._name = name
        self._host = host
        self._service = service
        self._timestamp = timestamp
        self._state = state

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

        Name of service, host!service format  # noqa: E501

        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Service.

        Name of service, host!service format  # noqa: E501

        :param name: The name of this Service.
        :type name: str
        """

        self._name = name

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
    def service(self) -> str:
        """Gets the service of this Service.

        Short name of the service  # noqa: E501

        :return: The service of this Service.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service: str):
        """Sets the service of this Service.

        Short name of the service  # noqa: E501

        :param service: The service of this Service.
        :type service: str
        """

        self._service = service

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
