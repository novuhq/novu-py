# AgentsControllerUpdateAgentRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `identifier`                                                       | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `idempotency_key`                                                  | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | A header for idempotency purposes                                  |
| `update_agent_request_dto`                                         | [models.UpdateAgentRequestDto](../models/updateagentrequestdto.md) | :heavy_check_mark:                                                 | N/A                                                                |