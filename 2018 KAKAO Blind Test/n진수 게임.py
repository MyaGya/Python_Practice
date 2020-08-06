# n : 진수
# number : 입력 숫자
def makelist(number, n):
    ret = []
    # 10진수 number를 진법변환하여 리스트로 출력시킨다
    refer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    # 최초 종료 조건
    if number == 0:
        ret.append(0)
        return ret

    while True:
        if number == 0:
            return ret
        ret.append(refer[number % n])
        number //= n


'''
n : 진법
t : 미리 굴려본 숫자의 갯수
m : 게임에 참가하는 인원
p : 튜브의 순서
'''
def solution(n, t, m, p):
    answer = ''
    number = 0
    myTurn = p-1
    while 0 < t:
        # 역방향으로 값이 나온다
        user = makelist(number, n)
        while len(user):
            value = user.pop()
            if myTurn == 0:
                answer += str(value)
                myTurn = m-1
                t -= 1
                if t == 0:
                    break;
            else:
                myTurn -= 1
        number += 1
    return answer


print(solution(2, 4, 2, 1))
