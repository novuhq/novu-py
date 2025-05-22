# Subscriptions
(*topics.subscriptions*)

## Overview

### Available Operations

* [list](#list) - List topic subscriptions
* [create](#create) - Create topic subscriptions
* [delete](#delete) - Delete topic subscriptions

## list

List all topics that a subscriber is subscribed to.
    Checkout all available filters in the query section.

### Example Usage

```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.topics.subscriptions.list(request={
        "topic_key": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.TopicsControllerListTopicSubscriptionsRequest](../../models/topicscontrollerlisttopicsubscriptionsrequest.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.TopicsControllerListTopicSubscriptionsResponse](../../models/topicscontrollerlisttopicsubscriptionsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create

This api will create subscription for subscriberIds for a topic. 
      Its like subscribing to a common interest group. if topic does not exist, it will be created.

### Example Usage

```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.topics.subscriptions.create(topic_key="<value>", create_topic_subscriptions_request_dto={
        "subscriber_ids": [
            "subscriberId1",
            "subscriberId2",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `topic_key`                                                                                     | *str*                                                                                           | :heavy_check_mark:                                                                              | The key identifier of the topic                                                                 |
| `create_topic_subscriptions_request_dto`                                                        | [models.CreateTopicSubscriptionsRequestDto](../../models/createtopicsubscriptionsrequestdto.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `idempotency_key`                                                                               | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | A header for idempotency purposes                                                               |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.TopicsControllerCreateTopicSubscriptionsResponse](../../models/topicscontrollercreatetopicsubscriptionsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Delete subscriptions for subscriberIds for a topic.

### Example Usage

```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.topics.subscriptions.delete(topic_key="<value>", delete_topic_subscriptions_request_dto={
        "subscriber_ids": [
            "subscriberId1",
            "subscriberId2",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `topic_key`                                                                                     | *str*                                                                                           | :heavy_check_mark:                                                                              | The key identifier of the topic                                                                 |
| `delete_topic_subscriptions_request_dto`                                                        | [models.DeleteTopicSubscriptionsRequestDto](../../models/deletetopicsubscriptionsrequestdto.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `idempotency_key`                                                                               | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | A header for idempotency purposes                                                               |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.TopicsControllerDeleteTopicSubscriptionsResponse](../../models/topicscontrollerdeletetopicsubscriptionsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |