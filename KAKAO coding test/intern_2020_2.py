# 연산자 운선순위
from collections import deque
import itertools
import copy
def solution(expression):
    # 연산자 우선순위
    priority = list(itertools.permutations(['+', '-', '*'], 3))
    print(priority)

    # 데이터 추출
    data = deque()
    operator = deque()
    cnt = 0
    for i in range(len(expression)):
        if expression[i] == '-' or expression[i] == '+' or expression[i] == '*':
            data.append(int(expression[cnt:i]))
            operator.append((expression[i]))
            cnt = i+1
    data.append(int(expression[cnt:i+1]))
    # 연산 진행
    data_backup = copy.deepcopy(data)
    operator_backup = copy.deepcopy(operator)
    MAX = 0
    for pri in priority:
        data = copy.deepcopy(data_backup)
        operator = copy.deepcopy(operator_backup)
        for command in pri:
            while True:
                if command in operator:
                    idx = operator.index(command)
                    if command == '+':
                        data[idx] += data[idx+1]
                    elif command == '-':
                        data[idx] -= data[idx+1]
                    else:
                        data[idx] *= data[idx+1]
                    del data[idx+1]
                    del operator[idx]
                else:
                    break;
        MAX = max(MAX,abs(data[0]))
    return MAX
expression = input()
print(solution(expression))
