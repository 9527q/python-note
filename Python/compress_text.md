# 压缩字符串

```py
def compress_text(text: str) -> str:
    """compress text.
    compress_text('aabcccccb')  -->  'a2b1c5b1'
    return text if len(result) >= len(text)

    O(n)
    """
    if not isinstance(text, str):
        raise TypeError('compress_text() need a str, not {}'.format(type(text)))
    res, letter, num = '', '', 0
    for letter_new in text:
        if letter_new == letter:
            num += 1
        else:
            res += letter + str(num) if num else ''
            letter, num = letter_new, 1

    return res if len(res) < len(text) else text
```
