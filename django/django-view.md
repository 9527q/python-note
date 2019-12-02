# 视图

## 1. request 对象

域名、路径相关

```py
from urlparse import urlsplit

request.path  # 获取不带参数的路径（/api/xxx/bb）
request.get_host()  # 域名
request.build_absolute_uri()  # 整个请求地址（包括http、域名、路径、参数）
url_split = urlsplit(request.build_absolute_uri())
url_split.scheme  # 'http' / 'https'
url_split.netloc  # 域名
```