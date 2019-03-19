# 转换路径

转换路径为当前系统所需（针对 / \）

```py
import os


def convert_path(path: str) -> str:
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)
```