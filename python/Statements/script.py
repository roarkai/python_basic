# -*- coding: utf-8
import sys
print(sys.path)

x = '文本'
y = '\xc4\xe8'
for i in x, y:
    print(f'{i}, {len(i)},{i.encode()},  {i.encode(''utf-8)}')

