# GenerateConnectOauthURLRequestDtoConnectionMode

Connection mode that determines how the channel connection is scoped. "subscriber" (default) associates the connection with a specific subscriber. "shared" associates the connection with a context instead of a subscriber.

## Example Usage

```python
from novu_py.models import GenerateConnectOauthURLRequestDtoConnectionMode

value = GenerateConnectOauthURLRequestDtoConnectionMode.SUBSCRIBER
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `SUBSCRIBER` | subscriber   |
| `SHARED`     | shared       |