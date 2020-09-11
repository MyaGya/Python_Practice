def solution(number, k):
    start, end = 0, len(number) - (len(number)-k) + 1
    ret = ""
    for _ in range(len(number)-k):
        MAX = ''
        idx = 0
        for i in range(start,end):
            if number[i] > MAX:
                MAX = number[i]
                idx = i
        start = idx + 1
        end += 1
        ret += MAX
    return ret
print(solution("4177252841",0))