# NovuNotifications
(*subscribers.notifications*)

## Overview

### Available Operations

* [feed](#feed) - Get in-app notification feed for a particular subscriber
* [unseen_count](#unseen_count) - Get the unseen in-app notifications count for subscribers feed

## feed

Get in-app notification feed for a particular subscriber

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.notifications.feed(request={
    "subscriber_id": "<id>",
    "payload": "btoa(JSON.stringify({ foo: 123 })) results in base64 encoded string like eyJmb28iOjEyM30=",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                   | [models.SubscribersControllerGetNotificationsFeedRequest](../../models/subscriberscontrollergetnotificationsfeedrequest.md) | :heavy_check_mark:                                                                                                          | The request object to use for the request.                                                                                  |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.SubscribersControllerGetNotificationsFeedResponse](../../models/subscriberscontrollergetnotificationsfeedresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## unseen_count

Get the unseen in-app notifications count for subscribers feed

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.notifications.unseen_count(subscriber_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `seen`                                                              | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Indicates whether to count seen notifications.                      |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | The maximum number of notifications to return.                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerGetUnseenCountResponse](../../models/subscriberscontrollergetunseencountresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |