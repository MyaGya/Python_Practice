def solution(s):
    new_s = []

    for c in s:
        if not new_s:
            new_s.append(c)
        elif new_s[-1] == c:
            new_s.pop()
        else:
            new_s.append(c)
    return 0 if new_s else 1
