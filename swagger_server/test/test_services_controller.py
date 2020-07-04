# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.service import Service  # noqa: E501
from swagger_server.test import BaseTestCase


class TestServicesController(BaseTestCase):
    """ServicesController integration test stubs"""

    def test_get_services(self):
        """Test case for get_services

        Get all services of a host
        """
        response = self.client.open(
            '//{channel}/{host}'.format(channel='channel_example', host='host_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_service(self):
        """Test case for put_service

        Service notification
        """
        body = Service()
        response = self.client.open(
            '//{channel}/{host}/{service}'.format(channel='channel_example', host='host_example', service='service_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
