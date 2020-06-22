from flask import Flask
app = Flask(__name__)

import connexion
import six

from swagger_server.models.channel import Channel  # noqa: E501
from swagger_server import util

from swagger_server import data
from flask import make_response, abort

from swagger_server.data import CHANNELS
from swagger_server.sender import channels_notify


def channels_create(body):  # noqa: E501
    """Create a channel and add it to the channels list

    Create a new channel in the channels list # noqa: E501

    :param body: Channel to create
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Channel.from_dict(connexion.request.get_json())  # noqa: E501

    name = body.name
    if name not in CHANNELS and name is not None:
        CHANNELS[name] = body
        channels_notify(name)
        return make_response(
            "{name} successfully created".format(name=name), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Channel with name {name} already exists".format(name=name),
        )


def channels_delete(name):  # noqa: E501
    """Delete a channel from the channels list

    Delete a channel # noqa: E501

    :param name: 
    :type name: str

    :rtype: None
    """
    # Does the host to delete exist?
    if name in CHANNELS:
        del CHANNELS[name]
        return make_response(
            "{name} successfully deleted".format(name=name), 200
        )

    # Otherwise, nope, host to delete not found
    else:
        abort(
            404, "Channel with name {name} not found".format(name=name)
        )


def channels_read_all(length=None, offset=None):  # noqa: E501
    """Read the entire channels list

    Read the channels lists # noqa: E501

    :param length: Number of channels to get from channels
    :type length: int
    :param offset: Offset from beginning of list where to start gathering channels
    :type offset: int

    :rtype: List[Channel]
    """
    return [CHANNELS[key] for key in sorted(CHANNELS.keys())]


def channels_read_one(name):  # noqa: E501
    """Read one channel from the channels list

    Read one channel from the channels list # noqa: E501

    :param name: Name of the channel to get from the list
    :type name: str

    :rtype: Channel
    """
    # Does the host to delete exist?
    if name in CHANNELS:
        return CHANNELS[name]

    # Otherwise, nope, host to delete not found
    else:
        abort(
            404, "Channel with name {name} not found".format(name=name)
        )


def channels_update(name, body=None):  # noqa: E501
    """Update a channel in the channels list

    Update a channel in the channels list # noqa: E501

    :param name: Name of the channel to update in the list
    :type name: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Channel.from_dict(connexion.request.get_json())  # noqa: E501

    if body.timestamp:
        CHANNELS[name].timestamp = body.timestamp
