def solution(s):
    s = s.split(' ')
    ret = ""
    for tmp_s in s:
        tmp_ret = ""
        for i in range(len(tmp_s)):
            if i%2 == 0: # 짝수
                tmp_ret += tmp_s[i].upper()
            else:
                tmp_ret += tmp_s[i].lower()
        ret += tmp_ret + " "
    return ret[:-1]

print(solution("try hello world"))