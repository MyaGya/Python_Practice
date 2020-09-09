from itertools import combinations


def check_unique(L: [], relation: []) -> bool: # 유일성인지 확인한다
    tmp = []
    for i in L:
        tmp.append(relation[i])
    if len(set(zip(*tmp))) == len(relation[0]):  # set연산 후 지워지지 않을 경우(유일할 경우)
        return True
    else:
        return False


def check_dict(L,find_key): # 최소성인지 확인한다
    comb = []
    for i in range(1,len(L)):
        comb +=list(combinations(L,i))
    for cmp in comb:
        if cmp in find_key: # 값이 있는 경우
            return True
    return False
def solution(relation):
    possibility = []
    find_key = {}
    for i in range(1, len(relation[0]) + 1):  # 반복의 수
        possibility.append(list(combinations([d for d in range(len(relation[0]))], i)))
    relation = list(zip(*relation))
    ret = 0
    for L2 in possibility: # 경우 분할 1개일때, 2개일때 등
        for L in L2:# 모든 경우를 돌면서 확인
            if check_dict(L, find_key):
                continue
            else:  # 최소성 법칙을 위배하지 않을 경우 유일성 확인
                if check_unique(L, relation):  # 유일할경우 사전에 입력 진행
                    find_key[L] = True
                    ret += 1
    return ret


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))


test = 4
print(test)
print (1 << test)