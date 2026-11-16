# AuthMethod

Twilio: `apiKey` authenticates with `apiKey` (API Key SID) and `secretKey` (API Key Secret) on behalf of `accountSid`. When omitted, `token` (Auth Token) is used.

## Example Usage

```python
from novu_py.models import AuthMethod

value = AuthMethod.API_KEY
```


## Values

| Name      | Value     |
| --------- | --------- |
| `API_KEY` | apiKey    |