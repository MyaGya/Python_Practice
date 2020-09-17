def calcNeed(data, need_number, i): # 실제로 필요한 값
    ret = need_number[i]
    for check_i in range(0,i):
        if data[check_i]:
            data[check_i] -= 1
            ret -= need_number[check_i]
    return ret


def solution(data: list, need_number:dict, start):
    i = 0
    end = len(data)-1
    while end > 0:
        if i < len(data) and data[i]: # 해당 값이 있는 경우
            data[i] -= 1
        else:       # 해당 값이 없는 경우
            need = calcNeed(data,need_number,i)
            for j in range(end,-1,-1): # 뒤로 탐색
                if need <= data[j]: # 데이터가 충분할경우
                    data[j] -= need
                    break
                else:                           # 데이터가 충분하지 않을 경우
                    need -= data[j]
                    end -= 1
        i+=1
    return i-1


N = int(input())

refer = list(map(int, input().split()))
# include
need_number = dict()
need_number[0] = 1
need_number[1] = 1

for i in range(2, 10001):
    need_number[i] = need_number[i - 1] * 2

data = [0 for _ in range(100010)]
for i in range(len(refer)):
    data[i] = refer[i]
if data.count(0) == N-1:
    for i in range(len(data)):
        if data[i] != 0:
            print(i if i != 0 else 1)
else:
    print(solution(data,need_number, 0))

