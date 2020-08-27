import heapq

### init ###
parent = [i for i in range(110)]
### find ###
def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]


### merge ###
def merge(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return
    parent[u] = v

def solution(n, costs):
    island = []
    ret = 0
    # heap 구현
    for L in costs:
        heapq.heappush(island,(L[2],L)) # 정렬기준 L2



    ### solution ###
    while 0 < len(island):
        garbage, L = heapq.heappop(island)
        u = find(L[0])
        v = find(L[1])
        if u != v: # 부모가 다른 경우
            merge(u,v)
            ret += L[2]
    return ret
print(solution(4,  [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]))