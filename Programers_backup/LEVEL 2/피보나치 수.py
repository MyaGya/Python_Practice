'''
def solution(n):
    x1, x2, x3 = 0, 1, 1
    for i in range(n - 1):
        x3 = (x1 + x2) %1234567
        x1, x2 = x2, x3
    if n == 1 : return 1
    return x3
'''


def solution(n):
    value1, value2, value3 = 0, 1, 1  # 0, 1, 2
    for i in range(n - 2):
        value1, value2 = value2, value3
        value3 = (value1 + value2) % 1234567

    return value3


test = 'a'
test.isalpha()