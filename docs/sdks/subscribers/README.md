# Subscribers
(*subscribers*)

## Overview

A subscriber in Novu represents someone who should receive a message. A subscriber's profile information contains important attributes about the subscriber that will be used in messages (name, email). The subscriber object can contain other key-value pairs that can be used to further personalize your messages.
<https://docs.novu.co/subscribers/subscribers>

### Available Operations

* [search](#search) - Search subscribers
* [create](#create) - Create a subscriber
* [retrieve](#retrieve) - Retrieve a subscriber
* [patch](#patch) - Update a subscriber
* [delete](#delete) - Delete a subscriber
* [create_bulk](#create_bulk) - Bulk create subscribers

## search

Search subscribers by their **email**, **phone**, **subscriberId** and **name**. 
    The search is case sensitive and supports pagination.Checkout all available filters in the query section.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_searchSubscribers" method="get" path="/v2/subscribers" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
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

## create

Create a subscriber with the subscriber attributes. 
      **subscriberId** is a required field, rest other fields are optional, if the subscriber already exists, it will be updated

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_createSubscriber" method="post" path="/v2/subscribers" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.create(fail_if_exists=False, create_subscriber_request_dto={
        "subscriber_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `fail_if_exists`                                                                | *bool*                                                                          | :heavy_check_mark:                                                              | N/A                                                                             |
| `create_subscriber_request_dto`                                                 | [models.CreateSubscriberRequestDto](../../models/createsubscriberrequestdto.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `idempotency_key`                                                               | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | A header for idempotency purposes                                               |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.SubscribersControllerCreateSubscriberResponse](../../models/subscriberscontrollercreatesubscriberresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.SubscriberResponseDtoError | 409                               | application/json                  |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 404, 405, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## retrieve

Retrieve a subscriber by its unique key identifier **subscriberId**. 
    **subscriberId** field is required.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_getSubscriber" method="get" path="/v2/subscribers/{subscriberId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
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

Update a subscriber by its unique key identifier **subscriberId**. 
    **subscriberId** is a required field, rest other fields are optional

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_patchSubscriber" method="patch" path="/v2/subscribers/{subscriberId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
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

Deletes a subscriber entity from the Novu platform along with associated messages, preferences, and topic subscriptions. 
      **subscriberId** is a required field.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_removeSubscriber" method="delete" path="/v2/subscribers/{subscriberId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
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

## create_bulk


      Using this endpoint multiple subscribers can be created at once. The bulk API is limited to 500 subscribers per request.
    

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersV1Controller_bulkCreateSubscribers" method="post" path="/v1/subscribers/bulk" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
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