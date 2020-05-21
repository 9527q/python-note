# typing

Python 标准库，类型标注支持。

> Python 运行时不强制函数和变量的类型。

基本格式：

```py
def greeting(name: str) -> str:
    return 'Hello ' + name
```

函数的 `name` 参数预期为 str 类型，返回为 str 类型。

**子类型允许作为参数和返回值**，就是说标注了 str 类型，那么 str 的子类型也可以通过检查。父类型是不能通过子类型标注的检查器的检查的。

## 类型别名

将类型分配给别名来定义，它们是可互换的同义词，可以用于简化复杂类型签名，静态类型检查器对待别名和对待复杂的原对象是完全一致的。

例：

```py
from typing import Dict, Tuple, Sequence

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...
```

注：`None` 作为类型提示是特殊情况，并且由 `type(None)` 取代。

## NewType

使用 NewType() 辅助函数创建不同的类型，静态类型检查器会将新类型视为原始类型的子类。

```py
from typing import NewType

UserId = NewType('UserId', int)


def get_user_name(user_id: UserId) -> str:
    ...


user_a = get_user_name(UserId(42351))  # 检查通过
user_b = get_user_name(-1)  # 检查不通过
```

对 `UserId` 类型的变量执行所有的 `int` 支持的操作都没问题，结果会是 `int` 类型。这可以方便的在需要 `int` 的地方传入 `UserId`，并且防止无意中创建 `UserId`，例如：`UserId(23413) + UserId(54341)` 得到结果的类型是 `int` 而不是 `UserId`。

**注意**：这些检查仅仅由静态类型检查器执行。运行的时候，`Derived = NewType('Derived', Base)` 语句将使 `Derived` 成为一个函数，该函数直接返回任何传给它的参数。这意味着 `Derived(some_value)` 表达式不会创建新类或引入任何超出常规函数调用的开销。

也就是说，表达式 `some_value is Derived(some_value)` 在运行时总为真。

这也意味着无法创建 `Derived` 的子类型，因为它是运行时的标识函数，而不是实际的类型。下面这个运行时就会报错并且不进行类型检查。

```py
from typing import NewType

UserId = NewType('UserId', int)

# TypeError: function() argument 'code' must be code, not str
class AdminUserId(UserId): pass
```

但是可以基于派生的 `NewType` 创建 `NewType()`：

```py
from typing import NewType

UserId = NewType('UserId', int)
ProUserId = NewType('ProUserId', UserId)
```

并且 `ProUserId` 的类型检查将按预期工作。

> **类型别名和 `NewType`**
> 
> - 类型别名的两者完全等效，可以用于简化复杂签名
> - `NewType` 声明一个类型是另一种类型的子类，那么父类类型的值不能用于子类类型标记的地方，可以用于以最小的运行时间成本防止逻辑错误。

## Callable

可调用的。

标注参数类型和返回值类型： `Callable[[Arg1Type, Arg2Type], ReturnType]`。

例如：

```py
from typing import Callable

def feeder(get_next_item: Callable[[], str]) -> None:
    ...

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    ...
```

不指定参数类型仅指定返回值类型时，可以使用省略号代替 `Callable[..., ReturnType]`。

## 范型（Generic）

通用类型。

抽象基类也扩展为支持抽取操作

## 类、函数和装饰器

### typing.Union

联合类型；`Union[X, Y]` 意味着要么是 X，要么是 Y。

- 参数必须是类型，而且必须至少又一个参数，如
  ```py
  Union[int, str]
  ```
- 联合类型的联合类型会被展开打平
  ```py
  Union[Union[int, str], float] == Union[int, str, float]
  ```
- 仅有一个参数的联合类型会坍缩为参数自身
  ```py
  Union[int] == int  # 构造函数实际上返回 int
  ```
- 多余的参数会被跳过
  ```py
  Union[int, str, int] == Union[int, str]
  ```
- 比较联合类型时，忽略参数顺序
  ```py
  Union[int, str] == Union[str, int]
  ```
- 不能继承或者实例化联合类型
- 不能写成 `Union[X][Y]`
- 可以使用 `Optional[X]` 作为 `Union[X, None]` 的缩写。

### typing.Optional

可选类型。

`Optional[X]` 等价于 `Union[X, None]`。

**注意**，这和可选参数的概念不同，可选参数具有默认值。具有默认值的可选参数不需要类型注释上的 `Optional` 限定符，因为它是可选的。例如：

```py
def foo(arg: int=0) -> None:
    ...
```

另一方面，如果允许显式的 `None`，则无论参数是否为可选参数，都可以使用 `Optional`。例如：

```py
def foo(arg: Optional[int] = None) -> None:
    ...
```
