# openapi_client.UtilApi

All URIs are relative to *https://api.zerotier.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_random_token**](UtilApi.md#get_random_token) | **GET** /randomToken | Get a random 32 character token
[**get_status**](UtilApi.md#get_status) | **GET** /status | Obtain the overall status of the account tied to the API token in use.


# **get_random_token**
> RandomToken get_random_token()

Get a random 32 character token

Get a random 32 character.  Used by the web UI to generate API keys

### Example


```python
import time
import openapi_client
from openapi_client.api import util_api
from openapi_client.model.random_token import RandomToken
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = util_api.UtilApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get a random 32 character token
        api_response = api_instance.get_random_token()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UtilApi->get_random_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RandomToken**](RandomToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Random token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> Status get_status()

Obtain the overall status of the account tied to the API token in use.

### Example


```python
import time
import openapi_client
from openapi_client.api import util_api
from openapi_client.model.status import Status
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = util_api.UtilApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Obtain the overall status of the account tied to the API token in use.
        api_response = api_instance.get_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UtilApi->get_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

