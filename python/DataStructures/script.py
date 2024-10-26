# -*- coding: latin-1 -*-

x = chr(0xc4) + chr(0xe8)  # x和y是相同的两个拉丁字符
y = '\xc4\xe8'             # '\xc4\xe8'是这两个字符对应的latin-1码值
for i in x, y:
    print(f"{i},{i.encode()},  {i.encode('latin-1')}")

