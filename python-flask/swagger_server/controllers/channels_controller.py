import connexion
import six

from swagger_server.models.channel import Channel  # noqa: E501
from swagger_server.models.channel1 import Channel1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def channels_create(channel):  # noqa: E501
    """Create a channel and add it to the channels list

    Create a new channel in the channels list # noqa: E501

    :param channel: Channel to create
    :type channel: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        channel = Channel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def channels_delete(name):  # noqa: E501
    """Delete a channel from the channels list

    Delete a channel # noqa: E501

    :param name: 
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def channels_read_all(length=None, offset=None):  # noqa: E501
    """Read the entire channels list

    Read the channels lists # noqa: E501

    :param length: Number of channels to get from channels
    :type length: int
    :param offset: Offset from beginning of list where to start gathering channels
    :type offset: int

    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'


def channels_read_one(name):  # noqa: E501
    """Read one channel from the channels list

    Read one channel from the channels list # noqa: E501

    :param name: Name of the channel to get from the list
    :type name: str

    :rtype: object
    """
    return 'do some magic!'


def channels_update(name, channel=None):  # noqa: E501
    """Update a channel in the channels list

    Update a channel in the channels list # noqa: E501

    :param name: Name of the channel to update in the list
    :type name: str
    :param channel: 
    :type channel: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        channel = Channel1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
