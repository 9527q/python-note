# celery

[官方文档](http://docs.celeryproject.org/en/latest/)

## 开启celery服务

```sh
celery -A celery_task.tasks worker --loglevel=info
celery -A tasks worker --loglevel=info
celery -A celery_task.tasks worker --loglevel=info --logfile=celery.log
```

注意：tasks处的写法取决于执行命令时的位置，但是会影响使用
比如用了第二种写法，那么使用的地方必须是from tasks import work
比如用了第一种写法，那么使用的地方必须是from celery.tasks import work
也就是说从哪个位置启动celery服务应该取决于使用任务的地方在哪个层级（不同地方导包不一样）

开启后会创建5个相同的进程

--logfile参数指定日志文件，如果不指定则输出到控制台