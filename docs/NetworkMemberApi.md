# openapi_client.NetworkMemberApi

All URIs are relative to *https://api.zerotier.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_network_member**](NetworkMemberApi.md#delete_network_member) | **DELETE** /network/{networkID}/member/{memberID} | Delete a network member
[**get_network_member**](NetworkMemberApi.md#get_network_member) | **GET** /network/{networkID}/member/{memberID} | Return an individual member on a network
[**get_network_member_list**](NetworkMemberApi.md#get_network_member_list) | **GET** /network/{networkID}/member | Returns a list of Members on the network.
[**update_network_member**](NetworkMemberApi.md#update_network_member) | **POST** /network/{networkID}/member/{memberID} | Modify a network member


# **delete_network_member**
> delete_network_member(network_id, member_id)

Delete a network member

### Example


```python
import time
import openapi_client
from openapi_client.api import network_member_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_member_api.NetworkMemberApi(api_client)
    network_id = "networkID_example" # str | ID of the network
    member_id = "memberID_example" # str | ID of the member

    # example passing only required values which don't have defaults set
    try:
        # Delete a network member
        api_instance.delete_network_member(network_id, member_id)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworkMemberApi->delete_network_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| ID of the network |
 **member_id** | **str**| ID of the member |

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
**200** | member deleted |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_member**
> Member get_network_member(network_id, member_id)

Return an individual member on a network

### Example


```python
import time
import openapi_client
from openapi_client.api import network_member_api
from openapi_client.model.member import Member
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_member_api.NetworkMemberApi(api_client)
    network_id = "networkID_example" # str | ID of the network
    member_id = "memberID_example" # str | ID of the member

    # example passing only required values which don't have defaults set
    try:
        # Return an individual member on a network
        api_response = api_instance.get_network_member(network_id, member_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworkMemberApi->get_network_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| ID of the network |
 **member_id** | **str**| ID of the member |

### Return type

[**Member**](Member.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | member get success |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_member_list**
> [Member] get_network_member_list(network_id)

Returns a list of Members on the network.

### Example


```python
import time
import openapi_client
from openapi_client.api import network_member_api
from openapi_client.model.member import Member
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_member_api.NetworkMemberApi(api_client)
    network_id = "networkID_example" # str | ID of the network to return

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of Members on the network.
        api_response = api_instance.get_network_member_list(network_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworkMemberApi->get_network_member_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| ID of the network to return |

### Return type

[**[Member]**](Member.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | member list get success |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_member**
> Member update_network_member(network_id, member_id, member)

Modify a network member

### Example


```python
import time
import openapi_client
from openapi_client.api import network_member_api
from openapi_client.model.member import Member
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_member_api.NetworkMemberApi(api_client)
    network_id = "networkID_example" # str | ID of the network
    member_id = "memberID_example" # str | ID of the member
    member = Member(
        hidden=False,
        name="my-cray-supercomputer",
        description="My super awesome cray that I got ZeroTier to run on",
        config=MemberConfig(
            active_bridge=False,
            authorized=True,
            capabilities=[
                1,
            ],
            ip_assignments=["10.0.0.3"],
            no_auto_assign_ips=False,
            tags=[[123,456]],
        ),
    ) # Member | Member object JSON

    # example passing only required values which don't have defaults set
    try:
        # Modify a network member
        api_response = api_instance.update_network_member(network_id, member_id, member)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworkMemberApi->update_network_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| ID of the network |
 **member_id** | **str**| ID of the member |
 **member** | [**Member**](Member.md)| Member object JSON |

### Return type

[**Member**](Member.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | member changed successfully |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

