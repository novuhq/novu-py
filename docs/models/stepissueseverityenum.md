# StepIssueSeverityEnum

Blocking severity of the issue. `error` (default when omitted) blocks save; `warning` is a non-blocking notice.

## Example Usage

```python
from novu_py.models import StepIssueSeverityEnum

value = StepIssueSeverityEnum.ERROR
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ERROR`   | error     |
| `WARNING` | warning   |