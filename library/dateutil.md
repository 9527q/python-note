# dateutil

很好用的时间组件，比如当我们想算下个月的今天时，直接加一个月的时间增量就好了，而不需要考虑天数、月份等

```python
import datetime

from dateutil.relativedelta import relativedelta

today = datetime.date.today()  # datetime.date(2019, 12, 3)
next_month_today = today + relativedelta(months=1)  # datetime.date(2020, 1, 3)
```
