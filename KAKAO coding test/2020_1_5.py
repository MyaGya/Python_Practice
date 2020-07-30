from operator import itemgetter
class structure():
    def __init__(self,List):
        self.x = List[0]
        self.y = List[1]
        self.a = List[2]
        self.b = List[3]

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
                pillar[s[0], s[1]] = 1
            elif s[2] == 1:
                beam[s[0], s[1]] = 1
    pillar = list(pillar.items())
    beam = list(beam.items())

    print(pillar)
    print(beam)



n = int(input())
data = []
for _ in range(8):
    data.append(list((map(int, input().split()))))

solution(n,data)