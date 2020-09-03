from collections import Counter
def solution(n:int) -> int:
    cnt = Counter(bin(n))['1']
    for i in range(n+1,1000001):
        if Counter(bin(i))['1'] == cnt:
            return i



print(solution(78))






v = [[1, 4], [3, 4], [3, 10]]
print(Counter([L[0] for L in v]).items())
ret = [key for key, value in Counter([L[0] for L in v]).items() if value == 1]
ret += ([key for key, value in Counter([L[1] for L in v]).items() if value == 1])
print(ret)


A = [1]
B = [[2]]
A.append(B)
print (A)