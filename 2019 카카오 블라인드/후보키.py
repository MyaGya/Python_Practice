from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))


def solution(relation):
    n, m = len(relation), len(relation[0])
    ## key_candi를 만드는 작업
    key_candi = []
    for key in powerset(range(m)):
        aset = set()
        for i in range(n):
            aset.add(tuple(relation[i][j] for j in key))
        if len(aset) == n: key_candi.append(key)

    ## key_candi2를 만드는 작업
    key_candi2 = []
    for i in range(len(key_candi) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if set(key_candi[i]) & set(key_candi[j]) == set(key_candi[j]):
                key_candi2.append(key_candi[i])
                break
    return len(key_cd) - len(key_cd2)






print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))