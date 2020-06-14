# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.service import Service  # noqa: E501
from swagger_server.test import BaseTestCase


class TestServicesController(BaseTestCase):
    """ServicesController integration test stubs"""

    def test_services_create(self):
        """Test case for services_create

        Create a service and add it to the services list
        """
        body = Service()
        response = self.client.open(
            '/services',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_services_delete(self):
        """Test case for services_delete

        Delete a service from the services list
        """
        response = self.client.open(
            '/services/{name}'.format(name='name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_services_read_all(self):
        """Test case for services_read_all

        Read the entire services list
        """
        query_string = [('length', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/services',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_services_read_one(self):
        """Test case for services_read_one

        Read one service from the services list
        """
        response = self.client.open(
            '/services/{name}'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_services_update(self):
        """Test case for services_update

        Update a service in the services list
        """
        body = Service()
        response = self.client.open(
            '/services/{name}'.format(name='name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
