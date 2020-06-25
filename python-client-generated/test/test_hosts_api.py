# coding: utf-8

"""
    PICKY: Python ICinga2 to KeYbase

    A Bridge between Icinga2's Notifications and Keybase  # noqa: E501

    OpenAPI spec version: 1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.hosts_api import HostsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHostsApi(unittest.TestCase):
    """HostsApi unit test stubs"""

    def setUp(self):
        self.api = api.hosts_api.HostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_hosts_create(self):
        """Test case for hosts_create

        Create a host and add it to the hosts-channel list  # noqa: E501
        """
        pass

    def test_hosts_delete(self):
        """Test case for hosts_delete

        Delete a host from the hosts-channel list  # noqa: E501
        """
        pass

    def test_hosts_patch(self):
        """Test case for hosts_patch

        Rebuild the services list of a hosts-channel entry  # noqa: E501
        """
        pass

    def test_hosts_read_all(self):
        """Test case for hosts_read_all

        Read the entire hosts-channel list  # noqa: E501
        """
        pass

    def test_hosts_read_one_host(self):
        """Test case for hosts_read_one_host

        Read one host from the hosts list across all channels  # noqa: E501
        """
        pass

    def test_hosts_read_one_host_channel(self):
        """Test case for hosts_read_one_host_channel

        Read one entry from the hosts-channel list  # noqa: E501
        """
        pass

    def test_hosts_update(self):
        """Test case for hosts_update

        Update a host in the hosts-channel list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()