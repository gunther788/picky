# swagger_client.HostsApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hosts_create**](HostsApi.md#hosts_create) | **POST** /hosts | Create a host and add it to the hosts-channel list
[**hosts_delete**](HostsApi.md#hosts_delete) | **DELETE** /hosts/{name}/{channel} | Delete a host from the hosts-channel list
[**hosts_patch**](HostsApi.md#hosts_patch) | **PATCH** /hosts/{name}/{channel} | Rebuild the services list of a hosts-channel entry
[**hosts_read_all**](HostsApi.md#hosts_read_all) | **GET** /hosts | Read the entire hosts-channel list
[**hosts_read_one_host**](HostsApi.md#hosts_read_one_host) | **GET** /hosts/{name} | Read one host from the hosts list across all channels
[**hosts_read_one_host_channel**](HostsApi.md#hosts_read_one_host_channel) | **GET** /hosts/{name}/{channel} | Read one entry from the hosts-channel list
[**hosts_update**](HostsApi.md#hosts_update) | **PUT** /hosts/{name}/{channel} | Update a host in the hosts-channel list

# **hosts_create**
> hosts_create(body)

Create a host and add it to the hosts-channel list

Create a new host in the hosts-channel list

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
    # Create a host and add it to the hosts-channel list
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
> hosts_delete(name, channel)

Delete a host from the hosts-channel list

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
name = 'name_example' # str | Name of the host to delete from the list
channel = 'channel_example' # str | Channel being notified for this host

try:
    # Delete a host from the hosts-channel list
    api_instance.hosts_delete(name, channel)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the host to delete from the list | 
 **channel** | **str**| Channel being notified for this host | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_patch**
> hosts_patch(name, channel)

Rebuild the services list of a hosts-channel entry

Rebuild the services list of a hosts-channel entry

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
channel = 'channel_example' # str | Channel being notified for this host

try:
    # Rebuild the services list of a hosts-channel entry
    api_instance.hosts_patch(name, channel)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the host to update in the list | 
 **channel** | **str**| Channel being notified for this host | 

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

Read the entire hosts-channel list

Read the hosts-channel list

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
    # Read the entire hosts-channel list
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

# **hosts_read_one_host**
> Host hosts_read_one_host(name)

Read one host from the hosts list across all channels

Read one host from the hosts list across all channels

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
    # Read one host from the hosts list across all channels
    api_response = api_instance.hosts_read_one_host(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_read_one_host: %s\n" % e)
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

# **hosts_read_one_host_channel**
> Host hosts_read_one_host_channel(name, channel)

Read one entry from the hosts-channel list

Read one entry from the hosts-channel list

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
channel = 'channel_example' # str | Channel being notified for this host

try:
    # Read one entry from the hosts-channel list
    api_response = api_instance.hosts_read_one_host_channel(name, channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_read_one_host_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the host to get from the list | 
 **channel** | **str**| Channel being notified for this host | 

### Return type

[**Host**](Host.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hosts_update**
> hosts_update(name, channel, body=body)

Update a host in the hosts-channel list

Update a host in the hosts-channel list

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
channel = 'channel_example' # str | Channel being notified for this host
body = swagger_client.Host() # Host |  (optional)

try:
    # Update a host in the hosts-channel list
    api_instance.hosts_update(name, channel, body=body)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the host to update in the list | 
 **channel** | **str**| Channel being notified for this host | 
 **body** | [**Host**](Host.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

