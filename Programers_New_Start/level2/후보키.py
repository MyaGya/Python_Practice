def solution(relation):
    def is_powerset(parent, child):
        return parent | child == parent

    n_attr = len(relation[0])
    candidate_key = []

    for key in range(1, 1 << n_attr):
        # 현재까지 찾은 후보키을 부분집합으로 가지지 않는지를 먼저 판단
        print(1 >> 2)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
