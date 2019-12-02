# hashids

加密ID

```python
import hashids

# 可以用 alphabet 参数(str)指定结果字符集，默认是大小写字母加数字
hash_ = hashids.Hashids(salt='8vrC#BedKqh9a*Np', min_length=10)
# 编码
hash_.encode(3) # KP3RLAW7MV  可以传多个值进去
# 解码
hash_.decode('KP3RLAW7MV')  # (3,)  返回的是一个元祖
```