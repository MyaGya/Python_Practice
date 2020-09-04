def solution(s):
    ret = " " # 임시로 띄어쓰기 삽입
    for c in s:
        if ret[-1] == ' ':
            ret += c.upper()
        else:
            ret += c.lower()

    return ret[1:]


print(solution(" A  Sdf Fft "))