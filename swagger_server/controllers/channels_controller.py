import connexion
import six

from swagger_server.models.channel import Channel  # noqa: E501
from swagger_server import util


def get_channels():  # noqa: E501
    """Get all channels

    Get all channels # noqa: E501


    :rtype: List[Channel]
    """
    return 'do some magic!'


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
    return 'do some magic!'


def reset_channels():  # noqa: E501
    """Flush data and start notifications anew

    Flush data and start notifications anew # noqa: E501


    :rtype: List[Channel]
    """
    return 'do some magic!'
