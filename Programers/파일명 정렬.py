import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+{1,5}', file)[0])) # 숫자만 추출
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0]) # 문자만 추출
    return b


'''
def solution(files):
    data = []
    for s in files:
        head = ""
        number = ""
        for i in range(len(s)):
            if not s[i].isdigit():
                head += s[i]
            else:
                while i <len(s):
                    if s[i].isdigit():
                        number += s[i]
                        i += 1
                    else:
                        break
                break
        data.append([s,head.lower(),int(number)])
    # end make head,number
    data.sort(key=lambda x: (x[1],x[2]))
    ret = []
    for L in data:
        ret.append(L[0])
    return ret
'''

A = {1,2,3}
B = {3,4,5}
A.update((B))
print (A)