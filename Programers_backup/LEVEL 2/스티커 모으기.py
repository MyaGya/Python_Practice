def solution(sticker):
    if len(sticker) == 1: # 예외처리
        return sticker[0]
    dp_start0 = [0 for _ in range(len(sticker))]
    dp_start1 = [0 for _ in range(len(sticker))]

    dp_start0[0] = sticker[0]
    dp_start0[1] = max(sticker[0],sticker[1])
    dp_start1[0] = 0
    dp_start1[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp_start0[i] = max(dp_start0[i-2] + sticker[i],dp_start0[i-1])
        dp_start1[i] = max(dp_start1[i-2] + sticker[i],dp_start1[i-1])
    return max(dp_start0[-2],dp_start1[-1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))