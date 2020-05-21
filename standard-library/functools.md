# functools

## `wraps`

> wrap: 包

可以生成一个装饰器，这个被生成的装饰器装饰其他函数时，不会改变最后得到函数的各种属性，比如函数名、文档说明等

用处实例：Django 的登陆验证 login_required 内部的 user_passes_test 中就用到了。
