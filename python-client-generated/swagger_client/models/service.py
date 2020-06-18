# coding: utf-8

"""
    PICKY: Python ICinga2 to KeYbase

    A Bridge between Icinga2's Notifications and Keybase  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Service(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'host': 'str',
        'service': 'str',
        'timestamp': 'str',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'host': 'host',
        'service': 'service',
        'timestamp': 'timestamp',
        'state': 'state'
    }

    def __init__(self, name=None, host=None, service=None, timestamp=None, state='OK'):  # noqa: E501
        """Service - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._host = None
        self._service = None
        self._timestamp = None
        self._state = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if host is not None:
            self.host = host
        if service is not None:
            self.service = service
        if timestamp is not None:
            self.timestamp = timestamp
        if state is not None:
            self.state = state

    @property
    def name(self):
        """Gets the name of this Service.  # noqa: E501

        Name of service, host!service format  # noqa: E501

        :return: The name of this Service.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Service.

        Name of service, host!service format  # noqa: E501

        :param name: The name of this Service.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def host(self):
        """Gets the host of this Service.  # noqa: E501

        Host this service runs on  # noqa: E501

        :return: The host of this Service.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this Service.

        Host this service runs on  # noqa: E501

        :param host: The host of this Service.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def service(self):
        """Gets the service of this Service.  # noqa: E501

        Short name of the service  # noqa: E501

        :return: The service of this Service.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Service.

        Short name of the service  # noqa: E501

        :param service: The service of this Service.  # noqa: E501
        :type: str
        """

        self._service = service

    @property
    def timestamp(self):
        """Gets the timestamp of this Service.  # noqa: E501

        Last update  # noqa: E501

        :return: The timestamp of this Service.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Service.

        Last update  # noqa: E501

        :param timestamp: The timestamp of this Service.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def state(self):
        """Gets the state of this Service.  # noqa: E501


        :return: The state of this Service.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Service.


        :param state: The state of this Service.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "WARNING", "CRITICAL", "UNKNOWN"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Service, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
