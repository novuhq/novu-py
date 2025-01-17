# NovuMessages
(*subscribers.messages*)

## Overview

### Available Operations

* [mark_all_as](#mark_all_as) - Mark a subscriber messages as seen, read, unseen or unread
* [mark_all](#mark_all) - Marks all the subscriber messages as read, unread, seen or unseen. Optionally you can pass feed id (or array) to mark messages of a particular feed.
* [update_as_seen](#update_as_seen) - Mark message action as seen

## mark_all_as

Mark a subscriber messages as seen, read, unseen or unread

### Example Usage

```python
import novu_py
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.messages.mark_all_as(subscriber_id="<id>", message_mark_as_request_dto={
    "message_id": "<value>",
    "mark_as": novu_py.MarkAs.UNREAD,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `subscriber_id`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `message_mark_as_request_dto`                                             | [models.MessageMarkAsRequestDto](../../models/messagemarkasrequestdto.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.SubscribersControllerMarkMessagesAsResponse](../../models/subscriberscontrollermarkmessagesasresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## mark_all

Marks all the subscriber messages as read, unread, seen or unseen. Optionally you can pass feed id (or array) to mark messages of a particular feed.

### Example Usage

```python
import novu_py
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.messages.mark_all(subscriber_id="<id>", mark_all_message_as_request_dto={
    "mark_as": novu_py.MarkAllMessageAsRequestDtoMarkAs.SEEN,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `subscriber_id`                                                                 | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `mark_all_message_as_request_dto`                                               | [models.MarkAllMessageAsRequestDto](../../models/markallmessageasrequestdto.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.SubscribersControllerMarkAllUnreadAsReadResponse](../../models/subscriberscontrollermarkallunreadasreadresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## update_as_seen

Mark message action as seen

### Example Usage

```python
import novu_py
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.messages.update_as_seen(message_id="<id>", type_="<value>", subscriber_id="<id>", mark_message_action_as_seen_dto={
    "status": novu_py.MarkMessageActionAsSeenDtoStatus.DONE,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `message_id`                                                                    | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `type`                                                                          | *Any*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `subscriber_id`                                                                 | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `mark_message_action_as_seen_dto`                                               | [models.MarkMessageActionAsSeenDto](../../models/markmessageactionasseendto.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.SubscribersControllerMarkActionAsSeenResponse](../../models/subscriberscontrollermarkactionasseenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |