# 2 튜플 표현하기
# set을 쓰기에는 중복된 원소가 발생한다.
# 중복되는 원소가 있는지 없는지 모르겠다, 문제에 중의적으로 적혀있어!
def solution(s):
    data = []
    tmp = []
    tmp = ("".join((s[:-2].split("{")))).split("},")
    for line in tmp:
        data.append(line.split(","))

    data = sorted(data, key=lambda x: len(x))
    # 차집합 출력
    result = []
    result.append(data[0])
    for i in range(len(data) - 1):
        tmp1 = set(data[i])
        tmp2 = set(data[i + 1])
        result.append(list(tmp2 - tmp1))
    result = [int(s[0]) for s in result]
    return result


s = input()
print(solution(s))