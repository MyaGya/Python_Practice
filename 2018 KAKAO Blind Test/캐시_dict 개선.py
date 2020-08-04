from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    citiList = deque()
    citiList_dict = dict()
    time = 0
    for s in cities:
        s = s.lower()
        # 도시가 이미 리스트에 있는 경우
        if citiList_dict.get(s) != None:
            time += 1
            del citiList[citiList.index(s)]
            del citiList_dict[s]
            citiList.append(s)
            citiList_dict[s] = 1
        else:
            time += 5
            # 도시가 리스트에 없고 배열이 다 차지 않은 경우
            if len(citiList) < cacheSize:
                citiList.append(s)
                citiList_dict[s] = 1
            # 배열이 다 찬 경우
            else:
                del citiList_dict[citiList.popleft()]
                citiList.append(s)
                citiList_dict[s] = 1
    return time

n = int(input())
cities = list(input().split())
print(solution(n,cities))