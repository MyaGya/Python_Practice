# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


data = list(map(int, input().split()))

flag = True
# 중복되지 않는 6개의 숫자이며
if len(set(data)) == 6:
    # 1부터 45의 숫자일경우
    for s in data:
        if 1 <= s and s <= 45:
            pass
        else:
            flag = False
            break

    if flag:
        for i in range(len(data) - 1):
            if data[i] < data[i + 1]:
                pass
            else:
                flag = False

    if flag:
        print('true')
    else:
        print('false')
else:
    print('false')
