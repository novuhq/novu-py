# EnvironmentsControllerV1UpdateMyEnvironmentRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `environment_id`                                                               | *str*                                                                          | :heavy_check_mark:                                                             | The unique identifier of the environment                                       |
| `idempotency_key`                                                              | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | A header for idempotency purposes                                              |
| `update_environment_request_dto`                                               | [models.UpdateEnvironmentRequestDto](../models/updateenvironmentrequestdto.md) | :heavy_check_mark:                                                             | N/A                                                                            |