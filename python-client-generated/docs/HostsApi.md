# swagger_client.HostsApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hosts_create**](HostsApi.md#hosts_create) | **POST** /hosts | Create a host and add it to the hosts list
[**hosts_delete**](HostsApi.md#hosts_delete) | **DELETE** /hosts/{name} | Delete a host from the hosts list
[**hosts_patch**](HostsApi.md#hosts_patch) | **PATCH** /hosts/{name} | Rebuild the services list of a host
[**hosts_read_all**](HostsApi.md#hosts_read_all) | **GET** /hosts | Read the entire hosts list
[**hosts_read_one**](HostsApi.md#hosts_read_one) | **GET** /hosts/{name} | Read one host from the hosts list
[**hosts_update**](HostsApi.md#hosts_update) | **PUT** /hosts/{name} | Update a host in the hosts list

# **hosts_create**
> hosts_create(body)

Create a host and add it to the hosts list

Create a new host in the hosts list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
body = swagger_client.Host() # Host | Host to create

try:
    # Create a host and add it to the hosts list
    api_instance.hosts_create(body)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Host**](Host.md)| Host to create | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_delete**
> hosts_delete(name)

Delete a host from the hosts list

Delete a host

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
name = 'name_example' # str | 

try:
    # Delete a host from the hosts list
    api_instance.hosts_delete(name)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_patch**
> hosts_patch(name)

Rebuild the services list of a host

Rebuild the services list of a host

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
name = 'name_example' # str | 

try:
    # Rebuild the services list of a host
    api_instance.hosts_patch(name)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_read_all**
> list[Host] hosts_read_all(length=length, offset=offset)

Read the entire hosts list

Read the hosts list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
length = 56 # int | Number of hosts to get from hosts (optional)
offset = 56 # int | Offset from beginning of list where to start gathering hosts (optional)

try:
    # Read the entire hosts list
    api_response = api_instance.hosts_read_all(length=length, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_read_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **length** | **int**| Number of hosts to get from hosts | [optional] 
 **offset** | **int**| Offset from beginning of list where to start gathering hosts | [optional] 

### Return type

[**list[Host]**](Host.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_read_one**
> Host hosts_read_one(name)

Read one host from the hosts list

Read one host from the hosts list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
name = 'name_example' # str | Name of the host to get from the list

try:
    # Read one host from the hosts list
    api_response = api_instance.hosts_read_one(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_read_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the host to get from the list | 

### Return type

[**Host**](Host.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_update**
> hosts_update(name, body=body)

Update a host in the hosts list

Update a host in the hosts list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi()
name = 'name_example' # str | Name of the host to update in the list
body = swagger_client.Host() # Host |  (optional)

try:
    # Update a host in the hosts list
    api_instance.hosts_update(name, body=body)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the host to update in the list | 
 **body** | [**Host**](Host.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

