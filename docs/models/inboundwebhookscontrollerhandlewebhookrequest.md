# InboundWebhooksControllerHandleWebhookRequest


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `environment_id`                                     | *str*                                                | :heavy_check_mark:                                   | The environment identifier                           |
| `integration_id`                                     | *str*                                                | :heavy_check_mark:                                   | The integration identifier for the delivery provider |
| `idempotency_key`                                    | *Optional[str]*                                      | :heavy_minus_sign:                                   | A header for idempotency purposes                    |
| `request_body`                                       | Dict[str, *Any*]                                     | :heavy_check_mark:                                   | Webhook event payload from the delivery provider     |