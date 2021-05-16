def solution(p):
    answer = ''
    # 종료조건
    if (p == ''): return ''

    # p는 균형잡힌 괄호 문자열
    u = str()
    v = str()
    flag = True
    balance = 0
    # 균형잡힌 괄호 문자열 u, v로 분리한다
    for i in range(len(p)):
        # u 종료조건
        if balance == 0 and i != 0:
            v = solution(p[i:len(p)])
            break;
        # make u
        else:
            u += p[i]
            if p[i] == '(':
                balance += 1
            else:
                balance -= 1
                if (balance < 0):
                    flag = False

    # 4. u가 올바른 괄호문자열인가?
    if flag:
        answer = u + v
    # 올바른 괄호문자가 아닐 경우
    else:
        tmp = str()
        for i in range(1, len(u) - 1):
            if (u[i] == '('):
                tmp += ')'
            else:
                tmp += '('
        answer += '(' + v + ')' + tmp

    return answer
