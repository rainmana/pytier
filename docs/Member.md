# Member


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | concatenation of network ID and member ID | [optional] [readonly] 
**clock** | **int, none_type** |  | [optional] [readonly] 
**network_id** | **str, none_type** |  | [optional] [readonly] 
**node_id** | **str, none_type** | ZeroTier ID of the member | [optional] [readonly] 
**controller_id** | **str, none_type** |  | [optional] [readonly] 
**hidden** | **bool, none_type** | Whether or not the member is hidden in the UI | [optional] 
**name** | **str, none_type** | User defined name of the member | [optional] 
**description** | **str, none_type** | User defined description of the member | [optional] 
**config** | [**MemberConfig**](MemberConfig.md) |  | [optional] 
**last_online** | **int, none_type** | Last seen time of the member.  Note: This data is considered ephemeral and may be reset to 0 at any time without warning. | [optional] [readonly] 
**physical_address** | **str, none_type** | IP address the member last spoke to the controller via.  Note: This data is considered ephemeral and may be reset to 0 at any time without warning. | [optional] [readonly] 
**client_version** | **str, none_type** | ZeroTier version the member is running | [optional] [readonly] 
**protocol_version** | **int, none_type** | ZeroTier protocol version | [optional] [readonly] 
**supports_rules_engine** | **bool, none_type** | Whether or not the client version is new enough to support the rules engine (1.4.0+) | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


