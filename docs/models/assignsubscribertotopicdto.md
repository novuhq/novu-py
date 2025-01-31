# AssignSubscriberToTopicDto


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `succeeded`                                                                | List[*str*]                                                                | :heavy_check_mark:                                                         | List of successfully assigned subscriber IDs                               |
| `failed`                                                                   | [Optional[models.FailedAssignmentsDto]](../models/failedassignmentsdto.md) | :heavy_minus_sign:                                                         | Details about failed assignments                                           |