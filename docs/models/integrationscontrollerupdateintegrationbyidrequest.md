# IntegrationsControllerUpdateIntegrationByIDRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `integration_id`                                                               | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `update_integration_request_dto`                                               | [models.UpdateIntegrationRequestDto](../models/updateintegrationrequestdto.md) | :heavy_check_mark:                                                             | N/A                                                                            |
| `idempotency_key`                                                              | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | A header for idempotency purposes                                              |