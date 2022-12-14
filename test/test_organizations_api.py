"""
    ZeroTier Central API

    ZeroTier Central Network Management Portal API.<p>All API requests must have an API token header specified in the <code>Authorization: token xxxxx</code> format.  You can generate your API key by logging into <a href=\"https://my.zerotier.com\">ZeroTier Central</a> and creating a token on the Account page.</p><p>eg. <code>curl -X GET -H \"Authorization: token xxxxx\" https://api.zerotier.com/api/v1/network</code></p><p><h3>Rate Limiting</h3></p><p>The ZeroTier Central API implements rate limiting.  Paid users are limited to 100 requests per second.  Free users are limited to 20 requests per second.</p> <p> You can get the OpenAPI spec here as well: <code>https://docs.zerotier.com/openapi/centralv1.json</code></p>  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.organizations_api import OrganizationsApi  # noqa: E501


class TestOrganizationsApi(unittest.TestCase):
    """OrganizationsApi unit test stubs"""

    def setUp(self):
        self.api = OrganizationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accept_invitation(self):
        """Test case for accept_invitation

        Accept organization invitation  # noqa: E501
        """
        pass

    def test_decline_invitation(self):
        """Test case for decline_invitation

        Decline organization invitation  # noqa: E501
        """
        pass

    def test_get_invitation_by_id(self):
        """Test case for get_invitation_by_id

        Get organization invitation  # noqa: E501
        """
        pass

    def test_get_organization(self):
        """Test case for get_organization

        Get the current user's organization  # noqa: E501
        """
        pass

    def test_get_organization_by_id(self):
        """Test case for get_organization_by_id

        Get organization by ID  # noqa: E501
        """
        pass

    def test_get_organization_invitation_list(self):
        """Test case for get_organization_invitation_list

        Get list of organization invitations  # noqa: E501
        """
        pass

    def test_get_organization_members(self):
        """Test case for get_organization_members

        Get list of organization members  # noqa: E501
        """
        pass

    def test_invite_user_by_email(self):
        """Test case for invite_user_by_email

        Invite a user to your organization by email  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
