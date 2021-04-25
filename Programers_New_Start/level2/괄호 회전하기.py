from collections import deque


def collect(s):
    input_stack = ['[', '{', '(']
    match_success = {('[', ']'), ('(', ')'), ('{', '}')}
    stack = []

    for bracket in s:
        if not stack or bracket in input_stack:
            stack.append(bracket)
        else:
            last_value = stack.pop()
            if (last_value, bracket) in match_success:
                continue
            else:
                return False
    if not stack:
        return True
    return False


def solution(s):
    s = deque(s)

    answer = 0
    for _ in range(len(s)):
        s.append(s.popleft())
        if collect(s):
            answer += 1
    return answer


print(solution("[](){}"))
