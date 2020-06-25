import connexion
import six

from swagger_server.models.host import Host  # noqa: E501
from swagger_server import util


def hosts_create(body):  # noqa: E501
    """Create a host and add it to the hosts-channel list

    Create a new host in the hosts-channel list # noqa: E501

    :param body: Host to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Host.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def hosts_delete(name, channel):  # noqa: E501
    """Delete a host from the hosts-channel list

    Delete a host # noqa: E501

    :param name: Channel!Name of the host to delete from the list
    :type name: str
    :param channel: Channel being notified for this host
    :type channel: str

    :rtype: None
    """
    return 'do some magic!'


def hosts_patch(name, channel):  # noqa: E501
    """Rebuild the services list of a hosts-channel entry

    Rebuild the services list of a hosts-channel entry # noqa: E501

    :param name: Name of the host to update in the list
    :type name: str
    :param channel: Channel being notified for this host
    :type channel: str

    :rtype: None
    """
    return 'do some magic!'


def hosts_read_all(length=None, offset=None):  # noqa: E501
    """Read the entire hosts-channel list

    Read the hosts-channel list # noqa: E501

    :param length: Number of hosts to get from hosts
    :type length: int
    :param offset: Offset from beginning of list where to start gathering hosts
    :type offset: int

    :rtype: List[Host]
    """
    return 'do some magic!'


def hosts_read_one_host(name):  # noqa: E501
    """Read one host from the hosts list across all channels

    Read one host from the hosts list across all channels # noqa: E501

    :param name: Name of the host to get from the list
    :type name: str

    :rtype: Host
    """
    return 'do some magic!'


def hosts_read_one_host_channel(name, channel):  # noqa: E501
    """Read one entry from the hosts-channel list

    Read one entry from the hosts-channel list # noqa: E501

    :param name: Name of the host to get from the list
    :type name: str
    :param channel: Channel being notified for this host
    :type channel: str

    :rtype: Host
    """
    return 'do some magic!'


def hosts_update(name, channel, body=None):  # noqa: E501
    """Update a host in the hosts-channel list

    Update a host in the hosts-channel list # noqa: E501

    :param name: Name of the host to update in the list
    :type name: str
    :param channel: Channel being notified for this host
    :type channel: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Host.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
