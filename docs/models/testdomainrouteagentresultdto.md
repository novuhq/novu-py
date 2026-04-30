# TestDomainRouteAgentResultDto


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `agent_id`                                                  | *str*                                                       | :heavy_check_mark:                                          | N/A                                                         |
| `http_status`                                               | *float*                                                     | :heavy_check_mark:                                          | N/A                                                         |
| `agent_reply`                                               | [Optional[models.AgentReply]](../models/agentreply.md)      | :heavy_minus_sign:                                          | Parsed JSON body from the agent webhook response when JSON. |
| `latency_ms`                                                | *float*                                                     | :heavy_check_mark:                                          | N/A                                                         |