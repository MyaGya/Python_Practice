# chr ord 함수 사용
def solution(name):
    idx = 0
    ret = 0
    name = list(name)
    while True:
        ret += min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx])+1) # 알파벳 계산
        name[idx] = 'A'
        for i in range(len(name)//2 + 2): # 3개 케이스 예외처리를 위해 + 2를 해주었다
            if name[(idx + len(name) - i) % len(name)] != 'A':
                break
        for j in range(len(name)//2 + 2):
            if name[(idx + len(name) + j) % len(name)] != 'A':
                break
        if name[(idx - i + len(name)) % len(name)] == 'A' and name[(idx + j) % len(name)] == 'A': # 종료조건
            break
        if i < j:
            ret += i
            idx = (idx - i + len(name)) % len(name)
        else:
            ret += j
            idx = (idx + j % len(name))
    return ret
print(solution("JAN"))