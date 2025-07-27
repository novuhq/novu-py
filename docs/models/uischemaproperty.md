# UISchemaProperty


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `placeholder`                                                       | [OptionalNullable[models.Placeholder]](../models/placeholder.md)    | :heavy_minus_sign:                                                  | Placeholder for the UI Schema Property                              |
| `component`                                                         | [models.UIComponentEnum](../models/uicomponentenum.md)              | :heavy_check_mark:                                                  | Component type for the UI Schema Property                           |
| `properties`                                                        | Dict[str, [models.UISchemaProperty](../models/uischemaproperty.md)] | :heavy_minus_sign:                                                  | Properties of the UI Schema                                         |