# admin 站点

ModelAdmin 类可以管理模型类在 admin 后台站点中的表现形式，一般放在 Django 应用（app）下的 admin.py 文件中。例如

```py
from django.contrib import admin
from myproject.myapp.models import Author

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)

# 当然这个 ModelAdmin 类什么自定义内容都没有，所以会展示默认样式
# 如果明确要展示默认样式，那么这个 ModelAdmin 完全可以不写，只是下面这一句就让 Author 模型类注册成功了，就会在 admin 站点中显示
# admin.site.register(Author)
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

## ModelAdmin options

### ModelAdmin.fields

添加和编辑页面展示哪些字段，给一个列表或元祖值，里面是字符串的字段名，显示的顺序就是你给定的顺序。可以有二级元祖，这样里面的内容会被放在一行里。

还可以自定义展示值，只要同时再定义一个同名的实例方法即可，这个实例方法需要一个obj参数（模型类实例），返回值即是显示值

### ModelAdmin.empty_value_display

可以规定空值时显示什么（本来默认是显示 `-`）,例如

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

- raw_id_fields
  - 元组，外键字段对应的属性名
  - 填入后站点中选择值时是放大镜搜索，会弹出新窗口选择，在编辑页会显示为id值，适合外键对应表的数据很多的情况
  - 不填的外键在选择值时是下拉列表的样子，适合外键对应表的数据较少的情况