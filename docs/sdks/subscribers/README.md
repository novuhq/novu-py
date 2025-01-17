# Subscribers
(*subscribers*)

## Overview

A subscriber in Novu represents someone who should receive a message. A subscriber’s profile information contains important attributes about the subscriber that will be used in messages (name, email). The subscriber object can contain other key-value pairs that can be used to further personalize your messages.
<https://docs.novu.co/subscribers/subscribers>

### Available Operations

* [list](#list) - Get subscribers
* [create](#create) - Create subscriber
* [retrieve](#retrieve) - Get subscriber
* [update](#update) - Update subscriber
* [delete](#delete) - Delete subscriber
* [create_bulk](#create_bulk) - Bulk create subscribers

## list

Returns a list of subscribers, could paginated using the `page` and `limit` query parameter

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.list()

if res is not None:
    while True:
        # handle items

        res = res.next()
        if res is None:
            break

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerListSubscribersResponse](../../models/subscriberscontrollerlistsubscribersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## create

Creates a subscriber entity, in the Novu platform. The subscriber will be later used to receive notifications, and access notification feeds. Communication credentials such as email, phone number, and 3 rd party credentials i.e slack tokens could be later associated to this entity.

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.create(request={
    "subscriber_id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.CreateSubscriberRequestDto](../../models/createsubscriberrequestdto.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.SubscribersControllerCreateSubscriberResponse](../../models/subscriberscontrollercreatesubscriberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## retrieve

Get subscriber by your internal id used to identify the subscriber

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.retrieve(subscriber_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `include_topics`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Includes the topics associated with the subscriber                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerGetSubscriberResponse](../../models/subscriberscontrollergetsubscriberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## update

Used to update the subscriber entity with new information

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.update(subscriber_id="<id>", update_subscriber_request_dto={
    "email": "john.doe@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "+1234567890",
    "avatar": "https://example.com/avatar.jpg",
    "locale": "en-US",
    "data": {
        "preferences": {
            "notifications": True,
            "theme": "dark",
        },
        "tags": [
            "premium",
            "newsletter",
        ],
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `subscriber_id`                                                                 | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `update_subscriber_request_dto`                                                 | [models.UpdateSubscriberRequestDto](../../models/updatesubscriberrequestdto.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.SubscribersControllerUpdateSubscriberResponse](../../models/subscriberscontrollerupdatesubscriberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## delete

Deletes a subscriber entity from the Novu platform

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.delete(subscriber_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerRemoveSubscriberResponse](../../models/subscriberscontrollerremovesubscriberresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## create_bulk


      Using this endpoint you can create multiple subscribers at once, to avoid multiple calls to the API.
      The bulk API is limited to 500 subscribers per request.
    

### Example Usage

```python
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.subscribers.create_bulk(request={
    "subscribers": [
        {
            "subscriber_id": "<id>",
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.BulkSubscriberCreateDto](../../models/bulksubscribercreatedto.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.SubscribersControllerBulkCreateSubscribersResponse](../../models/subscriberscontrollerbulkcreatesubscribersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.ErrorDto           | 400, 404, 409             | application/json          |
| models.ValidationErrorDto | 422                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |