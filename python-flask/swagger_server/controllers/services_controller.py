import connexion
import six

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.service import Service  # noqa: E501
from swagger_server.models.service1 import Service1  # noqa: E501
from swagger_server import util


def services_create(service):  # noqa: E501
    """Create a service and add it to the services list

    Create a new service in the services list # noqa: E501

    :param service: Service to create
    :type service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        service = Service.from_dict(connexion.request.get_json())  # noqa: E501
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

    :rtype: List[InlineResponse2002]
    """
    return 'do some magic!'


def services_read_one(name):  # noqa: E501
    """Read one service from the services list

    Read one service from the services list # noqa: E501

    :param name: Name of the service to get from the list
    :type name: str

    :rtype: object
    """
    return 'do some magic!'


def services_update(name, service=None):  # noqa: E501
    """Update a service in the services list

    Update a service in the services list # noqa: E501

    :param name: Name of the service to update in the list
    :type name: str
    :param service: 
    :type service: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        service = Service1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
