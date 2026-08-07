# UpdateAgentBridgeRequestDto


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `bridge_url`                                 | *Optional[str]*                              | :heavy_minus_sign:                           | Production bridge URL for this agent         |
| `dev_bridge_url`                             | *Optional[str]*                              | :heavy_minus_sign:                           | Development bridge URL (set by npx novu dev) |
| `dev_bridge_active`                          | *Optional[bool]*                             | :heavy_minus_sign:                           | Whether the dev bridge override is active    |