# NovuSubscribers
(*topics.subscribers*)

## Overview

### Available Operations

* [assign](#assign) - Subscribers addition
* [retrieve](#retrieve) - Check topic subscriber
* [remove](#remove) - Subscribers removal

## assign

Add subscribers to a topic by key

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.topics.subscribers.assign(topic_key="<value>", add_subscribers_request_dto={
        "subscribers": [
            "<value>",
            "<value>",
            "<value>",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `topic_key`                                                                 | *str*                                                                       | :heavy_check_mark:                                                          | The topic key                                                               |
| `add_subscribers_request_dto`                                               | [models.AddSubscribersRequestDto](../../models/addsubscribersrequestdto.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `idempotency_key`                                                           | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | A header for idempotency purposes                                           |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.TopicsControllerAssignResponse](../../models/topicscontrollerassignresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Check if a subscriber belongs to a certain topic

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.topics.subscribers.retrieve(external_subscriber_id="<id>", topic_key="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `external_subscriber_id`                                            | *str*                                                               | :heavy_check_mark:                                                  | The external subscriber id                                          |
| `topic_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The topic key                                                       |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TopicsControllerGetTopicSubscriberResponse](../../models/topicscontrollergettopicsubscriberresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## remove

Remove subscribers from a topic

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.topics.subscribers.remove(topic_key="<value>", remove_subscribers_request_dto={
        "subscribers": [
            "<value>",
            "<value>",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `topic_key`                                                                       | *str*                                                                             | :heavy_check_mark:                                                                | The topic key                                                                     |
| `remove_subscribers_request_dto`                                                  | [models.RemoveSubscribersRequestDto](../../models/removesubscribersrequestdto.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `idempotency_key`                                                                 | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | A header for idempotency purposes                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.TopicsControllerRemoveSubscribersResponse](../../models/topicscontrollerremovesubscribersresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |