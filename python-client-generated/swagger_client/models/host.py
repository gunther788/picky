# coding: utf-8

"""
    PICKY: Python ICinga2 to KeYbase

    A Bridge between Icinga2's Notifications and Keybase  # noqa: E501

    OpenAPI spec version: 1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Host(object):
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
        'channel': 'str',
        'msg_id': 'int',
        'state': 'str',
        'output': 'str',
        'timestamp': 'str'
    }

    attribute_map = {
        'name': 'name',
        'channel': 'channel',
        'msg_id': 'msg_id',
        'state': 'state',
        'output': 'output',
        'timestamp': 'timestamp'
    }

    def __init__(self, name=None, channel=None, msg_id=0, state='UP', output='', timestamp='now'):  # noqa: E501
        """Host - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._channel = None
        self._msg_id = None
        self._state = None
        self._output = None
        self._timestamp = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if channel is not None:
            self.channel = channel
        if msg_id is not None:
            self.msg_id = msg_id
        if state is not None:
            self.state = state
        if output is not None:
            self.output = output
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def name(self):
        """Gets the name of this Host.  # noqa: E501

        Name of host to create  # noqa: E501

        :return: The name of this Host.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Host.

        Name of host to create  # noqa: E501

        :param name: The name of this Host.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def channel(self):
        """Gets the channel of this Host.  # noqa: E501

        Name of the channel to notify  # noqa: E501

        :return: The channel of this Host.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this Host.

        Name of the channel to notify  # noqa: E501

        :param channel: The channel of this Host.  # noqa: E501
        :type: str
        """

        self._channel = channel

    @property
    def msg_id(self):
        """Gets the msg_id of this Host.  # noqa: E501

        Message ID in the channel  # noqa: E501

        :return: The msg_id of this Host.  # noqa: E501
        :rtype: int
        """
        return self._msg_id

    @msg_id.setter
    def msg_id(self, msg_id):
        """Sets the msg_id of this Host.

        Message ID in the channel  # noqa: E501

        :param msg_id: The msg_id of this Host.  # noqa: E501
        :type: int
        """

        self._msg_id = msg_id

    @property
    def state(self):
        """Gets the state of this Host.  # noqa: E501


        :return: The state of this Host.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Host.


        :param state: The state of this Host.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def output(self):
        """Gets the output of this Host.  # noqa: E501

        Output of host check command  # noqa: E501

        :return: The output of this Host.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this Host.

        Output of host check command  # noqa: E501

        :param output: The output of this Host.  # noqa: E501
        :type: str
        """

        self._output = output

    @property
    def timestamp(self):
        """Gets the timestamp of this Host.  # noqa: E501

        Last update  # noqa: E501

        :return: The timestamp of this Host.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Host.

        Last update  # noqa: E501

        :param timestamp: The timestamp of this Host.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

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
        if issubclass(Host, dict):
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
        if not isinstance(other, Host):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
