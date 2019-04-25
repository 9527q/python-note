# 测试

```sh
# 测试所有
$ python manage.py test
# 仅测试某个应用
$ python manage.py test <appname>
# 仅测试某个应用的某个测试类
$ python manage.py test <appname>.tests.<ATestCase>
# 仅测试某个应有的某个测试类的某个方法
$ python manage.py test <appname>.tests.<ATestCase>.<test_func>
```

## 创建测试数据库费时

Django 有很多迁移文件，创建测试数据库时可以不考虑迁移文件而直接依照模型类创建，这样做会大大缩减创建测试数据库的时间。

有两种实现方案：1. 重写 MIGRATION_MODULES；2. 使用命令扩展

还有一个通过使用上次的测试数据库来缩短测试数据库创建时间的方案：3. 测试完毕后不删除测试数据库

### 1. 重写 MIGRATION_MODULES

在项目 settings.py 最后加入以下代码，测试时即可忽略迁移文件

```py
# Test without migration
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'
if TESTING:
    print('=========================')
    print('In TEST Mode - Disabling Migrations')
    print('=========================')

    class DisableMigrations(object):

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
```

### 2. 使用命令扩展：`django-test-without-migrations`

> Django 1.7+

1. pip 安装 `django-test-without-migrations`

   ```sh
   pip install django-test-without-migrations
   ```

   > 别忘了更新 requirements

2. 添加到 settings.py 的 INSTALLED_APPS 中

   ```py
   INSTALLED_APPS = (
    # ...
    'test_without_migrations',
   )
   ```

   > 如果还使用了其他关于测试命令 `test` 的扩展，且其在 INSTALLED_APPS 中的位置落后于本扩展，那么还需要一个设置来保证其他扩展能正常工作，以 Django-nose 为例：
   > 
   > ```py
   > TEST_WITHOUT_MIGRATIONS_COMMAND = 'django_nose.management.commands.test.Command'
   > ```

3. 使用测试命令 `test` 时加上参数即可
   ```sh
   # 两种均可
   $ python manage.py test --nomigrations
   $ python manage.py test -n
   # 指定 app 的话加到参数后面即可
   $ python manage.py test -n <appname>
   ```

### 3. 测试完毕后不删除测试数据库

使用下面的测试命令，测试完毕后不删除测试数据库，下次再创建时就不需要那么多时间了

```bash
python manage.py test --keepdb
```****