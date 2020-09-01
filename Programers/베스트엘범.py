from collections import defaultdict
def solution(genres, plays):
    # 최대 빈도 앨범명 탐색
    data = defaultdict(int)
    for i in range(len(genres)):
        data[genres[i]] += plays[i]
    rank = sorted(data.items(), key=lambda x: x[1], reverse=True)
    # 랭크 정보를 data에 삽입
    for i in range(len(rank)):
        data[rank[i][0]] = i
    print(data)
    # zip을 이용하여 엘범 데이터를 병합
    number = [i for i in range(len(genres))]
    total_data = sorted(list(zip(genres, plays, number)), key= lambda x: (data[x[0]],-x[1]))
    # 최종 결과 리스트
    ret = []
    name = ""
    for L in total_data:
        if name != L[0]:
            cnt = 1
            name = L[0]
            ret.append(L[2])
        else:
            if cnt < 2:
                ret.append(L[2])
                cnt += 1
    return ret

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))
