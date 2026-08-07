# QueryParamConnectionMode

Scope results relative to the subscriber. `subscriber` returns only the subscriber-owned connections, `shared` returns only shared (workspace-level) connections. Omit to return both.

## Example Usage

```python
from novu_py.models import QueryParamConnectionMode

value = QueryParamConnectionMode.SUBSCRIBER
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `SUBSCRIBER` | subscriber   |
| `SHARED`     | shared       |