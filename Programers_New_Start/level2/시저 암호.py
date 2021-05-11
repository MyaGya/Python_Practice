def solution(s, n):
    answer = []
    for c in s:
        if 'a' <= c <= 'z':
            if ord(c) + n > ord('z'):
                answer.append(chr(ord('a') + (ord(c) + n) - ord('z') - 1))
            else:
                answer.append(chr(ord(c) + n))
        elif 'A' <= c <= 'Z':
            if ord(c) + n > ord('Z'):
                answer.append(chr(ord('A') + (ord(c) + n) - ord('Z') - 1))
            else:
                answer.append(chr(ord(c) + n))
        else:
            answer.append(' ')

    return "".join(answer)


print(solution("a B z", 4))
