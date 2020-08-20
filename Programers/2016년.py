def solution(a, b):
    # 2016년 1월 1일은 금요일
    date = ["THU", 'FRI', "SAT", "SUN", "MON", "TUE", "WED"]
    Month31 = [1, 3, 5, 7, 8, 10, 12]
    Month30 = [4, 6, 9, 11]
    cnt = 0
    for i in range(1, a):
        if i in Month31: cnt += 31
        elif i in Month30: cnt += 30
        else: cnt += 29
    return date[(cnt + b) % 7]

print(solution(6, 1))