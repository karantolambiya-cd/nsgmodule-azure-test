<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.10.0 |
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | >= 4.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | >= 4.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_labels"></a> [labels](#module\_labels) | terraform-az-modules/tags/azurerm | 1.0.2 |

## Resources

| Name | Type |
|------|------|
| [azurerm_monitor_diagnostic_setting.nsg_diagnostic](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/monitor_diagnostic_setting) | resource |
| [azurerm_network_interface_security_group_association.nsg_nic_association](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_interface_security_group_association) | resource |
| [azurerm_network_security_group.nsg](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_security_group) | resource |
| [azurerm_network_security_rule.inbound](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_security_rule) | resource |
| [azurerm_network_security_rule.outbound](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_security_rule) | resource |
| [azurerm_subnet_network_security_group_association.nsg_subnet_association](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet_network_security_group_association) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_create"></a> [create](#input\_create) | Used when creating the Resource Group. | `string` | `"30m"` | no |
| <a name="input_custom_name"></a> [custom\_name](#input\_custom\_name) | Override default naming convention | `string` | `null` | no |
| <a name="input_delete"></a> [delete](#input\_delete) | Used when deleting the Resource Group. | `string` | `"30m"` | no |
| <a name="input_deployment_mode"></a> [deployment\_mode](#input\_deployment\_mode) | Specifies how the infrastructure/resource is deployed | `string` | `"terraform"` | no |
| <a name="input_enable_diagnostic"></a> [enable\_diagnostic](#input\_enable\_diagnostic) | Set to false to prevent the module from creating the diagnosys setting for the NSG Resource.. | `bool` | `false` | no |
| <a name="input_enabled"></a> [enabled](#input\_enabled) | Set to false to prevent the module from creating any resources. | `bool` | `true` | no |
| <a name="input_environment"></a> [environment](#input\_environment) | Environment (e.g. `prod`, `dev`, `staging`). | `string` | `""` | no |
| <a name="input_eventhub_authorization_rule_id"></a> [eventhub\_authorization\_rule\_id](#input\_eventhub\_authorization\_rule\_id) | Eventhub authorization rule id to pass it to destination details of diagnosys setting of NSG. | `string` | `null` | no |
| <a name="input_eventhub_name"></a> [eventhub\_name](#input\_eventhub\_name) | Eventhub Name to pass it to destination details of diagnosys setting of NSG. | `string` | `null` | no |
| <a name="input_extra_tags"></a> [extra\_tags](#input\_extra\_tags) | Variable to pass extra tags. | `map(string)` | `null` | no |
| <a name="input_inbound_rules"></a> [inbound\_rules](#input\_inbound\_rules) | List of objects that represent the configuration of each inbound rule. | <pre>list(object({<br/>    name                         = string<br/>    priority                     = number<br/>    access                       = string<br/>    protocol                     = string<br/>    source_address_prefix        = optional(string)<br/>    source_address_prefixes      = optional(list(string))<br/>    source_port_range            = optional(string)<br/>    destination_address_prefix   = optional(string)<br/>    destination_address_prefixes = optional(list(string))<br/>    destination_port_range       = optional(string)<br/>    description                  = optional(string)<br/>  }))</pre> | `[]` | no |
| <a name="input_label_order"></a> [label\_order](#input\_label\_order) | The order of labels used to construct resource names or tags. If not specified, defaults to ['name', 'environment', 'location']. | `list(any)` | <pre>[<br/>  "name",<br/>  "environment",<br/>  "location"<br/>]</pre> | no |
| <a name="input_location"></a> [location](#input\_location) | The location/region where the virtual network is created. Changing this forces a new resource to be created. | `string` | `""` | no |
| <a name="input_log_analytics_destination_type"></a> [log\_analytics\_destination\_type](#input\_log\_analytics\_destination\_type) | Possible values are AzureDiagnostics and Dedicated, default to AzureDiagnostics. When set to Dedicated, logs sent to a Log Analytics workspace will go into resource specific tables, instead of the legacy AzureDiagnostics table. | `string` | `"AzureDiagnostics"` | no |
| <a name="input_log_analytics_workspace_id"></a> [log\_analytics\_workspace\_id](#input\_log\_analytics\_workspace\_id) | log analytics workspace id to pass it to destination details of diagnosys setting of NSG. | `string` | `null` | no |
| <a name="input_logs"></a> [logs](#input\_logs) | List of log categories. Defaults to all available. | `list(map(string))` | `[]` | no |
| <a name="input_managedby"></a> [managedby](#input\_managedby) | ManagedBy, eg 'terraform-az-modules'. | `string` | `"terraform-az-modules"` | no |
| <a name="input_name"></a> [name](#input\_name) | Name  (e.g. `app` or `cluster`). | `string` | `""` | no |
| <a name="input_nic_association"></a> [nic\_association](#input\_nic\_association) | If true, the Network Security Group will be associated with the network interfaces specified in `nic_ids`. | `bool` | `false` | no |
| <a name="input_nic_ids"></a> [nic\_ids](#input\_nic\_ids) | A list of Network Interface IDs to associate with the Network Security Group. | `list(string)` | `[]` | no |
| <a name="input_outbound_rules"></a> [outbound\_rules](#input\_outbound\_rules) | List of objects that represent the configuration of each outbound rule. | <pre>list(object({<br/>    name                         = string<br/>    priority                     = number<br/>    access                       = string<br/>    protocol                     = string<br/>    source_address_prefix        = optional(string)<br/>    source_address_prefixes      = optional(list(string))<br/>    source_port_range            = optional(string)<br/>    destination_address_prefix   = optional(string)<br/>    destination_address_prefixes = optional(list(string))<br/>    destination_port_range       = optional(string)<br/>    description                  = optional(string)<br/>  }))</pre> | `[]` | no |
| <a name="input_read"></a> [read](#input\_read) | Used when retrieving the Resource Group. | `string` | `"5m"` | no |
| <a name="input_repository"></a> [repository](#input\_repository) | Terraform current module repo | `string` | `"https://github.com/terraform-az-modules/terraform-azure-nsg"` | no |
| <a name="input_resource_group_name"></a> [resource\_group\_name](#input\_resource\_group\_name) | The name of the resource group in which to create the network security group. | `string` | n/a | yes |
| <a name="input_resource_position_prefix"></a> [resource\_position\_prefix](#input\_resource\_position\_prefix) | Controls the placement of the resource type keyword (e.g., "vnet", "ddospp") in the resource name.<br/><br/>- If true, the keyword is prepended: "vnet-core-dev".<br/>- If false, the keyword is appended: "core-dev-vnet".<br/><br/>This helps maintain naming consistency based on organizational preferences. | `bool` | `true` | no |
| <a name="input_storage_account_id"></a> [storage\_account\_id](#input\_storage\_account\_id) | Storage ID for Log Analytics | `string` | `null` | no |
| <a name="input_subnet_association"></a> [subnet\_association](#input\_subnet\_association) | If true, the Network Security Group will be associated with the subnets specified in `subnet_ids`. | `bool` | `true` | no |
| <a name="input_subnet_ids"></a> [subnet\_ids](#input\_subnet\_ids) | A list of Subnet IDs to associate with the Network Security Group. | `list(string)` | `[]` | no |
| <a name="input_update"></a> [update](#input\_update) | Used when updating the Resource Group. | `string` | `"30m"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_id"></a> [id](#output\_id) | The network security group configuration ID. |
| <a name="output_name"></a> [name](#output\_name) | The name of the network security group. |
| <a name="output_network_security_group_id"></a> [network\_security\_group\_id](#output\_network\_security\_group\_id) | The ID of network security group |
| <a name="output_tags"></a> [tags](#output\_tags) | The tags assigned to the resource. |
<!-- END_TF_DOCS -->