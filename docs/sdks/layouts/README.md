# Layouts
(*layouts*)

## Overview

Layouts are reusable wrappers for your email notifications.
<https://docs.novu.co/platform/workflow/layouts>

### Available Operations

* [create](#create) - Create a layout
* [list](#list) - List all layouts
* [update](#update) - Update a layout
* [retrieve](#retrieve) - Retrieve a layout
* [delete](#delete) - Delete a layout
* [duplicate](#duplicate) - Duplicate a layout
* [generate_preview](#generate_preview) - Generate layout preview
* [usage](#usage) - Get layout usage

## create

Creates a new layout in the Novu Cloud environment

### Example Usage

<!-- UsageSnippet language="python" operationID="LayoutsController_create" method="post" path="/v2/layouts" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.layouts.create(create_layout_dto={
        "layout_id": "<id>",
        "name": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `create_layout_dto`                                                 | [models.CreateLayoutDto](../../models/createlayoutdto.md)           | :heavy_check_mark:                                                  | Layout creation details                                             |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LayoutsControllerCreateResponse](../../models/layoutscontrollercreateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## list

Retrieves a list of layouts with optional filtering and pagination

### Example Usage

<!-- UsageSnippet language="python" operationID="LayoutsController_list" method="get" path="/v2/layouts" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.layouts.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `request`                                                                           | [models.LayoutsControllerListRequest](../../models/layoutscontrollerlistrequest.md) | :heavy_check_mark:                                                                  | The request object to use for the request.                                          |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.LayoutsControllerListResponse](../../models/layoutscontrollerlistresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Updates the details of an existing layout, here **layoutId** is the identifier of the layout

### Example Usage

<!-- UsageSnippet language="python" operationID="LayoutsController_update" method="put" path="/v2/layouts/{layoutId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.layouts.update(layout_id="<id>", update_layout_dto={
        "name": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `layout_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `update_layout_dto`                                                 | [models.UpdateLayoutDto](../../models/updatelayoutdto.md)           | :heavy_check_mark:                                                  | Layout update details                                               |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LayoutsControllerUpdateResponse](../../models/layoutscontrollerupdateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Fetches details of a specific layout by its unique identifier **layoutId**

### Example Usage

<!-- UsageSnippet language="python" operationID="LayoutsController_get" method="get" path="/v2/layouts/{layoutId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.layouts.retrieve(layout_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `layout_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LayoutsControllerGetResponse](../../models/layoutscontrollergetresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Removes a specific layout by its unique identifier **layoutId**

### Example Usage

<!-- UsageSnippet language="python" operationID="LayoutsController__delete" method="delete" path="/v2/layouts/{layoutId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.layouts.delete(layout_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `layout_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the layout                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LayoutsControllerDeleteResponse](../../models/layoutscontrollerdeleteresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## duplicate

Duplicates a layout by its unique identifier **layoutId**. This will create a new layout with the content of the original layout.

### Example Usage

<!-- UsageSnippet language="python" operationID="LayoutsController_duplicate" method="post" path="/v2/layouts/{layoutId}/duplicate" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.layouts.duplicate(layout_id="<id>", duplicate_layout_dto={
        "name": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `layout_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `duplicate_layout_dto`                                              | [models.DuplicateLayoutDto](../../models/duplicatelayoutdto.md)     | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LayoutsControllerDuplicateResponse](../../models/layoutscontrollerduplicateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## generate_preview

Generates a preview for a layout by its unique identifier **layoutId**

### Example Usage

<!-- UsageSnippet language="python" operationID="LayoutsController_generatePreview" method="post" path="/v2/layouts/{layoutId}/preview" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.layouts.generate_preview(layout_id="<id>", layout_preview_request_dto={
        "preview_payload": {
            "subscriber": {
                "channels": [
                    {
                        "provider_id": novu_py.ChatOrPushProviderEnum.MATTERMOST,
                        "credentials": {
                            "webhook_url": "https://example.com/webhook",
                            "channel": "general",
                            "device_tokens": [
                                "token1",
                                "token2",
                                "token3",
                            ],
                            "alert_uid": "12345-abcde",
                            "title": "Critical Alert",
                            "image_url": "https://example.com/image.png",
                            "state": "resolved",
                            "external_url": "https://example.com/details",
                        },
                        "integration_id": "<id>",
                    },
                ],
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `layout_id`                                                               | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `layout_preview_request_dto`                                              | [models.LayoutPreviewRequestDto](../../models/layoutpreviewrequestdto.md) | :heavy_check_mark:                                                        | Layout preview generation details                                         |
| `idempotency_key`                                                         | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | A header for idempotency purposes                                         |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.LayoutsControllerGeneratePreviewResponse](../../models/layoutscontrollergeneratepreviewresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## usage

Retrieves information about workflows that use the specified layout by its unique identifier **layoutId**

### Example Usage

<!-- UsageSnippet language="python" operationID="LayoutsController_getUsage" method="get" path="/v2/layouts/{layoutId}/usage" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.layouts.usage(layout_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `layout_id`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LayoutsControllerGetUsageResponse](../../models/layoutscontrollergetusageresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |