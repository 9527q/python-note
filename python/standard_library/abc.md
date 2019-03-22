# abc

```py
from abc import ABC, abstractmethod
```

如果一个类继承自ABC，且有一些方法被abstractmethod修饰，那么子类必须重写这些方法才能实例化。