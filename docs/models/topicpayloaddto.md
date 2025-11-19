# TopicPayloadDto


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `topic_key`                                                                | *str*                                                                      | :heavy_check_mark:                                                         | N/A                                                                        |
| `type`                                                                     | [models.TriggerRecipientsTypeEnum](../models/triggerrecipientstypeenum.md) | :heavy_check_mark:                                                         | N/A                                                                        |
| `exclude`                                                                  | List[*str*]                                                                | :heavy_minus_sign:                                                         | Optional array of subscriber IDs to exclude from the topic trigger         |