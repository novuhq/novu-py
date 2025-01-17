<!-- Start SDK Example Usage [usage] -->
### Trigger Notification Event

```python
# Synchronous Example
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.trigger(request={
    "name": "workflow_identifier",
    "to": {
        "subscriber_id": "<id>",
    },
    "payload": {
        "comment_id": "string",
        "post": {
            "text": "string",
        },
    },
    "bridge_url": "https://example.com/bridge",
    "overrides": {
        "fcm": {
            "data": {
                "key": "value",
            },
        },
    },
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from novu_py import Novu
import os

async def main():
    s = Novu(
        api_key=os.getenv("NOVU_API_KEY", ""),
    )
    res = await s.trigger_async(request={
        "name": "workflow_identifier",
        "to": {
            "subscriber_id": "<id>",
        },
        "payload": {
            "comment_id": "string",
            "post": {
                "text": "string",
            },
        },
        "bridge_url": "https://example.com/bridge",
        "overrides": {
            "fcm": {
                "data": {
                    "key": "value",
                },
            },
        },
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```

### Trigger Notification Events in Bulk

```python
# Synchronous Example
import novu_py
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.trigger_bulk(request={
    "events": [
        {
            "name": "workflow_identifier",
            "to": {
                "subscriber_id": "<id>",
            },
            "payload": {
                "comment_id": "string",
                "post": {
                    "text": "string",
                },
            },
            "bridge_url": "https://example.com/bridge",
            "overrides": {
                "fcm": {
                    "data": {
                        "key": "value",
                    },
                },
            },
        },
        {
            "name": "workflow_identifier",
            "to": {
                "topic_key": "<value>",
                "type": novu_py.TriggerRecipientsTypeEnum.SUBSCRIBER,
            },
            "payload": {
                "comment_id": "string",
                "post": {
                    "text": "string",
                },
            },
            "bridge_url": "https://example.com/bridge",
            "overrides": {
                "fcm": {
                    "data": {
                        "key": "value",
                    },
                },
            },
        },
        {
            "name": "workflow_identifier",
            "to": [
                "SUBSCRIBER_ID",
                "SUBSCRIBER_ID",
            ],
            "payload": {
                "comment_id": "string",
                "post": {
                    "text": "string",
                },
            },
            "bridge_url": "https://example.com/bridge",
            "overrides": {
                "fcm": {
                    "data": {
                        "key": "value",
                    },
                },
            },
        },
    ],
})

if res is not None:
    # handle response
    pass
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
    s = Novu(
        api_key=os.getenv("NOVU_API_KEY", ""),
    )
    res = await s.trigger_bulk_async(request={
        "events": [
            {
                "name": "workflow_identifier",
                "to": {
                    "subscriber_id": "<id>",
                },
                "payload": {
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                "bridge_url": "https://example.com/bridge",
                "overrides": {
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            },
            {
                "name": "workflow_identifier",
                "to": {
                    "topic_key": "<value>",
                    "type": novu_py.TriggerRecipientsTypeEnum.SUBSCRIBER,
                },
                "payload": {
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                "bridge_url": "https://example.com/bridge",
                "overrides": {
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            },
            {
                "name": "workflow_identifier",
                "to": [
                    "SUBSCRIBER_ID",
                    "SUBSCRIBER_ID",
                ],
                "payload": {
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                "bridge_url": "https://example.com/bridge",
                "overrides": {
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            },
        ],
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```

### Broadcast Event to All

```python
# Synchronous Example
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.trigger_broadcast(request={
    "name": "<value>",
    "payload": {
        "comment_id": "string",
        "post": {
            "text": "string",
        },
    },
    "overrides": {},
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from novu_py import Novu
import os

async def main():
    s = Novu(
        api_key=os.getenv("NOVU_API_KEY", ""),
    )
    res = await s.trigger_broadcast_async(request={
        "name": "<value>",
        "payload": {
            "comment_id": "string",
            "post": {
                "text": "string",
            },
        },
        "overrides": {},
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```

### Cancel Triggered Event

```python
# Synchronous Example
from novu_py import Novu
import os

s = Novu(
    api_key=os.getenv("NOVU_API_KEY", ""),
)

res = s.cancel(transaction_id="<id>")

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from novu_py import Novu
import os

async def main():
    s = Novu(
        api_key=os.getenv("NOVU_API_KEY", ""),
    )
    res = await s.cancel_async(transaction_id="<id>")
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->