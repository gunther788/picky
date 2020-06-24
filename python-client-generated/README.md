# swagger-client
A Bridge between Icinga2's Notifications and Keybase

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Host() # Host | Host to create

try:
    # Create a host and add it to the hosts list
    api_instance.hosts_create(body)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_create: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Delete a host from the hosts list
    api_instance.hosts_delete(name)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_delete: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Rebuild the services list of a host
    api_instance.hosts_patch(name)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_patch: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
length = 56 # int | Number of hosts to get from hosts (optional)
offset = 56 # int | Offset from beginning of list where to start gathering hosts (optional)

try:
    # Read the entire hosts list
    api_response = api_instance.hosts_read_all(length=length, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_read_all: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of the host to get from the list

try:
    # Read one host from the hosts list
    api_response = api_instance.hosts_read_one(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_read_one: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.HostsApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of the host to update in the list
body = swagger_client.Host() # Host |  (optional)

try:
    # Update a host in the hosts list
    api_instance.hosts_update(name, body=body)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_update: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HostsApi* | [**hosts_create**](docs/HostsApi.md#hosts_create) | **POST** /hosts | Create a host and add it to the hosts list
*HostsApi* | [**hosts_delete**](docs/HostsApi.md#hosts_delete) | **DELETE** /hosts/{name} | Delete a host from the hosts list
*HostsApi* | [**hosts_patch**](docs/HostsApi.md#hosts_patch) | **PATCH** /hosts/{name} | Rebuild the services list of a host
*HostsApi* | [**hosts_read_all**](docs/HostsApi.md#hosts_read_all) | **GET** /hosts | Read the entire hosts list
*HostsApi* | [**hosts_read_one**](docs/HostsApi.md#hosts_read_one) | **GET** /hosts/{name} | Read one host from the hosts list
*HostsApi* | [**hosts_update**](docs/HostsApi.md#hosts_update) | **PUT** /hosts/{name} | Update a host in the hosts list
*ServicesApi* | [**services_create**](docs/ServicesApi.md#services_create) | **POST** /services | Create a service and add it to the services list
*ServicesApi* | [**services_delete**](docs/ServicesApi.md#services_delete) | **DELETE** /services/{name} | Delete a service from the services list
*ServicesApi* | [**services_read_all**](docs/ServicesApi.md#services_read_all) | **GET** /services | Read the entire services list
*ServicesApi* | [**services_read_one**](docs/ServicesApi.md#services_read_one) | **GET** /services/{name} | Read one service from the services list
*ServicesApi* | [**services_update**](docs/ServicesApi.md#services_update) | **PUT** /services/{name} | Update a service in the services list

## Documentation For Models

 - [Host](docs/Host.md)
 - [Service](docs/Service.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

