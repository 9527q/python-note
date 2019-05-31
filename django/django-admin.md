# admin 站点

/admin

![admin](images/admin.png)

## 1. 注册

ModelAdmin 类可以管理模型类在 admin 后台站点中的表现形式，一般放在 Django 应用（app）下的 admin.py 文件中。例如

```py
from django.contrib import admin
from myproject.myapp.models import Author

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)

# 当然这个 ModelAdmin 类什么自定义内容都没有，所以会展示默认样式
# 如果明确要展示默认样式，那么这个 ModelAdmin 完全可以不写，只有下面这一句就让 Author 模型类注册成功了，就会在 admin 站点中显示

admin.site.register(Author)
```

> 还可以使用装饰器来完成注册
>
> ```py
> from django.contrib import admin
> from .models import Author
>
> @admin.register(Author)
> class AuthorAdmin(admin.ModelAdmin):
>     pass
> ```

## 2. `ModelAdmin` options

### 2.1 `list_display` 列表页展示哪些字段

一个元祖，指定列表页展示哪些字段，展示的顺序和元祖中的顺序一致。

还可以自定义展示字段，在本类下再加一个同名方法即可，再用  `diy_filed_name.short_description = 'xxx'` 来指定对应的标题栏值即可。

```py
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'count')  # count 是自定义字段

    def image(self, obj):  # 必有第二个参数，会传入数据对象
        return obj.lower_t.count()

    get_image.short_description = u"子工单数量"
```

### 2.2 `empty_value_display` 空值显示样式



可以规定列表页空值时显示什么（本来默认是显示 `-`）,例如

```py
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
```

还可以为每个自定义字段单独规定空值显示

```py
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'title', 'view_birth_date')

    def view_birth_date(self, obj):
        return obj.birth_date

    view_birth_date.empty_value_display = '???'
```

### 2.3 `raw_id_fields` 外键使用“放大镜搜索”

元祖，传入外键字段对应的属性名，放入此元祖的外键字段在编辑页都显示为放大镜搜索的格式。默认情况下都是下拉列表的样子。

下图上面一行是放入 `raw_id_fields` 的情况，下面一行是没有放入的情况。
![raw_id_fields](images/raw_id_fields.png)