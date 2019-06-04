# urllib

> Python3

## 解码 url 中的汉字

```python
>>> import urllib
>>> urllib.request.quote('汉语')
'%E6%B1%89%E8%AF%AD'
>>> urllib.request.unquote('%E6%B1%89%E8%AF%AD')
'汉语'
```