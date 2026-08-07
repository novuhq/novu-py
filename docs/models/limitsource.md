# LimitSource

Which constraint produced the limits. `plan` limits are lifted by upgrading; `system` limits (platform cap or per-organization override) require contacting the Novu team.

## Example Usage

```python
from novu_py.models import LimitSource

value = LimitSource.PLAN
```


## Values

| Name     | Value    |
| -------- | -------- |
| `PLAN`   | plan     |
| `SYSTEM` | system   |