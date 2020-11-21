import re
from itertools import permutations
import copy

def calc(data, seq):
    for operator in seq:
        tmp_list = []
        i = 0
        while i < len(data):
            if operator == data[i]:
                if operator == '+':
                    tmp_list[-1] = int(tmp_list[-1]) + int(data[i+1])
                elif operator == '-':
                    tmp_list[-1] = int(tmp_list[-1]) - int(data[i+1])
                elif operator == '*':
                    tmp_list[-1] = int(tmp_list[-1]) * int(data[i+1])
                i += 1
            else:
                tmp_list.append(data[i])

            i += 1
        data = copy.copy(tmp_list)
    return data

def solution(expression):
    data = re.split('([-]|[+]|[*])', expression)
    tmp = ['+', '-', '*']
    sequence = list(permutations(tmp, 3))
    ret = []
    for seq in sequence:
        ret.append(abs(calc(data,seq)[0]))
    return max(ret)

print(solution("100-200*300-500+20"))
