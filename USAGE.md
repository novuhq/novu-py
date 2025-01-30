<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import novu_py
from novu_py import Novu
import os

with Novu(
    security=novu_py.Security(
        secret_key=os.getenv("NOVU_SECRET_KEY", ""),
    ),
) as novu:

    novu.support_controller_fetch_user_organizations(plain_card_request_dto={
        "timestamp": "<value>",
    })

    # Use the SDK ...
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
        security=novu_py.Security(
            secret_key=os.getenv("NOVU_SECRET_KEY", ""),
        ),
    ) as novu:

        await novu.support_controller_fetch_user_organizations_async(plain_card_request_dto={
            "timestamp": "<value>",
        })

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->