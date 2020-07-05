# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.channel import Channel  # noqa: E501
from swagger_server.test import BaseTestCase


class TestChannelsController(BaseTestCase):
    """ChannelsController integration test stubs"""

    def test_get_channels(self):
        """Test case for get_channels

        Get all channels
        """
        response = self.client.open(
            '//',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_channel(self):
        """Test case for put_channel

        Add a channel
        """
        body = Channel()
        response = self.client.open(
            '//{channel}'.format(channel='channel_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reset_channels(self):
        """Test case for reset_channels

        Flush data and start notifications anew
        """
        response = self.client.open(
            '//reset',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
