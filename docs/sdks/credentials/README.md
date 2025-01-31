# Credentials
(*subscribers.credentials*)

## Overview

### Available Operations

* [update](#update) - Update subscriber credentials
* [append](#append) - Modify subscriber credentials
* [delete](#delete) - Delete subscriber credentials by providerId

## update

Subscriber credentials associated to the delivery methods such as slack and push tokens.

### Example Usage

```python
import novu_py
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.credentials.update(subscriber_id="<id>", update_subscriber_channel_request_dto={
        "provider_id": novu_py.UpdateSubscriberChannelRequestDtoProviderID.PUSHPAD,
        "credentials": {
            "webhook_url": "https://example.com/webhook",
            "channel": "general",
            "device_tokens": [
                "token1",
                "token2",
                "token3",
            ],
            "alert_uid": "12345-abcde",
            "title": "Critical Alert",
            "image_url": "https://example.com/image.png",
            "state": "resolved",
            "external_url": "https://example.com/details",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                               | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `update_subscriber_channel_request_dto`                                                       | [models.UpdateSubscriberChannelRequestDto](../../models/updatesubscriberchannelrequestdto.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A header for idempotency purposes                                                             |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.SubscribersV1ControllerUpdateSubscriberChannelResponse](../../models/subscribersv1controllerupdatesubscriberchannelresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## append

Subscriber credentials associated to the delivery methods such as slack and push tokens.

    This endpoint appends provided credentials and deviceTokens to the existing ones.

### Example Usage

```python
import novu_py
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.credentials.append(subscriber_id="<id>", update_subscriber_channel_request_dto={
        "provider_id": novu_py.UpdateSubscriberChannelRequestDtoProviderID.ZULIP,
        "credentials": {
            "webhook_url": "https://example.com/webhook",
            "channel": "general",
            "device_tokens": [
                "token1",
                "token2",
                "token3",
            ],
            "alert_uid": "12345-abcde",
            "title": "Critical Alert",
            "image_url": "https://example.com/image.png",
            "state": "resolved",
            "external_url": "https://example.com/details",
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                               | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `update_subscriber_channel_request_dto`                                                       | [models.UpdateSubscriberChannelRequestDto](../../models/updatesubscriberchannelrequestdto.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A header for idempotency purposes                                                             |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.SubscribersV1ControllerModifySubscriberChannelResponse](../../models/subscribersv1controllermodifysubscriberchannelresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete subscriber credentials such as slack and expo tokens.

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.credentials.delete(subscriber_id="<id>", provider_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `provider_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersV1ControllerDeleteSubscriberCredentialsResponse](../../models/subscribersv1controllerdeletesubscribercredentialsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |