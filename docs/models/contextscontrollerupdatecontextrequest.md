# ContextsControllerUpdateContextRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Context ID                                                             |
| `type`                                                                 | *str*                                                                  | :heavy_check_mark:                                                     | Context type                                                           |
| `idempotency_key`                                                      | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | A header for idempotency purposes                                      |
| `update_context_request_dto`                                           | [models.UpdateContextRequestDto](../models/updatecontextrequestdto.md) | :heavy_check_mark:                                                     | N/A                                                                    |