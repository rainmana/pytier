# openapi_client.OrganizationsApi

All URIs are relative to *https://api.zerotier.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation**](OrganizationsApi.md#accept_invitation) | **POST** /org-invitation/{inviteID} | Accept organization invitation
[**decline_invitation**](OrganizationsApi.md#decline_invitation) | **DELETE** /org-invitation/{inviteID} | Decline organization invitation
[**get_invitation_by_id**](OrganizationsApi.md#get_invitation_by_id) | **GET** /org-invitation/{inviteID} | Get organization invitation
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /org | Get the current user&#39;s organization
[**get_organization_by_id**](OrganizationsApi.md#get_organization_by_id) | **GET** /org/{orgID} | Get organization by ID
[**get_organization_invitation_list**](OrganizationsApi.md#get_organization_invitation_list) | **GET** /org-invitation | Get list of organization invitations
[**get_organization_members**](OrganizationsApi.md#get_organization_members) | **GET** /org/{orgID}/user | Get list of organization members
[**invite_user_by_email**](OrganizationsApi.md#invite_user_by_email) | **POST** /org-invitation | Invite a user to your organization by email


# **accept_invitation**
> OrganizationInvitation accept_invitation(invite_id)

Accept organization invitation

### Example


```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.organization_invitation import OrganizationInvitation
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    invite_id = "inviteID_example" # str | Invitation ID

    # example passing only required values which don't have defaults set
    try:
        # Accept organization invitation
        api_response = api_instance.accept_invitation(invite_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->accept_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**| Invitation ID |

### Return type

[**OrganizationInvitation**](OrganizationInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization invitation accepted |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decline_invitation**
> decline_invitation(invite_id)

Decline organization invitation

### Example


```python
import time
import openapi_client
from openapi_client.api import organizations_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    invite_id = "inviteID_example" # str | Invitation ID

    # example passing only required values which don't have defaults set
    try:
        # Decline organization invitation
        api_instance.decline_invitation(invite_id)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->decline_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**| Invitation ID |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | organization invitation declined |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitation_by_id**
> OrganizationInvitation get_invitation_by_id(invite_id)

Get organization invitation

### Example


```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.organization_invitation import OrganizationInvitation
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    invite_id = "inviteID_example" # str | Invitation ID

    # example passing only required values which don't have defaults set
    try:
        # Get organization invitation
        api_response = api_instance.get_invitation_by_id(invite_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->get_invitation_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**| Invitation ID |

### Return type

[**OrganizationInvitation**](OrganizationInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get organization invitation |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> Organization get_organization()

Get the current user's organization

### Example


```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.organization import Organization
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current user's organization
        api_response = api_instance.get_organization()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get my organization |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_by_id**
> Organization get_organization_by_id(org_id)

Get organization by ID

### Example


```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.organization import Organization
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    org_id = "orgID_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get organization by ID
        api_response = api_instance.get_organization_by_id(org_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organization_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID |

### Return type

[**Organization**](Organization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_invitation_list**
> [OrganizationInvitation] get_organization_invitation_list()

Get list of organization invitations

### Example


```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.organization_invitation import OrganizationInvitation
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get list of organization invitations
        api_response = api_instance.get_organization_invitation_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organization_invitation_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[OrganizationInvitation]**](OrganizationInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get list of invitations |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_members**
> OrganizationMember get_organization_members(org_id)

Get list of organization members

### Example


```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.organization_member import OrganizationMember
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    org_id = "orgID_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get list of organization members
        api_response = api_instance.get_organization_members(org_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organization_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID |

### Return type

[**OrganizationMember**](OrganizationMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get organization members success |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user_by_email**
> OrganizationInvitation invite_user_by_email(organization_invitation)

Invite a user to your organization by email

### Example


```python
import time
import openapi_client
from openapi_client.api import organizations_api
from openapi_client.model.organization_invitation import OrganizationInvitation
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = organizations_api.OrganizationsApi(api_client)
    organization_invitation = OrganizationInvitation(
        email="joe@user.com",
    ) # OrganizationInvitation | Organization Invitation JSON object

    # example passing only required values which don't have defaults set
    try:
        # Invite a user to your organization by email
        api_response = api_instance.invite_user_by_email(organization_invitation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrganizationsApi->invite_user_by_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_invitation** | [**OrganizationInvitation**](OrganizationInvitation.md)| Organization Invitation JSON object |

### Return type

[**OrganizationInvitation**](OrganizationInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User invited to organization |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

