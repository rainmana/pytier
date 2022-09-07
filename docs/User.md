# User


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID | [optional] [readonly] 
**org_id** | **str** | Organization ID | [optional] [readonly] 
**global_permissions** | [**UserGlobalPermissions**](UserGlobalPermissions.md) |  | [optional] 
**display_name** | **str** | Display Name | [optional] 
**email** | **str** | User email address | [optional] [readonly] 
**auth** | [**UserAuth**](UserAuth.md) |  | [optional] 
**sms_number** | **str** | SMS number | [optional] 
**tokens** | **[str]** | List of API token names. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


