# swagger_client.ServicesApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**services_create**](ServicesApi.md#services_create) | **POST** /services | Create a service and add it to the services list
[**services_delete**](ServicesApi.md#services_delete) | **DELETE** /services/{host}/{name} | Delete a service from the services list
[**services_read_all**](ServicesApi.md#services_read_all) | **GET** /services/{host} | Read all services from one host
[**services_read_one**](ServicesApi.md#services_read_one) | **GET** /services/{host}/{name} | Read one service from the services list
[**services_update**](ServicesApi.md#services_update) | **PUT** /services/{host}/{name} | Update a service in the services list

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
> services_delete(host, name)

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
host = 'host_example' # str | Host of the service to delete from the list
name = 'name_example' # str | Name of the service to delete the list

try:
    # Delete a service from the services list
    api_instance.services_delete(host, name)
except ApiException as e:
    print("Exception when calling ServicesApi->services_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Host of the service to delete from the list | 
 **name** | **str**| Name of the service to delete the list | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_read_all**
> Service services_read_all(host)

Read all services from one host

Read all services from one host

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
host = 'host_example' # str | Host of the service to get from the list

try:
    # Read all services from one host
    api_response = api_instance.services_read_all(host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->services_read_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Host of the service to get from the list | 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_read_one**
> Service services_read_one(host, name)

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
host = 'host_example' # str | Host of the service to get from the list
name = 'name_example' # str | Name of the service to get from the list

try:
    # Read one service from the services list
    api_response = api_instance.services_read_one(host, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->services_read_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Host of the service to get from the list | 
 **name** | **str**| Name of the service to get from the list | 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_update**
> services_update(host, name, body=body)

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
host = 'host_example' # str | Host of the service to update in the list
name = 'name_example' # str | Name of the service to update in the list
body = swagger_client.Service() # Service |  (optional)

try:
    # Update a service in the services list
    api_instance.services_update(host, name, body=body)
except ApiException as e:
    print("Exception when calling ServicesApi->services_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Host of the service to update in the list | 
 **name** | **str**| Name of the service to update in the list | 
 **body** | [**Service**](Service.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

