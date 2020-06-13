import connexion
import six

from swagger_server.models.host import Host  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util


def hosts_create(body):  # noqa: E501
    """Create a host and add it to the hosts list

    Create a new host in the hosts list # noqa: E501

    :param body: Host to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Host.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def hosts_delete(name):  # noqa: E501
    """Delete a host from the hosts list

    Delete a host # noqa: E501

    :param name: 
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def hosts_patch(name):  # noqa: E501
    """Rebuild the services list of a host

    Rebuild the services list of a host # noqa: E501

    :param name: 
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def hosts_read_all(length=None, offset=None):  # noqa: E501
    """Read the entire hosts list

    Read the hosts list # noqa: E501

    :param length: Number of hosts to get from hosts
    :type length: int
    :param offset: Offset from beginning of list where to start gathering hosts
    :type offset: int

    :rtype: List[Host]
    """
    return 'do some magic!'


def hosts_read_one(name):  # noqa: E501
    """Read one host from the hosts list

    Read one host from the hosts list # noqa: E501

    :param name: Name of the host to get from the list
    :type name: str

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def hosts_update(name, body=None):  # noqa: E501
    """Update a host in the hosts list

    Update a host in the hosts list # noqa: E501

    :param name: Name of the host to update in the list
    :type name: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Host.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
