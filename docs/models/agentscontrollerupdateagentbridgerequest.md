# AgentsControllerUpdateAgentBridgeRequest


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `identifier`                                                                   | *str*                                                                          | :heavy_check_mark:                                                             | N/A                                                                            |
| `idempotency_key`                                                              | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | A header for idempotency purposes                                              |
| `update_agent_bridge_request_dto`                                              | [models.UpdateAgentBridgeRequestDto](../models/updateagentbridgerequestdto.md) | :heavy_check_mark:                                                             | N/A                                                                            |