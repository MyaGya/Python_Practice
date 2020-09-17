def solution(n, t, m, timetable):
    # 1. change time
    c_time = sorted([int(s[:2]) * 60 + int(s[-2:]) for s in timetable],reverse=True)

    # 2. check bus : 가장 마지막 버스를 타고 가면 된다
    cur_time = 540  # 09:00
    for _ in range(n):  # n번 운행
        for _ in range(m):  # m명의 사람을 태울 수 잇다
            if c_time and c_time[-1] <= cur_time :  # 기다리는 사람이 있는 경우
                ret = c_time.pop() - 1  # 기다리는 사람보다 1분만 빨리 오면 된다
            else:  # 기다리는 사람이 없을 경우 해당 버스가 오는 시간에만 오면 된다
                ret = cur_time
        cur_time += t  # 다음 버스가 오는 시간

    time, minute = divmod(ret,60)

    return str(time).zfill(2) + ":" + str(minute).zfill(2)

print(solution(2,10,2,['09:10', '09:09', '08:00']))