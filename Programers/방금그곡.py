'''
musicinfos 구성정보
음악 시작 시간, 끄탄 시간, 음악 제목, 악보 정보
'''
# 시간 계산
def calcTime(data1, data2):
    time1 = list(map(int,data1.split(":")))
    time2 = list(map(int,data2.split(":")))
    return int((time2[0] * 60 +time2[1]) - (time1[0] * 60 + time1[1]))

# 대치
def change(m):
    m = m.replace('A#', 'a')
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    return m
# 해답
def solution(m, musicinfos):
    answer = ['None', int(0)]
    m = change(m)
    for s in musicinfos:
        s = change(s)
        s = s.split(",")
        runningTime = calcTime(s[0], s[1])
        repeat = runningTime // len(s[3])
        # 실제 반복 배열
        running = s[3] * repeat + s[3][0:runningTime%len(s[3])]
        if m in running:
            # 실행시간이 더 긴 쪽이 정답
            if answer[1] < runningTime:
                answer[0] = s[2]
                answer[1] = runningTime

    if answer[1] == 0:
        return "(None)"
    else:
        return answer[0]

print(solution('ABC',['12:00,12:14,HELLO,C#', '13:00,13:05,WORLD,a']	))