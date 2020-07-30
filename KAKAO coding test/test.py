from collections import *
original = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

rotated = list(zip(*reversed(original)))

#print(rotated)


# 구조체 테스트

class TEST():
    def __init__(self,L):
        #x, y : 좌표
        self.x = L[0]
        self.y = L[1]
        # a : 0은 구조물 설치, 1은 삭제
        self.a = L[2]
        # b : 0은 삭제 1은 설치 
        self.b = L[3]

List = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

data = []
for L in List:
    data.append(TEST(L))

print(data[1].x)
