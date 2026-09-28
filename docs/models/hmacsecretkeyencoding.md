# HmacSecretKeyEncoding

Email webhook: how `secretKey` is interpreted when signing webhook calls. `text` signs with the raw UTF-8 bytes; `base64`/`hex` decode it to binary first (e.g. for AWS KMS).

## Example Usage

```python
from novu_py.models import HmacSecretKeyEncoding

value = HmacSecretKeyEncoding.TEXT
```


## Values

| Name     | Value    |
| -------- | -------- |
| `TEXT`   | text     |
| `BASE64` | base64   |
| `HEX`    | hex      |