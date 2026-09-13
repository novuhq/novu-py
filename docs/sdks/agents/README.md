# Agents

## Overview

Agents are conversational assistants that receive inbound messages from connected channels and respond through a custom code bridge or a managed runtime provider.
<https://docs.novu.co/agents>

### Available Operations

* [create](#create) - Create an agent
* [list](#list) - List all agents
* [send_reply](#send_reply) - Send an agent reply
* [retrieve](#retrieve) - Retrieve an agent
* [update](#update) - Update an agent
* [delete](#delete) - Delete an agent
* [update_bridge](#update_bridge) - Update an agent bridge

## create

Create an agent scoped to the current environment. The identifier must be unique per environment. Set `runtime` to `managed` and supply `managedRuntime` to provision a provider-hosted agent brain.

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentsController_createAgent" method="post" path="/v1/agents" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.create(novu_analytics_source="<value>", create_agent_request_dto={
        "name": "<value>",
        "identifier": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `novu_analytics_source`                                               | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `create_agent_request_dto`                                            | [models.CreateAgentRequestDto](../../models/createagentrequestdto.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `idempotency_key`                                                     | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | A header for idempotency purposes                                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.AgentsControllerCreateAgentResponse](../../models/agentscontrollercreateagentresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## list

Retrieve a cursor-paginated list of agents for the current environment. Use **after**, **before**, **limit**, **orderBy**, and **orderDirection** query parameters.

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentsController_listAgents" method="get" path="/v1/agents" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.list(request={
        "limit": 10,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.AgentsControllerListAgentsRequest](../../models/agentscontrollerlistagentsrequest.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.AgentsControllerListAgentsResponse](../../models/agentscontrollerlistagentsresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| models.ErrorDto                        | 414                                    | application/json                       |
| models.ErrorDto                        | 400, 401, 403, 404, 405, 409, 413, 415 | application/json                       |
| models.ValidationErrorDto              | 422                                    | application/json                       |
| models.ErrorDto                        | 500                                    | application/json                       |
| models.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## send_reply

Send a message or side-effect into an existing agent conversation from your backend.

Use this endpoint when you are not using `@novu/framework` (for example Python, Go, PHP, .NET, or Java SDKs),
or when a server process outside the bridge needs to post into a live conversation.

**Message actions**
- `reply` — markdown, interactive card, or tool-approval card (optional `files`)
- `edit` — update a previously delivered message in place
- `deleteMessages` — remove rendered platform messages (history is kept)
- `addReactions` — add emoji reactions to existing messages

**Turn control**
- `typing` — `{ status?: string }` to set status, or `"stop"` to clear
- `resolve` — mark the conversation resolved (optionally with a final reply)
- `error: true` — report a customer-runtime failure (cannot combine with other actions)

**Signals & tools**
- `signals` — metadata set/delete/clear, or trigger a Novu workflow
- `toolResults` — persist tool outputs into conversation history
- `toolApprovalRequest` — ledger a gated tool call (pair with an approval card reply)

Returns `{ data: { messageId, platformThreadId } }` when a reply or edit is delivered;
otherwise `{ data: null }`.

### Example Usage: addReaction

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="addReaction" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        add_reactions=[
            novu_py.AddReactionPayloadDto(
                message_id="1712345678.123456",
                emoji_name="white_check_mark",
            ),
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: cardReply

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="cardReply" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        reply=novu_py.CardReplyContentDto(
            card={
                "type": "card",
                "title": "Order #123",
                "children": [
                    {
                        "type": "text",
                        "content": "Your order is ready for pickup.",
                    },
                    {
                        "type": "button",
                        "id": "confirm",
                        "label": "Confirm",
                        "style": "primary",
                    },
                ],
            },
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: deleteMessage

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="deleteMessage" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        delete_messages=[
            novu_py.DeleteMessagePayloadDto(
                message_id="1712345678.123456",
            ),
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: editMessage

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="editMessage" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        edit=novu_py.EditPayloadDto(
            message_id="1712345678.123456",
            content=novu_py.MarkdownReplyContentDto(
                markdown="Updated: the report is now final.",
            ),
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: humanApprove

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="humanApprove" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        signals=[
            novu_py.HumanSignalDto(
                type=novu_py.HumanSignalDtoType.HUMAN,
                kind=novu_py.Kind.APPROVE,
                prompt="Deploy v2.4.1 to production?",
                request_id="hr_7c2e1a3b-4d5f-6789-abcd-ef0123456789",
            ),
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: markdownReply

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="markdownReply" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        reply=novu_py.MarkdownReplyContentDto(
            markdown="**Report ready.** Your weekly summary is attached.",
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: metadataSignal

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="metadataSignal" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        signals=[
            novu_py.TriggerSignalDto(
                type=novu_py.TriggerSignalDtoType.TRIGGER,
                workflow_id="order-shipped",
                to="subscriber-123",
                payload={
                    "orderId": "ORD-42",
                },
            ),
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: replyWithFile

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="replyWithFile" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        reply=novu_py.MarkdownReplyContentDto(
            markdown="Here is your report.",
            files=[
                novu_py.FileRefDto(
                    filename="report.pdf",
                    mime_type="application/pdf",
                    url="https://example.com/files/report.pdf",
                ),
            ],
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: resolveConversation

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="resolveConversation" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        reply=novu_py.MarkdownReplyContentDto(
            markdown="Glad that helped — marking this as resolved.",
        ),
        resolve=novu_py.ResolveDto(
            summary="Answered billing question about invoice INV-42.",
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: toolApprovalRequest

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="toolApprovalRequest" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        reply=novu_py.ToolApprovalCardReplyContentDto(
            tool_approval_card={
                "type": "tool-approval-card",
                "title": "Approve refund?",
                "subtitle": "issue_refund · ORD-42 · $25.00",
                "approveLabel": "Approve",
                "denyLabel": "Deny",
            },
        ),
        tool_approval_request=novu_py.ToolApprovalRequestPayloadDto(
            approval_id="apr_01HZX",
            tool_call_id="call_refund_1",
            name="issue_refund",
            input={
                "orderId": "ORD-42",
                "amountCents": 2500,
            },
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: toolResult

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="toolResult" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        reply=novu_py.MarkdownReplyContentDto(
            markdown="Your order **ORD-42** has shipped and should arrive by July 16.",
        ),
        tool_results=[
            novu_py.ToolResultDto(
                tool_call_id="call_abc123",
                tool_name="lookup_order",
                output=novu_py.Output(),
                preview="Order ORD-42 is shipped",
            ),
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: triggerWorkflow

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="triggerWorkflow" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        signals=[
            novu_py.TriggerSignalDto(
                type=novu_py.TriggerSignalDtoType.TRIGGER,
                workflow_id="order-shipped",
                to="subscriber-123",
                payload={
                    "orderId": "ORD-42",
                },
            ),
        ],
    ))

    # Handle response
    print(res)

```
### Example Usage: turnError

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="turnError" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        error=True,
    ))

    # Handle response
    print(res)

```
### Example Usage: typingStart

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="typingStart" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        typing=novu_py.TypingStatusDto(
            status="Looking up your order…",
        ),
    ))

    # Handle response
    print(res)

```
### Example Usage: typingStop

<!-- UsageSnippet language="python" operationID="AgentReplyController_handleAgentReplyHandler" method="post" path="/v1/agents/{agentId}/reply" example="typingStop" -->
```python
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.send_reply(agent_id="support-agent", agent_reply_payload_dto=novu_py.AgentReplyPayloadDto(
        conversation_id="64f5a1c2e8b7a3d9f0c1b2a3",
        integration_identifier="slack-support",
        typing=novu_py.Typing1.STOP,
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_id`                                                                                                                                                                                                                                      | *str*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                              | Agent identifier (slug) for the agent that owns the conversation.                                                                                                                                                                               | support-agent                                                                                                                                                                                                                                   |
| `agent_reply_payload_dto`                                                                                                                                                                                                                       | [models.AgentReplyPayloadDto](../../models/agentreplypayloaddto.md)                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                              | Reply payload. Provide at least one action: `reply`, `edit`, `resolve`, `signals`, `toolResults`, `toolApprovalRequest`, `addReactions`, `deleteMessages`, `typing`, or `error`. See named examples for common shapes used by server-side SDKs. |                                                                                                                                                                                                                                                 |
| `idempotency_key`                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                              | A header for idempotency purposes                                                                                                                                                                                                               |                                                                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                             |                                                                                                                                                                                                                                                 |

### Response

**[models.AgentReplyControllerHandleAgentReplyHandlerResponse](../../models/agentreplycontrollerhandleagentreplyhandlerresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## retrieve

Retrieve an agent by its external identifier (not the internal MongoDB id).

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentsController_getAgent" method="get" path="/v1/agents/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.retrieve(identifier="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentsControllerGetAgentResponse](../../models/agentscontrollergetagentresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## update

Update an agent by its external identifier.

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentsController_updateAgent" method="patch" path="/v1/agents/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.update(identifier="<value>", update_agent_request_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `identifier`                                                          | *str*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `update_agent_request_dto`                                            | [models.UpdateAgentRequestDto](../../models/updateagentrequestdto.md) | :heavy_check_mark:                                                    | N/A                                                                   |
| `idempotency_key`                                                     | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | A header for idempotency purposes                                     |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.AgentsControllerUpdateAgentResponse](../../models/agentscontrollerupdateagentresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## delete

Delete an agent by identifier, remove all agent-integration links, and clear the agent assignment from any workflows that reference it. For managed-runtime agents, pass `deleteFromProvider=true` to also archive the agent on the provider side (e.g. Anthropic). By default only the Novu record is deleted and the provider agent is left intact.

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentsController_deleteAgent" method="delete" path="/v1/agents/{identifier}" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.delete(identifier="<value>", delete_from_provider="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `identifier`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `delete_from_provider`                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `idempotency_key`                                                   | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A header for idempotency purposes                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentsControllerDeleteAgentResponse](../../models/agentscontrollerdeleteagentresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |

## update_bridge

Update the bridge URL configuration for an agent. Used by the CLI to register dev tunnel URLs. Refuses to activate dev bridges on production environments.

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentsController_updateAgentBridge" method="put" path="/v1/agents/{identifier}/bridge" -->
```python
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.agents.update_bridge(identifier="<value>", update_agent_bridge_request_dto={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `identifier`                                                                      | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `update_agent_bridge_request_dto`                                                 | [models.UpdateAgentBridgeRequestDto](../../models/updateagentbridgerequestdto.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `idempotency_key`                                                                 | *Optional[str]*                                                                   | :heavy_minus_sign:                                                                | A header for idempotency purposes                                                 |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.AgentsControllerUpdateAgentBridgeResponse](../../models/agentscontrollerupdateagentbridgeresponse.md)**

### Errors

| Error Type                        | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| models.ErrorDto                   | 414                               | application/json                  |
| models.ErrorDto                   | 400, 401, 403, 405, 409, 413, 415 | application/json                  |
| models.ValidationErrorDto         | 422                               | application/json                  |
| models.ErrorDto                   | 500                               | application/json                  |
| models.APIError                   | 4XX, 5XX                          | \*/\*                             |