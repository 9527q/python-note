# multiprocessing

## 类

`Process()`

- 返回进程对象
  - 会复制全局环境（有运行代码会运行）
  - 进程间不共享全局变量
- init接收group，target, name, args:tuple, kwargs:dict参数
  - 与线程对比没有daemon参数，多了group
  > 其实线程也有group，默认为None且只能为None
- `strat()`方法：启动进程
- `is_alive()`：判断进程是否还活着
- `join([timeout])`: 是否等待子进程结束或等待多少秒
- `terminate()`：立即终止子进程
- `pid`：当前进程的pid
- `name`: 当前进程的别名
---
`Queue()`
- 返回队列对象，实现进程间通信，先进先出
- init可接收maxsize参数，默认值-1
- `put(obj, block=True, timeout=None)`
    - 如果block=False或者设置了timeout的情况下，已经满了就抛异常
- `put_nowait(obj)`
    - 如果已经满了则立即抛异常
- `get(block=True, timeout=None)`
- `get_nowait()`
- `qsize()` -> int
- `empty()` -> bool
- `full()` -> bool