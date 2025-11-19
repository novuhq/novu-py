# Groups
(*translations.groups*)

## Overview

### Available Operations

* [delete](#delete) - Delete a translation group
* [retrieve](#retrieve) - Retrieve a translation group

## delete

Delete an entire translation group and all its translations

### Example Usage

<!-- UsageSnippet language="python" operationID="TranslationController_deleteTranslationGroupEndpoint" method="delete" path="/v2/translations/{resourceType}/{resourceId}" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    novu.translations.groups.delete(resource_type=novu_py.PathParamResourceType.WORKFLOW, resource_id="welcome-email")

    # Use the SDK ...

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `resource_type`                                                       | [models.PathParamResourceType](../../models/pathparamresourcetype.md) | :heavy_check_mark:                                                    | Resource type                                                         | workflow                                                              |
| `resource_id`                                                         | *str*                                                                 | :heavy_check_mark:                                                    | Resource ID                                                           | welcome-email                                                         |
| `idempotency_key`                                                     | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | A header for idempotency purposes                                     |                                                                       |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## retrieve

Retrieves a single translation group by resource type (workflow, layout) and resource ID (workflowId, layoutId)

### Example Usage

<!-- UsageSnippet language="python" operationID="TranslationController_getTranslationGroupEndpoint" method="get" path="/v2/translations/group/{resourceType}/{resourceId}" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.translations.groups.retrieve(resource_type=novu_py.TranslationControllerGetTranslationGroupEndpointPathParamResourceType.WORKFLOW, resource_id="welcome-email")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                             | Type                                                                                                                                                                  | Required                                                                                                                                                              | Description                                                                                                                                                           | Example                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `resource_type`                                                                                                                                                       | [models.TranslationControllerGetTranslationGroupEndpointPathParamResourceType](../../models/translationcontrollergettranslationgroupendpointpathparamresourcetype.md) | :heavy_check_mark:                                                                                                                                                    | Resource type                                                                                                                                                         | workflow                                                                                                                                                              |
| `resource_id`                                                                                                                                                         | *str*                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                    | Resource ID                                                                                                                                                           | welcome-email                                                                                                                                                         |
| `idempotency_key`                                                                                                                                                     | *Optional[str]*                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                    | A header for idempotency purposes                                                                                                                                     |                                                                                                                                                                       |
| `retries`                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                   |                                                                                                                                                                       |

### Response

**[models.TranslationGroupDto](../../models/translationgroupdto.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |