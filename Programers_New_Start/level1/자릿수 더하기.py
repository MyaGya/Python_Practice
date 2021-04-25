def solution(n):
    answer = 0
    for value in list(str(n)):
        answer += int(value)
    return answer
