'''
def solution(n):
    numbers = ['4', '1', '2']
    answer = ""
    while n:
        answer = numbers[n % 3] + answer
        # 자리수 빼주기
        n = n // 3 - (n % 3 == 0) # True는 1로 적용된다
    return answer
'''

def solution(n):
    change = ['1','2','4']
    ans = ""
    while n:
        ans += (change[(n-1) % 3])
        n = (n-1)// 3
    return ans[::-1]

print(solution(int(input())))