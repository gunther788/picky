import connexion
import six

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


def services_delete(host, name):  # noqa: E501
    """Delete a service from the services list

    Delete a service # noqa: E501

    :param host: Host of the service to delete from the list
    :type host: str
    :param name: Name of the service to delete the list
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def services_read_all(host):  # noqa: E501
    """Read all services from one host

    Read all services from one host # noqa: E501

    :param host: Host of the service to get from the list
    :type host: str

    :rtype: Service
    """
    return 'do some magic!'


def services_read_one(host, name):  # noqa: E501
    """Read one service from the services list

    Read one service from the services list # noqa: E501

    :param host: Host of the service to get from the list
    :type host: str
    :param name: Name of the service to get from the list
    :type name: str

    :rtype: Service
    """
    return 'do some magic!'


def services_update(host, name, body=None):  # noqa: E501
    """Update a service in the services list

    Update a service in the services list # noqa: E501

    :param host: Host of the service to update in the list
    :type host: str
    :param name: Name of the service to update in the list
    :type name: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Service.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
