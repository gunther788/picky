import connexion
import six

from swagger_server.models.host import Host  # noqa: E501
from swagger_server import util
from swagger_server import core


def get_hosts(channel):  # noqa: E501
    """Get all hosts in a channel

    Get all hosts in a channel # noqa: E501

    :param channel: Name of the channel to get all the hosts
    :type channel: str

    :rtype: List[Host]
    """
    return core.get_hosts(channel)


def put_host(channel, host, body=None):  # noqa: E501
    """Host notification

    Host notification # noqa: E501

    :param channel: Name of the channel
    :type channel: str
    :param host: Name of the host
    :type host: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Host.from_dict(connexion.request.get_json())  # noqa: E501
    return core.put_host(channel, host, body)
