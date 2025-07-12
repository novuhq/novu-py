# PatchWorkflowDto


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `active`                                         | *Optional[bool]*                                 | :heavy_minus_sign:                               | Activate or deactivate the workflow              |
| `name`                                           | *Optional[str]*                                  | :heavy_minus_sign:                               | New name for the workflow                        |
| `description`                                    | *Optional[str]*                                  | :heavy_minus_sign:                               | Updated description of the workflow              |
| `tags`                                           | List[*str*]                                      | :heavy_minus_sign:                               | Tags associated with the workflow                |
| `payload_schema`                                 | Dict[str, *Any*]                                 | :heavy_minus_sign:                               | The payload JSON Schema for the workflow         |
| `validate_payload`                               | *Optional[bool]*                                 | :heavy_minus_sign:                               | Enable or disable payload schema validation      |
| `is_translation_enabled`                         | *Optional[bool]*                                 | :heavy_minus_sign:                               | Enable or disable translations for this workflow |