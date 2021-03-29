import sys
sys.setrecursionlimit(10**9)
def solution(a):
    # 처음과 끝은 항상 가능
    dp = dict()
    dp[(0,0)] = a[0]
    dp[(len(a)-1,len(a)-1)] = a[-1]
    def dp_calc(start, end):
        if (start,end) in dp:
            return dp[(start,end)]
        elif start == end:
            dp[(start,end)] = a[start]
        else:
            if i < start: # 오른쪽의 경우 dp
                dp[(start,end)] = min(a[start], dp_calc(start+1,end)) # 큰 풍선을 터트려서 작은 풍선의 값이 남아있다
            elif start < i: # 왼쪽의 경우 dp
                dp[(start,end)] = min(a[end], dp_calc(start, end-1))

        return dp[(start,end)]
    ret = 2
    for i in range(1, len(a)-1): # 처음과 끝이 아니면 자신이 제일 큰 수일 경우 불가능
        if dp_calc(0,i-1) < a[i] and dp_calc(i+1,len(a)-1) < a[i]:
           pass
        else:
            ret += 1
    return ret if len(a) >1 else 1 # 한개 케이스 예외처리



print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))