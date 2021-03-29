def solution(relation):
    def is_powerset(parent, child):
        return parent | child == parent


    n_attr = len(relation[0])
    candidate_key = []

    for key in range(1, 1 << n_attr):
        # 현재까지 찾은 후보키을 부분집합으로 가지지 않는지를 먼저 판단
        flag = False
        for e in candidate_key:
            if is_powerset(key, e):
                flag = True
                break
        if flag:
            continue

        # 현재 키가 유일성을 만족하는지를 판단
        sliced_relation = []
        for row in relation:
            sliced_row = []
            for j in range(0, n_attr):
                # print(bin(copied_key >> j))
                if (key >> j) & 1 == 1:
                    sliced_row.append(row[j])
            sliced_relation.append(tuple(sliced_row))

        if len(sliced_relation) != len(set(sliced_relation)):
            continue

        # 후보키 목록에 추가
        candidate_key.append(key)

    answer = len(candidate_key)
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))