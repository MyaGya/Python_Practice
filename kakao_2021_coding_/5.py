from collections import defaultdict


def solution(play_time, adv_time, logs):
    # 경우의 수를 계산하는 방법으로 풀이
    # 1. 시간 변경 후 나열
    watch = defaultdict(int)
    new_logs = [0]
    for S in logs:
        S = S.split('-')
        start = int(S[0][0:2]) * 3600 + int(S[0][3:5]) * 60 + int(S[0][6:8])
        end = int(S[1][0:2]) * 3600 + int(S[1][3:5]) * 60 + int(S[1][6:8])
        watch[start] += 1
        watch[end] -= 1
        new_logs.append(start)
        new_logs.append(end)
    new_logs.append(int(play_time[0:2]) * 3600 + int(play_time[3:5]) * 60 + int(play_time[6:8]))
    new_logs.sort()
    adv_time = int(adv_time[0:2]) * 3600 + int(adv_time[3:5]) * 60 + int(adv_time[6:8])

    history = []  # 재생시간/ 시작시간
    # 2. 해당 지점에서 시작할 경우 / 끝날 경우의 수를 모두 기록
    now_watch = 0  # 현재 시청자 수
    for i in range(len(new_logs)):  # 모든 지점을 반복하면서 광고 시청 시간을 기록한다
        now_watch += watch[new_logs[i]]  # 해당 지점에서의 기본 시청자 수 갱신
        start = new_logs[i]
        end = start + adv_time
        sum_watch_time = 0
        sum_watch_people = now_watch
        for j in range(i + 1, len(new_logs)):  # 시청자 수 변경 지점마다 계산
            if new_logs[j] < end:  # 종료시점 이전에 시청자 수가 변경될 경우
                sum_watch_time += (new_logs[j] - start) * sum_watch_people  # 시청자 수 만큼 광고시간 합산
                sum_watch_people += watch[new_logs[j]]  # 시청자 수 갱신
                start = new_logs[j]  # 그 시점에서 다시 계산
            else:
                sum_watch_time += (end - start) * sum_watch_people  # 시청자 수 만큼 광고시간 합산
                history.append([sum_watch_time, new_logs[i]])  #
                break
        else:  # for문이 끝났을 경우 더 이상 확인할 필요가 없다
            break
    MAX = max(L[0] for L in history)  # 최댓값
    # 그 지점에서의 최대 수
    for L in history:
        if L[0] == MAX:
            h, m = divmod(L[1], 3600)
            m, s = divmod(m, 60)
            return str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)


print(solution("02:03:55", "00:14:15",
               ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                "01:37:44-02:02:30"]))
