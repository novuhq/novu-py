# Subscribers.Notifications

## Overview

### Available Operations

* [feed](#feed) - Retrieve subscriber notifications
* [unseen_count](#unseen_count) - Retrieve unseen notifications count

## feed

Retrieve subscriber in-app (inbox) notifications by its unique key identifier **subscriberId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersV1Controller_getNotificationsFeed" method="get" path="/v1/subscribers/{subscriberId}/notifications/feed" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.feed(request={
        "subscriber_id": "<id>",
        "page": 0,
        "payload": "btoa(JSON.stringify({ foo: 123 })) results in base64 encoded string like eyJmb28iOjEyM30=",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                       | [models.SubscribersV1ControllerGetNotificationsFeedRequest](../../models/subscribersv1controllergetnotificationsfeedrequest.md) | :heavy_check_mark:                                                                                                              | The request object to use for the request.                                                                                      |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.SubscribersV1ControllerGetNotificationsFeedResponse](../../models/subscribersv1controllergetnotificationsfeedresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## unseen_count

Retrieve unseen in-app (inbox) notifications count for a subscriber by its unique key identifier **subscriberId**.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersV1Controller_getUnseenCount" method="get" path="/v1/subscribers/{subscriberId}/notifications/unseen" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.notifications.unseen_count(subscriber_id="<id>", seen=False, limit=100)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `seen`                                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Indicates whether to count seen notifications.                      |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | The maximum number of notifications to return.                      |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersV1ControllerGetUnseenCountResponse](../../models/subscribersv1controllergetunseencountresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |