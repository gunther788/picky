# swagger_client.ChannelsApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_channels**](ChannelsApi.md#get_channels) | **GET** / | Get all channels
[**put_channel**](ChannelsApi.md#put_channel) | **PUT** /{channel} | Add a channel

# **get_channels**
> list[Channel] get_channels()

Get all channels

Get all channels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelsApi()

try:
    # Get all channels
    api_response = api_instance.get_channels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_channels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Channel]**](Channel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_channel**
> put_channel(channel, body=body)

Add a channel

Add a channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ChannelsApi()
channel = 'channel_example' # str | Name of the channel
body = swagger_client.Channel() # Channel |  (optional)

try:
    # Add a channel
    api_instance.put_channel(channel, body=body)
except ApiException as e:
    print("Exception when calling ChannelsApi->put_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**| Name of the channel | 
 **body** | [**Channel**](Channel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

