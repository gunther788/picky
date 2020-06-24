from flask import Flask
app = Flask(__name__)

import connexion
import six

from swagger_server.models.host import Host  # noqa: E501
from swagger_server import util
from swagger_server import data
from flask import make_response, abort

from swagger_server.data import HOSTS
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
    key = f"{body.channel}!{body.name}"
    if key not in HOSTS:
        HOSTS[key] = body
        hosts_notify(key)
        return make_response(f"{body.name} in {body.channel} successfully created", 201)

    else:
        abort(f"Host with name {body.name} and channel {body.channel} already exists", 406)


def hosts_delete(key):  # noqa: E501
    """Delete a host from the hosts list

    Delete a host # noqa: E501

    :param key: Channel!Name of the host to delete from the list
    :type key: str

    :rtype: None
    """
    # Does the host to delete exist?
    if key in HOSTS:
        host = HOSTS[key]
        name = host.name
        channel = host.channel
        del HOSTS[key]
        return make_response(f"{name} in {channel} successfully deleted", 200)

    # Otherwise, nope, host to delete not found
    else:
        abort("Entry {key} not found", 404)


def hosts_patch(key):  # noqa: E501
    """Rebuild the services list of a host

    Rebuild the services list of a host # noqa: E501

    :param key: Channel!Name of the host to update in the list
    :type key: str

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


def hosts_read_one(key):  # noqa: E501
    """Read one host from the hosts list

    Read one host from the hosts list # noqa: E501

    :param key: Channel!Name of the host to get from the list
    :type key: str

    :rtype: Host
    """
    # Does the host to delete exist?
    if key in HOSTS:
        return HOSTS[key]

    # Otherwise, nope, host to delete not found
    else:
        abort("Host with key {key} not found", 404)


def hosts_update(key, body=None):  # noqa: E501
    """Update a host in the hosts list

    Update a host in the hosts list # noqa: E501

    :param key: Channel!Name of the host to update in the list
    :type key: str
    :param body:
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Host.from_dict(connexion.request.get_json())  # noqa: E501

    if key not in HOSTS and key is not None:
        return hosts_create(body)

    host = HOSTS[key]

    if body.messages:
        for channel in host.messages:
            if channel in body.messages:
                body.messages[channel] = host.messages[channel]
        host.messages = body.messages

    if body.state:
        host.state = body.state

    if body.output:
        host.output = body.output.replace('\n', ' ')[:100]

    if body.timestamp:
        host.timestamp = body.timestamp

    hosts_notify(key)

    return make_response(f"{key} successfully updated", 201)
