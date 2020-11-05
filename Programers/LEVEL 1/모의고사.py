def solution(answers):
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = cnt2 = cnt3 = 0
    for i in range(len(answers)):
        if man1[i % len(man1)] == answers[i]:
            cnt1 += 1
        if man2[i % len(man2)] == answers[i]:
            cnt2 += 1
        if man3[i % len(man3)] == answers[i]:
            cnt3 += 1
    tmp = [[1, cnt1], [2, cnt2], [3, cnt3]]
    tmp = sorted(tmp, key=lambda x: x[1], reverse=True)
    return [L[0] for L in tmp if L[1] == max(cnt1, cnt2, cnt3)]