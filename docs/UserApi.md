# openapi_client.UserApi

All URIs are relative to *https://api.zerotier.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_api_token**](UserApi.md#add_api_token) | **POST** /user/{userID}/token | Add an API token
[**delete_api_token**](UserApi.md#delete_api_token) | **DELETE** /user/{userID}/token/{tokenName} | Delete API Token
[**delete_user_by_id**](UserApi.md#delete_user_by_id) | **DELETE** /user/{userID} | Delete user
[**get_user_by_id**](UserApi.md#get_user_by_id) | **GET** /user/{userID} | Get user record
[**update_user_by_id**](UserApi.md#update_user_by_id) | **POST** /user/{userID} | Update user record (SMS number or Display Name only)


# **add_api_token**
> APIToken add_api_token(user_id, api_token)

Add an API token

### Example


```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.api_token import APIToken
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "userID_example" # str | User ID
    api_token = APIToken(
        token_name="my-super-secret-token",
        token="adsf98ashdkjh3689adsfnj3$ADn",
    ) # APIToken | APIToken JSON object

    # example passing only required values which don't have defaults set
    try:
        # Add an API token
        api_response = api_instance.add_api_token(user_id, api_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->add_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |
 **api_token** | [**APIToken**](APIToken.md)| APIToken JSON object |

### Return type

[**APIToken**](APIToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | API Token added |  -  |
**400** | Bad request |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_token**
> delete_api_token(user_id, token_name)

Delete API Token

### Example


```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "userID_example" # str | User ID
    token_name = "tokenName_example" # str | Token Name

    # example passing only required values which don't have defaults set
    try:
        # Delete API Token
        api_instance.delete_api_token(user_id, token_name)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->delete_api_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |
 **token_name** | **str**| Token Name |

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
**200** | API token deleted |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_by_id**
> delete_user_by_id(user_id)

Delete user

Deletes the user and all associated networks.  This is not reversible. Delete at your own risk.

### Example


```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "userID_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_instance.delete_user_by_id(user_id)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->delete_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

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
**200** | user deleted |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id**
> User get_user_by_id(user_id)

Get user record

### Example


```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "userID_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Get user record
        api_response = api_instance.get_user_by_id(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->get_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User get success |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_by_id**
> User update_user_by_id(user_id, user)

Update user record (SMS number or Display Name only)

### Example


```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to https://api.zerotier.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.zerotier.com/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "userID_example" # str | User ID
    user = User(
        display_name="Joe User",
        sms_number="+1-800-555-1212",
    ) # User | User object JSON

    # example passing only required values which don't have defaults set
    try:
        # Update user record (SMS number or Display Name only)
        api_response = api_instance.update_user_by_id(user_id, user)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->update_user_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID |
 **user** | [**User**](User.md)| User object JSON |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User update success |  -  |
**401** | Authorization required |  -  |
**403** | Access denied |  -  |
**404** | Item not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

