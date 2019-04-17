# Anaconda

Anaconda是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项。

官网下载还是挺慢的，推荐到[清华镜像源](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)下载适合自己系统的最新版本，据说是五分钟一同步的。

## 命令

虚拟环境相关

```sh
# 列出所有虚拟环境，* 标记当前使用的是哪个
$ conda env list
$ conda-env list

$ conda create -n env_name python=x.x  # 创建虚拟环境
$ conda remove -n env_name --all  # 移除虚拟环境
$ conda activate env_name  # 使用虚拟环境
$ conda deactivate env_name  # 退出虚拟环境
$ conda activate base  # base 是基础环境（行为和虚拟环境一样，list能列出来，只不过envs目录下没有而已），使用基础环境就是退出了虚拟环境
```

虚拟环境的所有相关文件都在 anaconda/envs 目录下