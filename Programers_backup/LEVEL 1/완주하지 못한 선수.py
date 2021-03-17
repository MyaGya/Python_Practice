from collections import defaultdict
def solution(participant, completion):
    participant_list = defaultdict(int)
    for s in participant:
        participant_list[s] += 1
    for s in completion:
        participant_list[s] -= 1
        if participant_list[s] == 0:
            del participant_list[s]

    return list(participant_list.keys())[0]

print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))
