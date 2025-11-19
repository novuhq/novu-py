# Activity
(*activity*)

## Overview

### Available Operations

* [track](#track) - Track activity and engagement events

## track

Track activity and engagement events for a specific delivery provider

### Example Usage

<!-- UsageSnippet language="python" operationID="InboundWebhooksController_handleWebhook" method="post" path="/v2/inbound-webhooks/delivery-providers/{environmentId}/{integrationId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.activity.track(environment_id="<id>", integration_id="<id>", request_body="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `environment_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The environment identifier                                          |
| `integration_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | The integration identifier for the delivery provider                |
| `request_body`                                                      | *Any*                                                               | :heavy_check_mark:                                                  | Webhook event payload from the delivery provider                    |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.WebhookResultDto]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |