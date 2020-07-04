import connexion
import six

from swagger_server.models.channel import Channel  # noqa: E501
from swagger_server import util
from swagger_server import core


def get_channels():  # noqa: E501
    """Get all channels

    Get all channels # noqa: E501


    :rtype: List[Channel]
    """
    return core.get_channels()


def put_channel(channel, body=None):  # noqa: E501
    """Add a channel

    Add a channel # noqa: E501

    :param channel: Name of the channel
    :type channel: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Channel.from_dict(connexion.request.get_json())  # noqa: E501
    return core.put_channel(channel, body)
