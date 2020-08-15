def solution(n):
    numbers = ['4', '1', '2']
    answer = ""
    while n:
        answer = numbers[n % 3] + answer
        # 자리수 빼주기
        n = n // 3 - (n % 3 == 0) # True는 1로 적용된다
    return answer


print(solution(int(input())))