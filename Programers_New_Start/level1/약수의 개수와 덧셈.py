import math


# 해석 : 자연수가 제곱수면 그 수의 약수는 홀수이고, 제곱수가 아니면 약수는 짝수개이다
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if math.sqrt(i) % 1 == 0:
            answer -= i
        else:
            answer += i

    return answer


print(solution(13, 17))
