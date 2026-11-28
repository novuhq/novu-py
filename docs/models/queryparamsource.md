# QueryParamSource

Filter by request origin: 'http' for API triggers or 'inbound_email' for inbound mail

## Example Usage

```python
from novu_py.models import QueryParamSource

value = QueryParamSource.HTTP
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `HTTP`          | http            |
| `INBOUND_EMAIL` | inbound_email   |