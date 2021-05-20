def solution(lottos, win_nums):
    lotto_score = {}
    lotto_score[6] = 1
    lotto_score[5] = 2
    lotto_score[4] = 3
    lotto_score[3] = 4
    lotto_score[2] = 5
    lotto_score[1] = 6
    lotto_score[0] = 6

    score = 0
    num_zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            score += 1
        if lotto == 0:
            num_zero += 1

    return [lotto_score[score + num_zero], lotto_score[score]]
