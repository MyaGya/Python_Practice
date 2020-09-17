def solution(s, n):
    # +26 -> 원래자리로 돌아온다
    # 따라서 원래 위치 - 'a'의 위치 + n 을 % 26을 한 결과값을 'a'로 더하면 구할 수 있다
    print(ord('a'))
    print(ord('z'))
    print(ord('A'))
    print(ord('Z'))
    ret = ""
    for char in s:
        if 'a' <= char <= 'z':
            ret += chr((ord(char) - 97 + n) % 26 + 97)
        elif 'A' <= char <= 'Z':
            ret += chr((ord(char) - 65 + n) % 26 + 65)
        else:
            ret += ' '
    return ret
print(solution("z",1))



print (['even' if i%2 == 0 else 'zero' if i ==0 else 'odd' for i in range(10)])