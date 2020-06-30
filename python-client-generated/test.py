from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

configuration = swagger_client.Configuration()
configuration.debug = True
configuration.host = "http://localhost:5000"

# create an instance of the API class
api_client = swagger_client.ApiClient(configuration=configuration)
api_instance = swagger_client.HostsApi(api_client=api_client)

body = swagger_client.Host() # Host |  (optional)
body.name = 'two.example.com'
body.channel = 'gold'
body.state = 'DOWN'
body.output = 'hm - no idea what happened...\nsecond line!'

try:
    # Update a host in the hosts list
    api_instance.put_host(body.channel, body.name, body=body)
except ApiException as e:
    print("Exception when calling HostsApi->put_host: %s\n" % e)
