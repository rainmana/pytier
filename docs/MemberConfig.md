# MemberConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_bridge** | **bool, none_type** | Allow the member to be a bridge on the network | [optional] 
**authorized** | **bool, none_type** | Is the member authorized on the network | [optional] 
**capabilities** | **[int], none_type** |  | [optional] 
**creation_time** | **int, none_type** | Time the member was created or first tried to join the network | [optional] [readonly] 
**id** | **str, none_type** | ID of the member node.  This is the 10 digit identifier that identifies a ZeroTier node. | [optional] [readonly] 
**identity** | **str, none_type** | Public Key of the member&#39;s Identity | [optional] [readonly] 
**ip_assignments** | **[str], none_type** | List of assigned IP addresses | [optional] 
**last_authorized_time** | **int, none_type** | Time the member was authorized on the network | [optional] [readonly] 
**last_deauthorized_time** | **int, none_type** | Time the member was deauthorized on the network | [optional] [readonly] 
**no_auto_assign_ips** | **bool, none_type** | Exempt this member from the IP auto assignment pool on a Network | [optional] 
**revision** | **int, none_type** | Member record revision count | [optional] [readonly] 
**tags** | [**[[MemberConfigTagsInnerInner]], none_type**](MemberConfigTagsInnerInner.md) | Array of 2 member tuples of tag [ID, tag value] | [optional] 
**v_major** | **int, none_type** | Major version of the client | [optional] [readonly] 
**v_minor** | **int, none_type** | Minor version of the client | [optional] [readonly] 
**v_rev** | **int, none_type** | Revision number of the client | [optional] [readonly] 
**v_proto** | **int, none_type** | Protocol version of the client | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


