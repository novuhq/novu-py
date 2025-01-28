<!-- Start SDK Example Usage [usage] -->
### Trigger Notification Event

```python
# Synchronous Example
import novu_py
from novu_py import Novu
import os

with Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
) as novu:

    res = novu.trigger(trigger_event_request_dto=novu_py.TriggerEventRequestDto(
        name="workflow_identifier",
        to={
            "subscriber_id": "<id>",
        },
        payload={
            "comment_id": "string",
            "post": {
                "text": "string",
            },
        },
        bridge_url="https://example.com/bridge",
        overrides={
            "fcm": {
                "data": {
                    "key": "value",
                },
            },
        },
    ))

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import novu_py
from novu_py import Novu
import os

async def main():
    async with Novu(
        api_key=os.getenv("NOVU_API_KEY", ""),
    ) as novu:

        res = await novu.trigger_async(trigger_event_request_dto=novu_py.TriggerEventRequestDto(
            name="workflow_identifier",
            to={
                "subscriber_id": "<id>",
            },
            payload={
                "comment_id": "string",
                "post": {
                    "text": "string",
                },
            },
            bridge_url="https://example.com/bridge",
            overrides={
                "fcm": {
                    "data": {
                        "key": "value",
                    },
                },
            },
        ))

        # Handle response
        print(res)

asyncio.run(main())
```

### Trigger Notification Events in Bulk

```python
# Synchronous Example
import novu_py
from novu_py import Novu
import os

with Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
) as novu:

    res = novu.trigger_bulk(bulk_trigger_event_dto={
        "events": [
            novu_py.TriggerEventRequestDto(
                name="workflow_identifier",
                to={
                    "subscriber_id": "<id>",
                },
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                bridge_url="https://example.com/bridge",
                overrides={
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            ),
            novu_py.TriggerEventRequestDto(
                name="workflow_identifier",
                to=[
                    {
                        "topic_key": "<value>",
                        "type": novu_py.TriggerRecipientsTypeEnum.SUBSCRIBER,
                    },
                ],
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                bridge_url="https://example.com/bridge",
                overrides={
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            ),
            novu_py.TriggerEventRequestDto(
                name="workflow_identifier",
                to=[
                    "SUBSCRIBER_ID",
                    "SUBSCRIBER_ID",
                ],
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                bridge_url="https://example.com/bridge",
                overrides={
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            ),
        ],
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import novu_py
from novu_py import Novu
import os

async def main():
    async with Novu(
        api_key=os.getenv("NOVU_API_KEY", ""),
    ) as novu:

        res = await novu.trigger_bulk_async(bulk_trigger_event_dto={
            "events": [
                novu_py.TriggerEventRequestDto(
                    name="workflow_identifier",
                    to={
                        "subscriber_id": "<id>",
                    },
                    payload={
                        "comment_id": "string",
                        "post": {
                            "text": "string",
                        },
                    },
                    bridge_url="https://example.com/bridge",
                    overrides={
                        "fcm": {
                            "data": {
                                "key": "value",
                            },
                        },
                    },
                ),
                novu_py.TriggerEventRequestDto(
                    name="workflow_identifier",
                    to=[
                        {
                            "topic_key": "<value>",
                            "type": novu_py.TriggerRecipientsTypeEnum.SUBSCRIBER,
                        },
                    ],
                    payload={
                        "comment_id": "string",
                        "post": {
                            "text": "string",
                        },
                    },
                    bridge_url="https://example.com/bridge",
                    overrides={
                        "fcm": {
                            "data": {
                                "key": "value",
                            },
                        },
                    },
                ),
                novu_py.TriggerEventRequestDto(
                    name="workflow_identifier",
                    to=[
                        "SUBSCRIBER_ID",
                        "SUBSCRIBER_ID",
                    ],
                    payload={
                        "comment_id": "string",
                        "post": {
                            "text": "string",
                        },
                    },
                    bridge_url="https://example.com/bridge",
                    overrides={
                        "fcm": {
                            "data": {
                                "key": "value",
                            },
                        },
                    },
                ),
            ],
        })

        # Handle response
        print(res)

asyncio.run(main())
```

### Broadcast Event to All

```python
# Synchronous Example
from novu_py import Novu
import os

with Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
) as novu:

    res = novu.trigger_broadcast(trigger_event_to_all_request_dto={
        "name": "<value>",
        "payload": {
            "comment_id": "string",
            "post": {
                "text": "string",
            },
        },
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from novu_py import Novu
import os

async def main():
    async with Novu(
        api_key=os.getenv("NOVU_API_KEY", ""),
    ) as novu:

        res = await novu.trigger_broadcast_async(trigger_event_to_all_request_dto={
            "name": "<value>",
            "payload": {
                "comment_id": "string",
                "post": {
                    "text": "string",
                },
            },
        })

        # Handle response
        print(res)

asyncio.run(main())
```

### Cancel Triggered Event

```python
# Synchronous Example
from novu_py import Novu
import os

with Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
) as novu:

    res = novu.cancel(transaction_id="<id>")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from novu_py import Novu
import os

async def main():
    async with Novu(
        api_key=os.getenv("NOVU_API_KEY", ""),
    ) as novu:

        res = await novu.cancel_async(transaction_id="<id>")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->