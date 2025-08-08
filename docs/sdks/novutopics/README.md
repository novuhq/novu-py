# NovuTopics
(*subscribers.topics*)

## Overview

### Available Operations

* [list](#list) - Retrieve subscriber subscriptions

## list

Retrieve subscriber's topic subscriptions by its unique key identifier **subscriberId**. 
    Checkout all available filters in the query section.

### Example Usage

<!-- UsageSnippet language="python" operationID="SubscribersController_listSubscriberTopics" method="get" path="/v2/subscribers/{subscriberId}/subscriptions" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.subscribers.topics.list(request={
        "subscriber_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                   | [models.SubscribersControllerListSubscriberTopicsRequest](../../models/subscriberscontrollerlistsubscribertopicsrequest.md) | :heavy_check_mark:                                                                                                          | The request object to use for the request.                                                                                  |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.SubscribersControllerListSubscriberTopicsResponse](../../models/subscriberscontrollerlistsubscribertopicsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |