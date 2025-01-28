# Properties
(*subscribers.properties*)

## Overview

### Available Operations

* [update_online_flag](#update_online_flag) - Update subscriber online status

## update_online_flag

Used to update the subscriber isOnline flag.

### Example Usage

```python
from novu_py import Novu
import os

with Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
) as novu:

    res = novu.subscribers.properties.update_online_flag(subscriber_id="<id>", update_subscriber_online_flag_request_dto={
        "is_online": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `subscriber_id`                                                                                     | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `update_subscriber_online_flag_request_dto`                                                         | [models.UpdateSubscriberOnlineFlagRequestDto](../../models/updatesubscriberonlineflagrequestdto.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `idempotency_key`                                                                                   | *Optional[str]*                                                                                     | :heavy_minus_sign:                                                                                  | A header for idempotency purposes                                                                   |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.SubscribersControllerUpdateSubscriberOnlineFlagResponse](../../models/subscriberscontrollerupdatesubscriberonlineflagresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |