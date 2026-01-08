# Workflows

## Overview

All notifications are sent via a workflow. Each workflow acts as a container for the logic and blueprint that are associated with a type of notification in your system.
<https://docs.novu.co/workflows>

### Available Operations

* [create](#create) - Create a workflow
* [list](#list) - List all workflows
* [update](#update) - Update a workflow
* [get](#get) - Retrieve a workflow
* [delete](#delete) - Delete a workflow
* [patch](#patch) - Update a workflow
* [sync](#sync) - Sync a workflow

## create

Creates a new workflow in the Novu Cloud environment

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkflowController_create" method="post" path="/v2/workflows" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.workflows.create(create_workflow_dto=novu_py.CreateWorkflowDto(
        name="<value>",
        workflow_id="<id>",
        steps=[],
        preferences=novu_py.PreferencesRequestDto(
            user=novu_py.UserWorkflowPreferencesDto(
                all=novu_py.WorkflowPreferenceDto(
                    enabled=True,
                    read_only=False,
                ),
                channels={
                    "email": novu_py.ChannelPreferenceDto(
                        enabled=True,
                    ),
                    "sms": novu_py.ChannelPreferenceDto(
                        enabled=False,
                    ),
                },
            ),
            workflow=novu_py.PreferencesRequestDtoWorkflow(
                all=novu_py.WorkflowPreferenceDto(
                    enabled=True,
                    read_only=False,
                ),
                channels={
                    "email": novu_py.ChannelPreferenceDto(),
                    "sms": novu_py.ChannelPreferenceDto(
                        enabled=False,
                    ),
                },
            ),
        ),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `create_workflow_dto`                                               | [models.CreateWorkflowDto](../../models/createworkflowdto.md)       | :heavy_check_mark:                                                  | Workflow creation details                                           |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkflowControllerCreateResponse](../../models/workflowcontrollercreateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## list

Retrieves a list of workflows with optional filtering and pagination

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkflowController_searchWorkflows" method="get" path="/v2/workflows" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.workflows.list(request={
        "limit": 10,
        "offset": 0,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.WorkflowControllerSearchWorkflowsRequest](../../models/workflowcontrollersearchworkflowsrequest.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.WorkflowControllerSearchWorkflowsResponse](../../models/workflowcontrollersearchworkflowsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## update

Updates the details of an existing workflow, here **workflowId** is the identifier of the workflow

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkflowController_update" method="put" path="/v2/workflows/{workflowId}" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.workflows.update(workflow_id="<id>", update_workflow_dto=novu_py.UpdateWorkflowDto(
        name="<value>",
        steps=[],
        preferences=novu_py.PreferencesRequestDto(
            user=novu_py.UserWorkflowPreferencesDto(
                all=novu_py.WorkflowPreferenceDto(
                    enabled=True,
                    read_only=False,
                ),
                channels={
                    "email": novu_py.ChannelPreferenceDto(
                        enabled=True,
                    ),
                    "sms": novu_py.ChannelPreferenceDto(
                        enabled=False,
                    ),
                },
            ),
            workflow=novu_py.PreferencesRequestDtoWorkflow(
                all=novu_py.WorkflowPreferenceDto(
                    enabled=True,
                    read_only=False,
                ),
                channels={
                    "email": novu_py.ChannelPreferenceDto(),
                    "sms": novu_py.ChannelPreferenceDto(
                        enabled=False,
                    ),
                },
            ),
        ),
        origin=novu_py.ResourceOriginEnum.EXTERNAL,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `update_workflow_dto`                                               | [models.UpdateWorkflowDto](../../models/updateworkflowdto.md)       | :heavy_check_mark:                                                  | Workflow update details                                             |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkflowControllerUpdateResponse](../../models/workflowcontrollerupdateresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## get

Fetches details of a specific workflow by its unique identifier **workflowId**

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkflowController_getWorkflow" method="get" path="/v2/workflows/{workflowId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.workflows.get(workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `environment_id`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkflowControllerGetWorkflowResponse](../../models/workflowcontrollergetworkflowresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## delete

Removes a specific workflow by its unique identifier **workflowId**

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkflowController_removeWorkflow" method="delete" path="/v2/workflows/{workflowId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.workflows.delete(workflow_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkflowControllerRemoveWorkflowResponse](../../models/workflowcontrollerremoveworkflowresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## patch

Partially updates a workflow by its unique identifier **workflowId**

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkflowController_patchWorkflow" method="patch" path="/v2/workflows/{workflowId}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.workflows.patch(workflow_id="<id>", patch_workflow_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `patch_workflow_dto`                                                | [models.PatchWorkflowDto](../../models/patchworkflowdto.md)         | :heavy_check_mark:                                                  | Workflow patch details                                              |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkflowControllerPatchWorkflowResponse](../../models/workflowcontrollerpatchworkflowresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## sync

Synchronizes a workflow to the target environment

### Example Usage

<!-- UsageSnippet language="python" operationID="WorkflowController_sync" method="put" path="/v2/workflows/{workflowId}/sync" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.workflows.sync(workflow_id="<id>", sync_workflow_dto={
        "target_environment_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `workflow_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `sync_workflow_dto`                                                 | [models.SyncWorkflowDto](../../models/syncworkflowdto.md)           | :heavy_check_mark:                                                  | Sync workflow details                                               |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WorkflowControllerSyncResponse](../../models/workflowcontrollersyncresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |