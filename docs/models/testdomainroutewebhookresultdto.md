# TestDomainRouteWebhookResultDto


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `skipped`                                                                            | *Optional[bool]*                                                                     | :heavy_minus_sign:                                                                   | True when outbound webhooks are disabled for this environment (nothing was emitted). |
| `latency_ms`                                                                         | *float*                                                                              | :heavy_check_mark:                                                                   | N/A                                                                                  |