from collections import deque


def solution(ball, order):
    ans = []
    ball = deque(ball)
    waiting = dict()  # 특정 공을 뺏을 때, 다음 공이 waiting상태라면 출력한다

    for i in order:
        if i == ball[-1]: # 공이 맨 뒤에 있을 경우
            ans.append(ball.pop())
            while ball:
                if ball[-1] in waiting:  # 공이 기다리고 있으면 출력한다
                    ans.append(ball.pop())
                else:
                    break
        elif i == ball[0]: # 공이 맨 앞에 있을 경우
            ans.append(ball.popleft())
            while ball:
                if ball[0] in waiting:  # 공이 기다리고 있으면 출력한다
                    ans.append(ball.popleft())
                else:
                    break
        else:  # 공이 앞이나 뒤에 없는 경우
            waiting[i] = True
    return ans

print(solution([1, 2, 3, 4, 5, 6],[1,3,2,4,5,6]))