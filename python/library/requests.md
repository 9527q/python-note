# requests

> 为什么requests不是标准库？？？

```py
import requests
```

## 发送请求 Request

- GET：`requests.get(url, params=params_dict)`
  - params：传入字典数据，自动拼接到url后面
- POST：`requests.post(url, json=want_json_data)`
  - json：想要传递json数据，无需手动json.dumps，直接把想要序列化的数据扔给json数据即可

通用参数

- timeout：`requests.get(url, timeout=10)`，和服务器建立连接后服务器返回第一条数据的时限
  - 超出时限抛出错误 requests.exception.ReadtimeError

## 相应对象 Response

发送请求的方法都会返回一个 Response 对象，`resp = requests.get(url)`

属性和方法

- `resp.status_code` 响应状态码
- `resp.content` 二进制的响应体内容，只读
- `resp.text` 对响应体内容解码的结果，只读。使用的编码方式是程序猜的，可以通过 `resp.encoding` 指定
- `resp.encoding` 响应体内容编码方式，实例属性
- `resp.headers` 响应头数据，类字典类型，键不区分大小写，不存在则返回 None
- `resp.raise_for_status()` 当状态码是 [400,600) 时抛出错误 HTTPError