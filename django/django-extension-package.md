# django 相关扩展库

## 性能分析 django-profiler

[django-profiler](https://pypi.org/project/django-profiler/)

```py
import sys

from profiling import profile

@profile(stats=True, stats_buffer=sys.stdout)
def complex_computations():
    #some complex computations
```