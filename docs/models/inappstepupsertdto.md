# InAppStepUpsertDto


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Unique identifier of the step                                        |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Name of the step                                                     |
| `type`                                                               | [models.StepTypeEnum](../models/steptypeenum.md)                     | :heavy_check_mark:                                                   | Type of the step                                                     |
| `control_values`                                                     | [OptionalNullable[models.ControlValues]](../models/controlvalues.md) | :heavy_minus_sign:                                                   | Control values for the In-App step                                   |