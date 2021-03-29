'''
def solution(number, k):
    stack = [number[0]]
    for i in range(1, len(number)):
        if not stack:
            stack.append(number[i])
            continue
        while stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
            if k == 0:
                stack.append(number[i:])  # 종료시 남은 수 모두 삽입
                break
        else:
            stack.append(number[i])
            continue
        break
    return "".join(stack[:len(stack)-k]) if k else "".join(stack)

'''


def solution(number, k):
    stack = []
    # delete k
    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue
        stack.append(number[i])
        while len(stack) > 1 and stack[-1] > stack[-2]:
            k -= 1
            stack[-2] = stack[-1]
            stack.pop()
            if k == 0:
                break
        if k == 0:
            break
    return "".join(stack)[:-k] if k != 0 else "".join(stack) + number[i+1:]


print(solution("1924",2))