# ChatControlsMetadataResponseDto


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `data_schema`                                        | Dict[str, *Any*]                                     | :heavy_minus_sign:                                   | JSON Schema for data                                 |
| `ui_schema`                                          | [Optional[models.UISchema]](../models/uischema.md)   | :heavy_minus_sign:                                   | UI Schema for rendering                              |
| `values`                                             | [models.ChatControlDto](../models/chatcontroldto.md) | :heavy_check_mark:                                   | Control values specific to Chat                      |