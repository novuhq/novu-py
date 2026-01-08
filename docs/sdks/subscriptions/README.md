# Topics.Subscriptions

## Overview

### Available Operations

* [list](#list) - List topic subscriptions
* [create](#create) - Create topic subscriptions
* [delete](#delete) - Delete topic subscriptions
* [get_subscription](#get_subscription) - Get a topic subscription
* [update](#update) - Update a topic subscription

## list

List all subscriptions of subscribers for a topic.
    Checkout all available filters in the query section.

### Example Usage

<!-- UsageSnippet language="python" operationID="TopicsController_listTopicSubscriptions" method="get" path="/v2/topics/{topicKey}/subscriptions" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.topics.subscriptions.list(request={
        "topic_key": "<value>",
        "limit": 10,
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

<!-- UsageSnippet language="python" operationID="TopicsController_createTopicSubscriptions" method="post" path="/v2/topics/{topicKey}/subscriptions" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.topics.subscriptions.create(topic_key="<value>", create_topic_subscriptions_request_dto={
        "subscriptions": [
            {
                "identifier": "subscriber-123-subscription-a",
                "subscriber_id": "subscriber-123",
            },
            {
                "identifier": "subscriber-456-subscription-b",
                "subscriber_id": "subscriber-456",
            },
        ],
        "name": "My Topic",
        "preferences": [
            {
                "condition": {
                    "===": [
                        {
                            "var": "tier",
                        },
                        "premium",
                    ],
                },
                "workflow_id": "workflow-123",
            },
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

<!-- UsageSnippet language="python" operationID="TopicsController_deleteTopicSubscriptions" method="delete" path="/v2/topics/{topicKey}/subscriptions" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.topics.subscriptions.delete(topic_key="<value>", delete_topic_subscriptions_request_dto={
        "subscriptions": [
            {
                "identifier": "subscriber-123-subscription-a",
                "subscriber_id": "subscriber-123",
            },
            {
                "subscriber_id": "subscriber-456",
            },
            {
                "identifier": "subscriber-789-subscription-b",
            },
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

## get_subscription

Get a subscription by its unique identifier for a topic.

### Example Usage

<!-- UsageSnippet language="python" operationID="TopicsController_getTopicSubscription" method="get" path="/v2/topics/{topicKey}/subscriptions/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.topics.subscriptions.get_subscription(topic_key="<value>", identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `topic_key`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The key identifier of the topic                                     |
| `identifier`                                                        | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the subscription                           |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TopicsControllerGetTopicSubscriptionResponse](../../models/topicscontrollergettopicsubscriptionresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Update a subscription by its unique identifier for a topic. You can update the preferences and name associated with the subscription.

### Example Usage

<!-- UsageSnippet language="python" operationID="TopicsController_updateTopicSubscription" method="patch" path="/v2/topics/{topicKey}/subscriptions/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.topics.subscriptions.update(topic_key="<value>", identifier="<value>", update_topic_subscription_request_dto={
        "name": "My Subscription",
        "preferences": [
            {
                "condition": {
                    "===": [
                        {
                            "var": "tier",
                        },
                        "premium",
                    ],
                },
                "workflow_id": "workflow-123",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `topic_key`                                                                                   | *str*                                                                                         | :heavy_check_mark:                                                                            | The key identifier of the topic                                                               |
| `identifier`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | The unique identifier of the subscription                                                     |
| `update_topic_subscription_request_dto`                                                       | [models.UpdateTopicSubscriptionRequestDto](../../models/updatetopicsubscriptionrequestdto.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `idempotency_key`                                                                             | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | A header for idempotency purposes                                                             |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.TopicsControllerUpdateTopicSubscriptionResponse](../../models/topicscontrollerupdatetopicsubscriptionresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |