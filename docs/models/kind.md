# Kind

Distinguishes delivery integrations from agent-runtime integrations. Defaults to "delivery". Agent integrations do not have a channel.

## Example Usage

```python
from novu_py.models import Kind

value = Kind.DELIVERY
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `DELIVERY` | delivery   |
| `AGENT`    | agent      |