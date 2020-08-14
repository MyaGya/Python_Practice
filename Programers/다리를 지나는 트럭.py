from collections import deque

# 다리 위에 올라가있는 차의 시간을 계산한다.
# value는 흐른 시간이며, value 의 값이 None일경우 트럭이 건넌 후의 상황을 계산한다
def findTime(ans, value = None):
    if value is None:
        time = ans[0][0]
        for i in range(len(ans)):
            ans[i][0] -= time
        #시간과 용량값을 리턴한다
        return time,ans.popleft()[1]
    for i in range(len(ans)):
        ans[i][0] -= value
    return 0

def solution(bridge_length, weight, truck_weights):
    nowCapacity = 0
    time = 0
    # (remainTime, Weight)
    ans = deque()
    for truck in truck_weights:
        while True:
            # 다리 위에 올라 갈 수 있는 경우
            if nowCapacity + truck <= weight:
                # 트력을 올리고
                ans.append([bridge_length, truck])
                nowCapacity += truck
                # 모든 올라가있는 배열에 -1값을 지정한다
                findTime(ans, 1)
                if ans[0][0] == 0:
                    tmp = ans.popleft()
                    nowCapacity -= tmp[1]
                time += 1
                break
            # 다리 위에 트럭이 올라가지 못 하는 경우
            else:
                # 다음시간까지 건너뛰어 다시 계산한다
                tmp = findTime(ans)
                time += tmp[0]
                nowCapacity -= tmp[1]

    return time + ans[len(ans)-1][0] + 1
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
