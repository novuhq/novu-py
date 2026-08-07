# AgentsControllerCreateAgentRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `novu_analytics_source`                                            | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `idempotency_key`                                                  | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | A header for idempotency purposes                                  |
| `create_agent_request_dto`                                         | [models.CreateAgentRequestDto](../models/createagentrequestdto.md) | :heavy_check_mark:                                                 | N/A                                                                |