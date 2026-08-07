# EditPayloadDto


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `message_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | Platform message id of the message to edit.                              | 1712345678.123456                                                        |
| `content`                                                                | [models.Content](../models/content.md)                                   | :heavy_check_mark:                                                       | Replacement content. Exactly one of markdown, card, or toolApprovalCard. |                                                                          |