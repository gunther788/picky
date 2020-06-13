# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.channel import Channel  # noqa: E501
from swagger_server.models.channel1 import Channel1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestChannelsController(BaseTestCase):
    """ChannelsController integration test stubs"""

    def test_channels_create(self):
        """Test case for channels_create

        Create a channel and add it to the channels list
        """
        channel = Channel()
        response = self.client.open(
            '/gunther788/picky/1.0.0/channels',
            method='POST',
            data=json.dumps(channel),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_channels_delete(self):
        """Test case for channels_delete

        Delete a channel from the channels list
        """
        response = self.client.open(
            '/gunther788/picky/1.0.0/channels/{name}'.format(name='name_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_channels_read_all(self):
        """Test case for channels_read_all

        Read the entire channels list
        """
        query_string = [('length', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/gunther788/picky/1.0.0/channels',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_channels_read_one(self):
        """Test case for channels_read_one

        Read one channel from the channels list
        """
        response = self.client.open(
            '/gunther788/picky/1.0.0/channels/{name}'.format(name='name_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_channels_update(self):
        """Test case for channels_update

        Update a channel in the channels list
        """
        channel = Channel1()
        response = self.client.open(
            '/gunther788/picky/1.0.0/channels/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(channel),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
