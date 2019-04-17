# Jupyter Notebook

## 修改解释器

1. 查看内核文件所在位置
    ```sh
    jupyter kernelspec list
    ```
    ![jupyter_kernel_spec](images/jupyter_kernelspec_list.png)
2. 进入上述命令显示的位置，打开 `kernel.json` 文件，`"argv"` 列表的第一个值就是解释器，修改为自己想要的即可

> 改完后不能用呀，使用不了(jupyterlab)