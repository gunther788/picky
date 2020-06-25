# swagger_client.ServicesApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**services_create**](ServicesApi.md#services_create) | **POST** /services | Create a service and add it to the services list
[**services_delete**](ServicesApi.md#services_delete) | **DELETE** /services/{key} | Delete a service from the services list
[**services_read_all**](ServicesApi.md#services_read_all) | **GET** /services | Read the entire services list
[**services_read_one**](ServicesApi.md#services_read_one) | **GET** /services/{key} | Read one service from the services list
[**services_update**](ServicesApi.md#services_update) | **PUT** /services/{key} | Update a service in the services list

# **services_create**
> services_create(body)

Create a service and add it to the services list

Create a new service in the services list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
body = swagger_client.Service() # Service | Service to create

try:
    # Create a service and add it to the services list
    api_instance.services_create(body)
except ApiException as e:
    print("Exception when calling ServicesApi->services_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Service**](Service.md)| Service to create | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_delete**
> services_delete(key)

Delete a service from the services list

Delete a service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
key = 'key_example' # str | Host!Service key of the service to delete from the list

try:
    # Delete a service from the services list
    api_instance.services_delete(key)
except ApiException as e:
    print("Exception when calling ServicesApi->services_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Host!Service key of the service to delete from the list | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_read_all**
> list[Service] services_read_all(length=length, offset=offset)

Read the entire services list

Read the services list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
length = 56 # int | Number of services to get from services (optional)
offset = 56 # int | Offset from beginning of list where to start gathering services (optional)

try:
    # Read the entire services list
    api_response = api_instance.services_read_all(length=length, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->services_read_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **length** | **int**| Number of services to get from services | [optional] 
 **offset** | **int**| Offset from beginning of list where to start gathering services | [optional] 

### Return type

[**list[Service]**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_read_one**
> Service services_read_one(key)

Read one service from the services list

Read one service from the services list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
key = 'key_example' # str | Host!Service key of the service to get from the list

try:
    # Read one service from the services list
    api_response = api_instance.services_read_one(key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->services_read_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Host!Service key of the service to get from the list | 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_update**
> services_update(key, body=body)

Update a service in the services list

Update a service in the services list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
key = 'key_example' # str | Host!Service key of the service to update in the list
body = swagger_client.Service() # Service |  (optional)

try:
    # Update a service in the services list
    api_instance.services_update(key, body=body)
except ApiException as e:
    print("Exception when calling ServicesApi->services_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Host!Service key of the service to update in the list | 
 **body** | [**Service**](Service.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

