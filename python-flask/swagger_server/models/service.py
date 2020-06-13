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

    def __init__(self, name: str=None, host: str=None, short: str=None, state: str='OK'):  # noqa: E501
        """Service - a model defined in Swagger

        :param name: The name of this Service.  # noqa: E501
        :type name: str
        :param host: The host of this Service.  # noqa: E501
        :type host: str
        :param short: The short of this Service.  # noqa: E501
        :type short: str
        :param state: The state of this Service.  # noqa: E501
        :type state: str
        """
        self.swagger_types = {
            'name': str,
            'host': str,
            'short': str,
            'state': str
        }

        self.attribute_map = {
            'name': 'name',
            'host': 'host',
            'short': 'short',
            'state': 'state'
        }

        self._name = name
        self._host = host
        self._short = short
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

        Name of service to create  # noqa: E501

        :return: The name of this Service.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Service.

        Name of service to create  # noqa: E501

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
    def short(self) -> str:
        """Gets the short of this Service.

        Short name of the service  # noqa: E501

        :return: The short of this Service.
        :rtype: str
        """
        return self._short

    @short.setter
    def short(self, short: str):
        """Sets the short of this Service.

        Short name of the service  # noqa: E501

        :param short: The short of this Service.
        :type short: str
        """

        self._short = short

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
