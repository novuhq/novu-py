# Mode

OAuth flow mode. Use "connect" (default) to create a workspace channel connection, or "link_user" to identify the subscriber's Slack user ID without creating a connection.

## Example Usage

```python
from novu_py.models import Mode

value = Mode.CONNECT
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `CONNECT`   | connect     |
| `LINK_USER` | link_user   |