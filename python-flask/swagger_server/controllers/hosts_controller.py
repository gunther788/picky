from flask import Flask
app = Flask(__name__)

import connexion
import six

from swagger_server.models.host import Host  # noqa: E501
from swagger_server import util
from swagger_server import data
from flask import make_response, abort

from swagger_server.data import HOSTS, CHANNELS
from swagger_server.sender import hosts_notify


def hosts_create(body):  # noqa: E501
    """Create a host and add it to the hosts list

    Create a new host in the hosts list # noqa: E501

    :param body: Host to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Host.from_dict(connexion.request.get_json())  # noqa: E501

    app.logger.info(f"hosts_create({body})")
    name = body.name
    if name not in HOSTS and name is not None:
        HOSTS[name] = body
        hosts_notify(name)
        return make_response(
            "{name} successfully created".format(name=name), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Host with name {name} already exists".format(name=name),
        )


def hosts_delete(name):  # noqa: E501
    """Delete a host from the hosts list

    Delete a host # noqa: E501

    :param name:
    :type name: str

    :rtype: None
    """
    # Does the host to delete exist?
    if name in HOSTS:
        del HOSTS[name]
        return make_response(
            "{name} successfully deleted".format(name=name), 200
        )

    # Otherwise, nope, host to delete not found
    else:
        abort(
            404, "Host with name {name} not found".format(name=name)
        )


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
    return [HOSTS[key] for key in sorted(HOSTS.keys())]


def hosts_read_one(name):  # noqa: E501
    """Read one host from the hosts list

    Read one host from the hosts list # noqa: E501

    :param name: Name of the host to get from the list
    :type name: str

    :rtype: Host
    """
    # Does the host to delete exist?
    if name in HOSTS:
        return HOSTS[name]

    # Otherwise, nope, host to delete not found
    else:
        abort(
            404, "Host with name {name} not found".format(name=name)
        )


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

    if name not in HOSTS and name is not None:
        return hosts_create(body)

    if body.state:
        HOSTS[name].state = body.state

    hosts_notify(name)
    return make_response(
        "{name} successfully updated".format(name=name), 201
    )
