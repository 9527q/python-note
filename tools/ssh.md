# SSH

## Ubuntu安装SSH服务

```sh
sudo apt-get install openssh-server
```

## 生成秘钥

```sh
ssh-keygen
```

1. 首先选择存储位置，默认是`~/.ssh`目录
2. 然后要求输入口令，可以为空
3. 存储目录下有一对以`id_dsa`或`id_rsa`命名的文件
4. 后缀`.pub`是公钥，另一个是私钥
