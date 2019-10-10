# better-excptions

在抛出错误信息时直接展示变量的值，可以在大部分情况省略掉 print 和 debug 的过程，大大缩短问题定位时间。

[GitHub](https://github.com/Qix-/better-exceptions)

## 在 Django 中使用

大体按照 [GitHub](https://github.com/Qix-/better-exceptions) 中说明的使用就好，有两点需要说明

1. 中间件的 `__init__` 方法的 `get_response` 参数应该有 `None` 默认值，这是中间件的标准写法，不是所有调用中间件的对象都有这个参数传递的
2. 在开发环境使用这个中间件时，**可能**会看到输出了两套错误信息，一套是 better-exc 的，一套是 Django 本来的，设置 `DEBUG = False` 即可。（貌似是因为 True 的时候第二套要返回给前端看吧）
