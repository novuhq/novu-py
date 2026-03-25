# Workflows.Steps

## Overview

### Available Operations

* [generate_preview](#generate_preview) - Generate step preview
* [retrieve](#retrieve) - Retrieve workflow step

## generate_preview

Generates a preview for a specific workflow step by its unique identifier **stepId**

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkflowController_generatePreview" method="post" path="/v2/workflows/{workflowId}/step/{stepId}/preview" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.workflows.steps.generate_preview(workflow_id="<id>", step_id="<id>", generate_preview_request_dto={
        "preview_payload": {
            "subscriber": {
                "first_name": "Kennith",
                "last_name": "Schneider",
                "channels": [
                    {
                        "provider_id": novu_py.ChatOrPushProviderEnum.SLACK,
                        "integration_identifier": "<value>",
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
                "is_online": False,
                "last_online_at": "<value>",
            },
            "context": {
                "key": "org-acme",
            },
        },
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `workflow_id`                                                                 | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `step_id`                                                                     | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `generate_preview_request_dto`                                                | [models.GeneratePreviewRequestDto](../../models/generatepreviewrequestdto.md) | :heavy_check_mark:                                                            | Preview generation details                                                    |
| `idempotency_key`                                                             | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | A header for idempotency purposes                                             |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.WorkflowControllerGeneratePreviewResponse](../../models/workflowcontrollergeneratepreviewresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## retrieve

Retrieves data for a specific step in a workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkflowController_getWorkflowStepData" method="get" path="/v2/workflows/{workflowId}/steps/{stepId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.workflows.steps.retrieve(workflow_id="<id>", step_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `step_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkflowControllerGetWorkflowStepDataResponse](../../models/workflowcontrollergetworkflowstepdataresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |