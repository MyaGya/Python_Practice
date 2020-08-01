# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def isfind(data,number):
    global ans
    if(data[number] == 0):
        ans.append(0)
        ans.append(len(ans)+1)
        isfind(data,data[number])
    else:
        ans.append(1)
        ans.append(data[number])

tmp = input().split(';')
print(tmp)
number = int(tmp[0])
data = list(map(int,tmp[1][1:].split(' ')))
abs = []
isfind(data,number)

