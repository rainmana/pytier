# NetworkConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Network ID | [optional] [readonly] 
**creation_time** | **int, none_type** | Time the network was created | [optional] [readonly] 
**capabilities** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type** | Array of network capabilities | [optional] 
**dns** | **DNS** |  | [optional] 
**enable_broadcast** | **bool, none_type** | Enable broadcast packets on the network | [optional] 
**ip_assignment_pools** | [**[IPRange], none_type**](IPRange.md) | Range of IP addresses for the auto assign pool | [optional] 
**last_modified** | **int, none_type** | Time the network was last modified | [optional] [readonly] 
**mtu** | **int, none_type** | MTU to set on the client virtual network adapter | [optional] 
**multicast_limit** | **int, none_type** | Maximum number of recipients per multicast or broadcast. Warning - Setting this to 0 will disable IPv4 communication on your network! | [optional] 
**name** | **str, none_type** |  | [optional] 
**private** | **bool, none_type** | Whether or not the network is private.  If false, members will *NOT* need to be authorized to join. | [optional] 
**routes** | [**[Route], none_type**](Route.md) |  | [optional] 
**rules** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type** |  | [optional] 
**tags** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type** |  | [optional] 
**v4_assign_mode** | [**IPV4AssignMode**](IPV4AssignMode.md) |  | [optional] 
**v6_assign_mode** | [**IPV6AssignMode**](IPV6AssignMode.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


