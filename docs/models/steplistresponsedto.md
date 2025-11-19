# StepListResponseDto


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `slug`                                                       | *str*                                                        | :heavy_check_mark:                                           | Slug of the step                                             |
| `type`                                                       | [models.StepTypeEnum](../models/steptypeenum.md)             | :heavy_check_mark:                                           | Type of the step                                             |
| `issues`                                                     | [Optional[models.StepIssuesDto]](../models/stepissuesdto.md) | :heavy_minus_sign:                                           | Issues associated with the step                              |