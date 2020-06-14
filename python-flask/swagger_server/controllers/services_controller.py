import connexion
import six

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.service import Service  # noqa: E501
from swagger_server import util


def services_create(body):  # noqa: E501
    """Create a service and add it to the services list

    Create a new service in the services list # noqa: E501

    :param body: Service to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Service.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def services_delete(name):  # noqa: E501
    """Delete a service from the services list

    Delete a service # noqa: E501

    :param name: 
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def services_read_all(length=None, offset=None):  # noqa: E501
    """Read the entire services list

    Read the services list # noqa: E501

    :param length: Number of services to get from services
    :type length: int
    :param offset: Offset from beginning of list where to start gathering services
    :type offset: int

    :rtype: List[Service]
    """
    return 'do some magic!'


def services_read_one(name):  # noqa: E501
    """Read one service from the services list

    Read one service from the services list # noqa: E501

    :param name: Name of the service to get from the list
    :type name: str

    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def services_update(name, body=None):  # noqa: E501
    """Update a service in the services list

    Update a service in the services list # noqa: E501

    :param name: Name of the service to update in the list
    :type name: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Service.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
