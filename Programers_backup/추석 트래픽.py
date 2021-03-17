def solution(lines):
    logs = []
    for line in lines:
        _, end, time = line.split()
        h,m,s = end.split(":")
        end = (int(h)*60*60 + int(m) * 60 + float(s))*1000
        logs.append((end-float(time[:-1])*1000+1, end)) # include start_time

    ret = 1
    for i in range(len(logs)):
        cnt = 1
        for j in range(i+1, len(logs)):
            if logs[j][1] - logs[i][1] >= 4001: # max timeOut 3000 + 1000
                break
            if logs[j][0] - logs[i][1] < 1000:
                cnt += 1
        ret = max(ret, cnt)
    return ret


print(solution([
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]))