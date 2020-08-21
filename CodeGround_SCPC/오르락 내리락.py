T = int(input())
visited = dict()
psum = dict()
def solution(value):
    if value in visited:
        return visited[value]
    # 짝수인 경우
    if value % 2 == 0:
        visited[value] = solution(value//2) + 1
    else:
        visited[value] = solution(value+1) +1
    return visited[value]

# init

visited[1] = 0
visited[2] = 1
psum[0] = 0
psum[1] = 0
psum[2] = 1
for i in range(3, 1000001):
    psum[i] = psum[i-1] + solution(i)

for t in range(0, T):
    a,b = map(int,input().split())
    Answer = psum[b] - psum[a-1]
    print('Case #%d' % (int(t) + 1))
    print(Answer)

