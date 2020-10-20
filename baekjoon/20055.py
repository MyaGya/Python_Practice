# 문제의 상세한 설명이 되어있지 않아 중단
'''
1. '내려간다' 라는 표현이 로봇이 내려가는것인지 컨베이어 벨트 아랫쪽으로 내려간다는것인지 중의적인 표현임
2. 마찬가지로 '올라온다' 라는 표현도 중의적으로 적혀 있어 로봇이 밑의 컨베이어 벨트에서 올라오는 것인지 새로 올리는 것인지가 모호함
3. '이동한다'가 컨베이어 벨트가 이동하면서 로봇도 이동 되고 이에 따라 추가적으로 이동을 해야하는것인지가 모호함
즉, 로봇이 최종적으로 2칸을 움직이게 되는 것인지 1칸을 움직이게 되는 것인지가 중의적으로 적혀있음
또한, 이 경우에 2칸을 움직이면 내려가게 되는 로봇은 내려가버리게 되는 것인지 등의 케이스가 너무 모호함
따라서 조건이 더 추가될 때 까지 문제풀이를 중단함
'''

from collections import deque

### init belt ###
n, k = map(int, input().split())

belt = deque(map(int, input().split()))

for i in range(len(belt)):
    belt[i] = [belt[i], False]

### make solution ###
ret = 0
while True:
    ret += 1
    belt.appendleft(belt.pop())  # rotate
    if belt[len(belt)//2+1][1]:  # robot go down
        belt[len(belt)//2+1][1] = False
    for i in range(len(belt)//2,-1,-1):
        if belt[i][1] and belt[i][0] == 1:
            k -= 1
            if k == 0:
                pass

