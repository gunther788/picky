# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.host import Host  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHostsController(BaseTestCase):
    """HostsController integration test stubs"""

    def test_get_hosts(self):
        """Test case for get_hosts

        Get all hosts in a channel
        """
        response = self.client.open(
            '//{channel}'.format(channel='channel_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_host(self):
        """Test case for put_host

        Host notification
        """
        body = Host()
        response = self.client.open(
            '//{channel}/{host}'.format(channel='channel_example', host='host_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
