# swagger_client.ServicesApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_services**](ServicesApi.md#get_services) | **GET** /{channel}/{host} | Get all services of a host
[**put_service**](ServicesApi.md#put_service) | **PUT** /{channel}/{host}/{service} | Service notification

# **get_services**
> list[Service] get_services(channel, host)

Get all services of a host

Get all services of a host

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
channel = 'channel_example' # str | Name of the channel
host = 'host_example' # str | Name of the host

try:
    # Get all services of a host
    api_response = api_instance.get_services(channel, host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->get_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**| Name of the channel | 
 **host** | **str**| Name of the host | 

### Return type

[**list[Service]**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_service**
> put_service(channel, host, service, body=body)

Service notification

Service notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
channel = 'channel_example' # str | Name of the channel
host = 'host_example' # str | Name of the host
service = 'service_example' # str | Name of the service
body = swagger_client.Service() # Service |  (optional)

try:
    # Service notification
    api_instance.put_service(channel, host, service, body=body)
except ApiException as e:
    print("Exception when calling ServicesApi->put_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**| Name of the channel | 
 **host** | **str**| Name of the host | 
 **service** | **str**| Name of the service | 
 **body** | [**Service**](Service.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

