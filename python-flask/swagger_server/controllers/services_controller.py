import connexion
import six

from swagger_server.models.service import Service  # noqa: E501
from swagger_server import util
from swagger_server import core


def get_services(channel, host):  # noqa: E501
    """Get all services of a host

    Get all services of a host # noqa: E501

    :param channel: Name of the channel
    :type channel: str
    :param host: Name of the host
    :type host: str

    :rtype: List[Service]
    """
    return core.get_services(channel, host)


def put_service(channel, host, service, body=None):  # noqa: E501
    """Service notification

    Service notification # noqa: E501

    :param channel: Name of the channel
    :type channel: str
    :param host: Name of the host
    :type host: str
    :param service: Name of the service
    :type service: str
    :param body:
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Service.from_dict(connexion.request.get_json())  # noqa: E501
    return core.put_service(channel, host, service, body)
