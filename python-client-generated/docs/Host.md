# Host

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of host | [optional] 
**msg_id** | **int** | Message ID in the channel | [optional] [default to 0]
**state** | **str** |  | [optional] [default to 'UP']
**output** | **str** | Output of host check command | [optional] [default to '']
**services** | [**dict(str, Service)**](Service.md) |  | [optional] 
**timestamp** | **str** | Last update | [optional] 
**updates** | **int** | Update counter | [optional] [default to 0]
**sla** | **str** |  | [optional] [default to 'bronze']
**note_type** | **str** |  | [optional] [default to 'Problem']
**picky** | **str** | Message neatly formatted for Keybase | [optional] 
**url** | **str** | Link to this object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

