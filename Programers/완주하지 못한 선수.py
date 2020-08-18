from collections import defaultdict
def solution(participant, completion):
    participantList = defaultdict(int)
    for s in participant:
        participantList[s] += 1
    for s in completion:
        participantList[s] -= 1
        if participantList[s] == 0:
            del participantList[s]
    return  list(participantList.keys())[0]




print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))
