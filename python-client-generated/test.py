from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

configuration = swagger_client.Configuration()
configuration.debug = True

# create an instance of the API class
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.HostsApi(api_client=api_client)

name = 'two.example.com' # str | Name of the host to update in the list
body = swagger_client.Host() # Host |  (optional)
body.name = 'two.example.com'
body.messages = dict({"containers": 0})
body.state = 'UP'
body.timestamp = "sometime"

try:
    # Update a host in the hosts list
    api_instance.hosts_update(name, body=body)
except ApiException as e:
    print("Exception when calling HostsApi->hosts_update: %s\n" % e)
