from operator import itemgetter

def solution(n, build_frame):
    pillar = dict()
    beam = dict()
    for s in build_frame:
        # 삭제의 경우
        if s[3] == 0:
            if s[2] == 0:
                del pillar[s[0], s[1]]
            elif s[2] == 1:
                del beam[s[0], s[1]]
        # 삽입의 경우
        else:
            if s[2] == 0:
                pillar[s[0], s[1]] = 0
            elif s[2] == 1:
                beam[s[0], s[1]] = 1
    result1 = []
    result2 = []
    for s in pillar.items():
        result1.append([s[0][0], s[0][1], s[1]])
    for s in beam.items():
        result1.append([s[0][0], s[0][1], s[1]])
    result1 = sorted(sorted(result1, key=itemgetter(1)), key=itemgetter(0))
    result2 = sorted(sorted(result2, key=itemgetter(1)), key=itemgetter(0))
    print(result1)



n = int(input())
data = []
for _ in range(8):
    data.append(list((map(int, input().split()))))

solution(n, data)
