def solution(s: str):
    answer = ['0' for _ in range(len(s))]

    isUpper = True
    for i in range(len(s)):
        if s[i] == ' ':
            isUpper = True
            answer[i] = ' '
            continue
        if isUpper:
            answer[i] = s[i].upper()
        else:
            answer[i] = s[i].lower()
        isUpper = not isUpper

    return "".join(answer)
