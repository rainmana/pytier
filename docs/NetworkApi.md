# openapi_client.NetworkApi

All URIs are relative to *https://api.zerotier.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_network**](NetworkApi.md#delete_network) | **DELETE** /network/{networkID} | delete network
[**get_network_by_id**](NetworkApi.md#get_network_by_id) | **GET** /network/{networkID} | Get network by ID
[**get_network_list**](NetworkApi.md#get_network_list) | **GET** /network | Returns a list of Networks you have access to.
[**new_network**](NetworkApi.md#new_network) | **POST** /network | Create a new network.
[**update_network**](NetworkApi.md#update_network) | **POST** /network/{networkID} | update network configuration


# **delete_network**
> delete_network(network_id)

delete network

### Example


```python
import time
import openapi_client
from openapi_client.api import network_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_api.NetworkApi(api_client)
    network_id = "networkID_example" # str | ID of the network

    # example passing only required values which don't have defaults set
    try:
        # delete network
        api_instance.delete_network(network_id)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworkApi->delete_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| ID of the network |

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
**200** | network deleted |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_by_id**
> Network get_network_by_id(network_id)

Get network by ID

Returns a single network

### Example


```python
import time
import openapi_client
from openapi_client.api import network_api
from openapi_client.model.network import Network
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_api.NetworkApi(api_client)
    network_id = "networkID_example" # str | ID of the network to return

    # example passing only required values which don't have defaults set
    try:
        # Get network by ID
        api_response = api_instance.get_network_by_id(network_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworkApi->get_network_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| ID of the network to return |

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get success |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_list**
> [Network] get_network_list()

Returns a list of Networks you have access to.

### Example


```python
import time
import openapi_client
from openapi_client.api import network_api
from openapi_client.model.network import Network
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_api.NetworkApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Returns a list of Networks you have access to.
        api_response = api_instance.get_network_list()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworkApi->get_network_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Network]**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** | Authorization required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **new_network**
> Network new_network(body)

Create a new network.

### Example


```python
import time
import openapi_client
from openapi_client.api import network_api
from openapi_client.model.network import Network
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_api.NetworkApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | empty JSON object

    # example passing only required values which don't have defaults set
    try:
        # Create a new network.
        api_response = api_instance.new_network(body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworkApi->new_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**| empty JSON object |

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network creation succeeded |  -  |
**403** | Authorization required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network**
> Network update_network(network_id, network)

update network configuration

### Example


```python
import time
import openapi_client
from openapi_client.api import network_api
from openapi_client.model.network import Network
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_api.NetworkApi(api_client)
    network_id = "networkID_example" # str | ID of the network to change
    network = Network(
        config=NetworkConfig(
            capabilities=[
                {},
            ],
            dns=DNS(
                domain="some.domain",
                servers=["10.0.0.3"],
            ),
            enable_broadcast=True,
            ip_assignment_pools=[
                IPRange(
                    ip_range_start="10.0.0.1",
                    ip_range_end="10.0.0.255",
                ),
            ],
            mtu=2800,
            multicast_limit=32,
            name="My ZeroTier Network",
            private=True,
            routes=[
                Route(
                    target="10.0.0.0/24",
                    via="via_example",
                ),
            ],
            rules=[
                {},
            ],
            tags=[
                {},
            ],
            v4_assign_mode=IPV4AssignMode(
                zt=True,
            ),
            v6_assign_mode=IPV6AssignMode(
                _6plane=True,
                rfc4193=False,
                zt=False,
            ),
        ),
        description="Some descriptive text about my network.",
        rules_source="accept;",
        permissions=PermissionsMap(
            key=Permissions(
                a=True,
                d=True,
                m=True,
                r=True,
            ),
        ),
        owner_id="00000000-0000-0000-0000-000000000000",
        capabilities_by_name={},
        tags_by_name={},
    ) # Network | Network object JSON

    # example passing only required values which don't have defaults set
    try:
        # update network configuration
        api_response = api_instance.update_network(network_id, network)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NetworkApi->update_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| ID of the network to change |
 **network** | [**Network**](Network.md)| Network object JSON |

### Return type

[**Network**](Network.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

