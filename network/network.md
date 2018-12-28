# 网络

## GET请求传参格式

IP或域名[:port]/path/请求数据[?参1=值1[&参2=值2...]]

例：192.168.1.230:8000/shop.json?id=123&device_id=

访问本机：0.0.0.0:port  127.0.0.1:port  localhost:port  网络中IP或域名:port

启动服务时设置为0.0.0.0:port，即表示本程序用port（如8001）端口接入网络

[Get,Post请求方式经典详解](https://www.cnblogs.com/insane-Mr-Li/p/9058273.html)