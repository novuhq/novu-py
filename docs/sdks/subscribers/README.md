# Subscribers
(*subscribers*)

## Overview

A subscriber in Novu represents someone who should receive a message. A subscriber’s profile information contains important attributes about the subscriber that will be used in messages (name, email). The subscriber object can contain other key-value pairs that can be used to further personalize your messages.
<https://docs.novu.co/subscribers/subscribers>

### Available Operations

* [list](#list) - Get subscribers
* [create](#create) - Create subscriber
* [retrieve_legacy](#retrieve_legacy) - Get subscriber
* [update](#update) - Update subscriber
* [~~delete_legacy~~](#delete_legacy) - Delete subscriber :warning: **Deprecated**
* [create_bulk](#create_bulk) - Bulk create subscribers
* [search](#search) - Search for subscribers
* [retrieve](#retrieve) - Get subscriber
* [patch](#patch) - Patch subscriber
* [delete](#delete) - Delete subscriber

## list

Returns a list of subscribers, could paginated using the `page` and `limit` query parameter

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.list()

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersV1ControllerListSubscribersResponse](../../models/subscribersv1controllerlistsubscribersresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create

Creates a subscriber entity, in the Novu platform. The subscriber will be later used to receive notifications, and access notification feeds. Communication credentials such as email, phone number, and 3 rd party credentials i.e slack tokens could be later associated to this entity.

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.create(create_subscriber_request_dto={
        "subscriber_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `create_subscriber_request_dto`                                                 | [models.CreateSubscriberRequestDto](../../models/createsubscriberrequestdto.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `idempotency_key`                                                               | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | A header for idempotency purposes                                               |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.SubscribersV1ControllerCreateSubscriberResponse](../../models/subscribersv1controllercreatesubscriberresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve_legacy

Get subscriber by your internal id used to identify the subscriber

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.retrieve_legacy(subscriber_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `include_topics`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Includes the topics associated with the subscriber                  |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersV1ControllerGetSubscriberResponse](../../models/subscribersv1controllergetsubscriberresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Used to update the subscriber entity with new information

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.update(subscriber_id="<id>", update_subscriber_request_dto={
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

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `subscriber_id`                                                                 | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `update_subscriber_request_dto`                                                 | [models.UpdateSubscriberRequestDto](../../models/updatesubscriberrequestdto.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `idempotency_key`                                                               | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | A header for idempotency purposes                                               |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.SubscribersV1ControllerUpdateSubscriberResponse](../../models/subscribersv1controllerupdatesubscriberresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## ~~delete_legacy~~

Deletes a subscriber entity from the Novu platform

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.delete_legacy(subscriber_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersV1ControllerRemoveSubscriberResponse](../../models/subscribersv1controllerremovesubscriberresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create_bulk


      Using this endpoint you can create multiple subscribers at once, to avoid multiple calls to the API.
      The bulk API is limited to 500 subscribers per request.
    

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.create_bulk(bulk_subscriber_create_dto={
        "subscribers": [
            {
                "subscriber_id": "<id>",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `bulk_subscriber_create_dto`                                              | [models.BulkSubscriberCreateDto](../../models/bulksubscribercreatedto.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `idempotency_key`                                                         | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | A header for idempotency purposes                                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.SubscribersV1ControllerBulkCreateSubscribersResponse](../../models/subscribersv1controllerbulkcreatesubscribersresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## search

Search for subscribers

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.search()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                             | [models.SubscribersControllerSearchSubscribersRequest](../../models/subscriberscontrollersearchsubscribersrequest.md) | :heavy_check_mark:                                                                                                    | The request object to use for the request.                                                                            |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.SubscribersControllerSearchSubscribersResponse](../../models/subscriberscontrollersearchsubscribersresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Get subscriber by your internal id used to identify the subscriber

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.retrieve(subscriber_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerGetSubscriberResponse](../../models/subscriberscontrollergetsubscriberresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## patch

Patch subscriber by your internal id used to identify the subscriber

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.patch(subscriber_id="<id>", patch_subscriber_request_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `subscriber_id`                                                               | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `patch_subscriber_request_dto`                                                | [models.PatchSubscriberRequestDto](../../models/patchsubscriberrequestdto.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `idempotency_key`                                                             | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A header for idempotency purposes                                             |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.SubscribersControllerPatchSubscriberResponse](../../models/subscriberscontrollerpatchsubscriberresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Deletes a subscriber entity from the Novu platform

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    secret_key=os.getenv("NOVU_SECRET_KEY", ""),
) as novu:

    res = novu.subscribers.delete(subscriber_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `subscriber_id`                                                     | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SubscribersControllerRemoveSubscriberResponse](../../models/subscriberscontrollerremovesubscriberresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |