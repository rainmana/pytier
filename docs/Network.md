# Network

Network object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** |  | [optional] [readonly] 
**clock** | **int, none_type** |  | [optional] [readonly] 
**config** | [**NetworkConfig**](NetworkConfig.md) |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**rules_source** | **str, none_type** |  | [optional] 
**permissions** | [**PermissionsMap**](PermissionsMap.md) |  | [optional] 
**owner_id** | **str, none_type** |  | [optional] 
**online_member_count** | **int, none_type** | Note: May be 0 on endpoints returning lists of Networks | [optional] [readonly] 
**authorized_member_count** | **int, none_type** |  | [optional] [readonly] 
**total_member_count** | **int, none_type** |  | [optional] [readonly] 
**capabilities_by_name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**tags_by_name** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


