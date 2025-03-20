<!-- Start SDK Example Usage [usage] -->
### Trigger Notification Event

```python
# Synchronous Example
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.trigger(trigger_event_request_dto=novu_py.TriggerEventRequestDto(
        workflow_id="workflow_identifier",
        to=novu_py.SubscriberPayloadDto(
            subscriber_id="<id>",
        ),
        payload={
            "comment_id": "string",
            "post": {
                "text": "string",
            },
        },
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

async def main():

    async with Novu(
        secret_key="YOUR_SECRET_KEY_HERE",
    ) as novu:

        res = await novu.trigger_async(trigger_event_request_dto=novu_py.TriggerEventRequestDto(
            workflow_id="workflow_identifier",
            to=novu_py.SubscriberPayloadDto(
                subscriber_id="<id>",
            ),
            payload={
                "comment_id": "string",
                "post": {
                    "text": "string",
                },
            },
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

### Cancel Triggered Event

```python
# Synchronous Example
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
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

async def main():

    async with Novu(
        secret_key="YOUR_SECRET_KEY_HERE",
    ) as novu:

        res = await novu.cancel_async(transaction_id="<id>")

        # Handle response
        print(res)

asyncio.run(main())
```

### Broadcast Event to All

```python
# Synchronous Example
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
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

async def main():

    async with Novu(
        secret_key="YOUR_SECRET_KEY_HERE",
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

### Trigger Notification Events in Bulk

```python
# Synchronous Example
import novu_py
from novu_py import Novu


with Novu(
    secret_key="YOUR_SECRET_KEY_HERE",
) as novu:

    res = novu.trigger_bulk(bulk_trigger_event_dto={
        "events": [
            novu_py.TriggerEventRequestDto(
                workflow_id="workflow_identifier",
                to=novu_py.SubscriberPayloadDto(
                    subscriber_id="<id>",
                ),
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                overrides={
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            ),
            novu_py.TriggerEventRequestDto(
                workflow_id="workflow_identifier",
                to=[
                    novu_py.TopicPayloadDto(
                        topic_key="<value>",
                        type=novu_py.TriggerRecipientsTypeEnum.SUBSCRIBER,
                    ),
                ],
                payload={
                    "comment_id": "string",
                    "post": {
                        "text": "string",
                    },
                },
                overrides={
                    "fcm": {
                        "data": {
                            "key": "value",
                        },
                    },
                },
            ),
            novu_py.TriggerEventRequestDto(
                workflow_id="workflow_identifier",
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

async def main():

    async with Novu(
        secret_key="YOUR_SECRET_KEY_HERE",
    ) as novu:

        res = await novu.trigger_bulk_async(bulk_trigger_event_dto={
            "events": [
                novu_py.TriggerEventRequestDto(
                    workflow_id="workflow_identifier",
                    to=novu_py.SubscriberPayloadDto(
                        subscriber_id="<id>",
                    ),
                    payload={
                        "comment_id": "string",
                        "post": {
                            "text": "string",
                        },
                    },
                    overrides={
                        "fcm": {
                            "data": {
                                "key": "value",
                            },
                        },
                    },
                ),
                novu_py.TriggerEventRequestDto(
                    workflow_id="workflow_identifier",
                    to=[
                        novu_py.TopicPayloadDto(
                            topic_key="<value>",
                            type=novu_py.TriggerRecipientsTypeEnum.SUBSCRIBER,
                        ),
                    ],
                    payload={
                        "comment_id": "string",
                        "post": {
                            "text": "string",
                        },
                    },
                    overrides={
                        "fcm": {
                            "data": {
                                "key": "value",
                            },
                        },
                    },
                ),
                novu_py.TriggerEventRequestDto(
                    workflow_id="workflow_identifier",
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
<!-- End SDK Example Usage [usage] -->