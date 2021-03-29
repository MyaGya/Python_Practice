import itertools
from collections import *

original = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

rotated = list(zip(*reversed(original)))


# print(rotated)


# 구조체 테스트

class TEST():
    def __init__(self, L):
        # x, y : 좌표
        self.x = L[0]
        self.y = L[1]
        # a : 0은 구조물 설치, 1은 삭제
        self.a = L[2]
        # b : 0은 삭제 1은 설치 
        self.b = L[3]


List = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

data = []
for L in List:
    data.append(TEST(L))

print(data[1].x)

# 순열 테스트

pool = ['A', 'B', 'C', 'D']

print(list(map(list, itertools.permutations(pool))))
print(list(map(''.join, itertools.permutations(pool))))
# 반복 테스트

List = deque()
List.append([1, 2, 3, 4, 5])

for i in List:
    i = 1
    print(i)

print(List)

# find 테스트

List = {1, 2, 3, 4, 5}
if 1 in List:
    print("TRUE")

# 반복 도중 리스트가 사라지면 어떻게되는가?

List = deque()
List.append(1)
List.append(2)
List.append(3)
List.append(4)
List.append(5)

try:
    for i in range(len(List)):
        if i == 0:
            del List[2]
        print(List[i])
except:
    pass
del List[2]
print(List)


class Node:
    def __init__(self):
        self.next = None


tmp = [[1 for _ in range(3)] for _ in range(10)]
print(tmp[9][2])

tmp = [1, 2, 3, 4, 5]
tmp2 = tmp
tmp2.clear()
print(tmp)


def solution(numbers: list[int,]):
    ret = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            ret.add(numbers[i] + numbers[j])
    return sorted(list(ret))


print(solution([1, 2, 3, 4, 5]))

tmp = list()
tmp.append('1')
tmp.append(1)
tmp.append(object)

print(tmp)

tmp = [3,1,2]


tmp = "Git pull request Test"