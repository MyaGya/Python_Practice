def solution(sticker):
    dp_start0 = []
    dp_start1 = []

    dp_start0[0] = sticker[0]
    dp_start0[1] = sticker[1]
    dp_start1[0] = 0
    dp_start1[1] = sticker[1]
    for i in range(2, len(stickers)):
        dp_start0[i] = dp_