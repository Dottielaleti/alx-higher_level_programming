#!/usr/bin/python3
for x in range(122, 96, -1):
    ch = chr(x)
    case = ch.upper() if (x - 122) % 2 == 0 else ch.lower()
    print(case, end='')
