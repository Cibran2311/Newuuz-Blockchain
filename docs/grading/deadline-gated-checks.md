# Deadline-gated Checks

GitHub Actions can run checks only on certain dates.

## Manual final check

```yaml
on:
  workflow_dispatch:
```

## Scheduled final check

```yaml
on:
  schedule:
    - cron: "0 19 25 3 *"
```

## Python deadline mode

```python
from datetime import datetime, timezone

DEADLINE = datetime(2026, 3, 25, 18, 59, tzinfo=timezone.utc)

if datetime.now(timezone.utc) < DEADLINE:
    print("Practice check only")
else:
    print("Final grading mode")
```
