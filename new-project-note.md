# 新 Django 项目启动笔记

- 版本：python=3.7.6，django=3.0.2，
    ```shell
    $ pip list
    Package    Version
    ---------- -------------------
    asgiref    3.2.3
    Django     3.0.2
    pip        19.3.1
    pytz       2019.3
    setuptools 44.0.0.post20200106
    sqlparse   0.3.0
    wheel      0.33.6
    ```
- 环境名称 ams

## anaconda

创建环境的时候会自动安装一些其他的包，可以使用 `pip freeze` 查看，都用 pip 卸载掉就得到干净的 python 环境了。以后就可以直接 `pip freeze > requirements.txt` 来更新 requriements 了。

## python

### 3.7 的变化

- 交互式环境中有 Tab 自动填写功能了。
  - 当只有一个备选时，Tab 就直接填写了；当有多个备选时，二次 Tab 可以弹出所有备选项。
  - 不知道是不是所有 python3 都这样

## Django 3.0

### 新建 Django 项目

```python
$ django-admin startproject mysite
```

### 查看 Django 版本

1. 运行代码查看
    ```python
    import djanog

    print(django.get_version())
    ```
2. shell 查看 `python -m django --verison`

### Django 的 SECRET_KEY 生成

```py
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

### 起三个文件

用三个 manage.py 配合三个 settings.py 和三个 wsgi.py，每个使用不同的配置，每个单独生成一下 SECRETY_KEY

### setting.py

mysql 数据库，需要安装 Python 的 mysql-client 的包，不同 Py、Dj、MS 需要的包版本不同，看错误提示即可。（线上的记得改Debug）

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'dev',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
```

时区

```py
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```

## sentry 错误信息查看

在 sentry 上建一个项目

### 在 Django 中使用 sentry

1. `pip install raven --upgrade`
   1. `pip freeze > requirements.txt`
2. 添加 Django app
    ```py
    INSTALLED_APPS = (
    'raven.contrib.django.raven_compat',
    )
    ```
   1. 添加 Django settings 参数
        ```py
        import os
        import raven

        RAVEN_CONFIG = {
            'dsn': '从 senty 新建项目后可以找到',
            # If you are using git, you can also automatically configure the
            # release based on the git info.
            'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
        }
        ```
3. 测试
    ```bash
    $ python manage.py raven test
    ```
4. 使用
    ```py
    from raven.contrib.django.raven_compat.models import client

    client.captureException()
    ```

### 新建app

```bash
$ python manage.py startapp account
```

### class Meta

abstract = True，表明为基类，不会创建数据表，不会继承Meta里的属性，只会继承字段。

verbose_name_plural 就是复述的描述，比如在admin首页显示的表明就是其实就是取自这里

## git

### 新建一个 gitlab 空项目后，如何将本地文件推上去

命令行指引
您还可以按照以下说明从计算机中上传现有文件。


Git 全局设置

    git config --global user.name "刘宇琪"
    git config --global user.email "liuyuqi@honganrobots.com"

创建一个新仓库

    git clone git@git.honganhome.com:software/ams.git
    cd ams
    touch README.md
    git add README.md
    git commit -m "add README"
    git push -u origin master

推送现有文件夹

    cd existing_folder
    git init
    git remote add origin git@git.honganhome.com:software/ams.git
    git add .
    git commit -m "Initial commit"
    git push -u origin master

推送现有的 Git 仓库

    cd existing_repo
    git remote rename origin old-origin
    git remote add origin git@git.honganhome.com:software/ams.git
    git push -u origin --all
    git push -u origin --tags

### git 的用户信息设置

`git config --global user.name` 这是基本格式。

上面的基本格式就是查看全局的用户名，把 name 换成 email 就是查看邮箱。如果不加 --global 参数就是查看当前 git 仓库的用户信息（当前目录必须是一个 git 仓库才行）

把上面的基本格式后面再加一个词，就是设置这个词为用户民/邮箱。同样，--global 参数还是用来控制设置全局的还是当前仓库的。

也就是说我们可以给每一个仓库设置不同的用户名和邮箱信息。

当新建一个 git 仓库时，里面初始的用户信息是使用 glogal 的。

### 设置文件名大小写敏感

```bash
$ git config core.ignorecase false
```

### pre-commit 配置

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.4.0
    hooks:
    -   id: check-added-large-files
    -   id: check-docstring-first
    -   id: end-of-file-fixer
    -   id: fix-encoding-pragma
        args: ['--remove']
    -   id: flake8
        language_version: python3.7
    -   id: name-tests-test
        args: ['--django']
    -   id: trailing-whitespace
-   repo: https://github.com/asottile/reorder_python_imports
    rev: v1.9.0
    hooks:
    -   id: reorder-python-imports
        language_version: python3.7
        args:
        - --separate-relative
        - --separate-from-import
        - --remove-import
        - from __future__ import absolute_import
        - --remove-import
        - from __future__ import division
        - --remove-import
        - from __future__ import print_function
        - --remove-import
        - from __future__ import unicode_literals
        - --remove-import
        - from __future__ import with_statement
-   repo: https://github.com/asottile/pyupgrade
    rev: v1.26.1
    hooks:
    -   id: pyupgrade
```

## mysql

创建数据库：`create database ams_dev character set utf8mb4;`，默认的 collate 是 utf8mb4_general_ci，ci 表示不区分大小写。