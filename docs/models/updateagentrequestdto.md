# UpdateAgentRequestDto


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `name`                                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `description`                                                      | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | N/A                                                                |
| `active`                                                           | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | N/A                                                                |
| `behavior`                                                         | [Optional[models.AgentBehaviorDto]](../models/agentbehaviordto.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `bridge_url`                                                       | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Production bridge URL for this agent                               |
| `dev_bridge_url`                                                   | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Development bridge URL (set by npx novu dev)                       |
| `dev_bridge_active`                                                | *Optional[bool]*                                                   | :heavy_minus_sign:                                                 | Whether the dev bridge override is active                          |