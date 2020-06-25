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
    """Create a host and add it to the hosts-channel list

    Create a new host in the hosts-channel list # noqa: E501

    :param body: Host to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Host.from_dict(connexion.request.get_json())  # noqa: E501

    app.logger.info(f"hosts_create({body})")
    key = f"{body.name}/{body.channel}"
    if key not in HOSTS:
        HOSTS[key] = body
        hosts_notify(key)
        return make_response(f"{body.name} in {body.channel} successfully created", 201)

    else:
        return make_response(f"Host with name {body.name} and channel {body.channel} already exists", 406)


def hosts_delete(name, channel):  # noqa: E501
    """Delete a host from the hosts-channel list

    Delete a host # noqa: E501

    :param name: Name of the host to delete from the list
    :type name: str
    :param channel: Channel being notified for this host
    :type channel: str

    :rtype: None
    """
    app.logger.info(f"hosts_delete({name}, {channel})")
    key = f"{name}/{channel}"

    # Does the host to delete exist?
    if key in HOSTS:
        del HOSTS[key]
        return make_response(f"{name} in {channel} successfully deleted", 200)

    # Otherwise, nope, host to delete not found
    else:
        return make_response(f"Entry {key} not found", 404)


def hosts_patch(name, channel):  # noqa: E501
    """Rebuild the services list of a hosts-channel entry

    Rebuild the services list of a hosts-channel entry # noqa: E501

    :param name: Name of the host to update in the list
    :type name: str
    :param channel: Channel being notified for this host
    :type channel: str

    :rtype: None
    """
    app.logger.info(f"hosts_patch({name}, {channel})")
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
    app.logger.info(f"hosts_read_all()")
    return [HOSTS[key] for key in sorted(HOSTS.keys())]


def hosts_read_one_host(name):  # noqa: E501
    """Read one host from the hosts list across all channels

    Read one host from the hosts list across all channels # noqa: E501

    :param name: Name of the host to get from the list
    :type name: str

    :rtype: Host
    """
    app.logger.info(f"hosts_read_one_host({name})")
    return [HOSTS[key] for key in sorted(HOSTS.keys()) if key.startswith(name + '/')]


def hosts_read_one_host_channel(name, channel):  # noqa: E501
    """Read one entry from the hosts-channel list

    Read one entry from the hosts-channel list # noqa: E501

    :param name: Name of the host to get from the list
    :type name: str
    :param channel: Channel being notified for this host
    :type channel: str

    :rtype: Host
    """
    app.logger.info(f"hosts_read_one_host_channel({name}, {channel})")
    key = f"{name}/{channel}"

    if key in HOSTS:
        return HOSTS[key]

    else:
        return make_response(f"Host with key {key} not found", 404)


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

    key = f"{name}/{channel}"

    if key not in HOSTS and key is not None:
        return hosts_create(body)

    host = HOSTS[key]

    if body.channel:
        body.channel = host.channel

    if body.msg_id:
        body.msg_id = host.msg_id

    if body.state:
        host.state = body.state

    if body.output:
        host.output = body.output.replace('\n', ' ')[:100]

    if body.timestamp:
        host.timestamp = body.timestamp

    hosts_notify(key)
    return make_response(f"{key} successfully updated", 201)
