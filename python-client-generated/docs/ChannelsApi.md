# swagger_client.ChannelsApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channels_create**](ChannelsApi.md#channels_create) | **POST** /channels | Create a channel and add it to the channels list
[**channels_delete**](ChannelsApi.md#channels_delete) | **DELETE** /channels/{name} | Delete a channel from the channels list
[**channels_read_all**](ChannelsApi.md#channels_read_all) | **GET** /channels | Read the entire channels list
[**channels_read_one**](ChannelsApi.md#channels_read_one) | **GET** /channels/{name} | Read one channel from the channels list
[**channels_update**](ChannelsApi.md#channels_update) | **PUT** /channels/{name} | Update a channel in the channels list

# **channels_create**
> channels_create(body)

Create a channel and add it to the channels list

Create a new channel in the channels list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelsApi()
body = swagger_client.Channel() # Channel | Channel to create

try:
    # Create a channel and add it to the channels list
    api_instance.channels_create(body)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Channel**](Channel.md)| Channel to create | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_delete**
> channels_delete(name)

Delete a channel from the channels list

Delete a channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelsApi()
name = 'name_example' # str | 

try:
    # Delete a channel from the channels list
    api_instance.channels_delete(name)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_delete: %s\n" % e)
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

# **channels_read_all**
> list[Channel] channels_read_all(length=length, offset=offset)

Read the entire channels list

Read the channels lists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelsApi()
length = 56 # int | Number of channels to get from channels (optional)
offset = 56 # int | Offset from beginning of list where to start gathering channels (optional)

try:
    # Read the entire channels list
    api_response = api_instance.channels_read_all(length=length, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_read_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **length** | **int**| Number of channels to get from channels | [optional] 
 **offset** | **int**| Offset from beginning of list where to start gathering channels | [optional] 

### Return type

[**list[Channel]**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_read_one**
> Channel channels_read_one(name)

Read one channel from the channels list

Read one channel from the channels list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelsApi()
name = 'name_example' # str | Name of the channel to get from the list

try:
    # Read one channel from the channels list
    api_response = api_instance.channels_read_one(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_read_one: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the channel to get from the list | 

### Return type

[**Channel**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_update**
> channels_update(name, body=body)

Update a channel in the channels list

Update a channel in the channels list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelsApi()
name = 'name_example' # str | Name of the channel to update in the list
body = swagger_client.Channel() # Channel |  (optional)

try:
    # Update a channel in the channels list
    api_instance.channels_update(name, body=body)
except ApiException as e:
    print("Exception when calling ChannelsApi->channels_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the channel to update in the list | 
 **body** | [**Channel**](Channel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

