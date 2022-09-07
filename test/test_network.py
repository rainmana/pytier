"""
    ZeroTier Central API

    ZeroTier Central Network Management Portal API.<p>All API requests must have an API token header specified in the <code>Authorization: token xxxxx</code> format.  You can generate your API key by logging into <a href=\"https://my.zerotier.com\">ZeroTier Central</a> and creating a token on the Account page.</p><p>eg. <code>curl -X GET -H \"Authorization: token xxxxx\" https://api.zerotier.com/api/v1/network</code></p><p><h3>Rate Limiting</h3></p><p>The ZeroTier Central API implements rate limiting.  Paid users are limited to 100 requests per second.  Free users are limited to 20 requests per second.</p> <p> You can get the OpenAPI spec here as well: <code>https://docs.zerotier.com/openapi/centralv1.json</code></p>  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.network_config import NetworkConfig
from openapi_client.model.permissions_map import PermissionsMap
globals()['NetworkConfig'] = NetworkConfig
globals()['PermissionsMap'] = PermissionsMap
from openapi_client.model.network import Network


class TestNetwork(unittest.TestCase):
    """Network unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNetwork(self):
        """Test Network"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Network()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
