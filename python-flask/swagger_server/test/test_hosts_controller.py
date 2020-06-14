# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.host import Host  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHostsController(BaseTestCase):
    """HostsController integration test stubs"""

    def test_hosts_create(self):
        """Test case for hosts_create

        Create a host and add it to the hosts list
        """
        body = Host()
        response = self.client.open(
            '/hosts',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hosts_delete(self):
        """Test case for hosts_delete

        Delete a host from the hosts list
        """
        response = self.client.open(
            '/hosts/{name}'.format(name='name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hosts_patch(self):
        """Test case for hosts_patch

        Rebuild the services list of a host
        """
        response = self.client.open(
            '/hosts/{name}'.format(name='name_example'),
            method='PATCH')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hosts_read_all(self):
        """Test case for hosts_read_all

        Read the entire hosts list
        """
        query_string = [('length', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/hosts',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hosts_read_one(self):
        """Test case for hosts_read_one

        Read one host from the hosts list
        """
        response = self.client.open(
            '/hosts/{name}'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hosts_update(self):
        """Test case for hosts_update

        Update a host in the hosts list
        """
        body = Host()
        response = self.client.open(
            '/hosts/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
