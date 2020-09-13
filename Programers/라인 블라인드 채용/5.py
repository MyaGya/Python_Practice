from itertools import combinations


def sum_user(user_list:list): # 유저 배열이 가질 수 있는 값
    data = []
    for value in user_list:
        if value == 1:
            data.append(1)
            data.append(11)
        else:
            data.append(value)
    tmp = list(combinations(data,len(user_list)))

    ret = []
    for L in tmp:
        ret.append(sum(L))
    return ret #


def solution(cards):

    for i in range(len(cards)): # J Q K 치환
        if cards[i] >10:
            cards[i] = 10



    i = 0
    ret = 0
    while i < len(cards):
        player_card = []
        dealer_card = []
        if i + 4 <= len(cards):
            # 1. 카드를 한 장 뽑아 플레이어에게 준다
            player_card.append(cards[i])
            # 2. 딜러가 카드를 뽑아 뒤집어 보인다
            dealer_card.append(cards[i+1])
            # 3. 플레이어에게 카드를 준다
            player_card.append(cards[i+2])
            # 4. 딜러가 앞에 보이게 카드를 보인다
            dealer_card.append(cards[i+3])
            # 5. 플레이어에게 카드를 받을지 물어본다
        else:
            return ret
        i+=4

        if 21 in sum_user(player_card): # 플레이어 합계에 21이 있을 경우
            if 21 in sum_user(dealer_card) : # 딜러의 합계에 21이 있을 경우 비긴다
                ret += 0 # 비김
                continue
            else:
                ret += 3 # 블랙잭 승리
                continue

        # 조건 1 1이거나 7 이상일 경우

        flag2 = True
        flag = False
        while (dealer_card[1] == 1 or dealer_card[1] >= 7):
            player_point = 0
            player_list = sum_user(player_card)
            for player in player_list: # 모든 경우의 수를 순회하면서
                if 17 <= player <= 21 : # 플레이어가 17 이상의 수를 확보했을 경우
                    player_point = max(player,player_point) # 해당 점수를 기록한다
            if player_point > 0:
                break
            for player in player_list: # 모든 점수가 21점 이상일 경우
                if player <=21:
                    flag = False
            if flag: # 패배한다
                ret -= 2
                flag = True
                break
            for player in player_list: # 모든 점수가 17점 이하일 경우
                if player < 17:
                    flag2 = True
                else:
                    flag2 = False
            if flag2: # 모든 점수가 17점 이하인 경우
                if i < len(cards): # 카드를 뽑을 수 있다면
                    player_card.append(cards[i])
                    i +=1
                else: # 카드를 뽑을 수 없다면
                    flag = True
        if flag: # 게임에서 졌거나 카드를 뽑을 수 없는 경우 조건을 확인한다
            continue

        # 조건 2
        player_point = 0
        flag2 = True
        flag = False
        while dealer_card[1] == 2 or dealer_card[1] == 3: # 딜러의 카드가 2 or 3 인 경우
            flag = True
            player_list = sum_user(player_card)
            for player in player_list: # 모든 경우의 수를 순회하면서
                if 12 <= player <= 21 : # 플레이어가 12 이상의 수를 확보했을 경우
                    player_point = max(player,player_point) # 해당 점수를 기록한다
            if player_point > 0:
                break
            for player in player_list: # 모든 점수가 21점 이상일 경우
                if player <=21:
                    flag = False
            if flag: # 패배한다
                ret -= 2
                flag = True
                break
            for player in player_list: # 모든 점수가 17점 이하일 경우
                if player < 12:
                    flag2 = True
                else:
                    flag2 = False
            if flag2: # 모든 점수가 17점 이하인 경우
                if i < len(cards): # 카드를 뽑을 수 있다면
                    player_card.append(cards[i])
                    i +=1
                else: # 카드를 뽑을 수 없다면
                    flag = True
        if flag: # 게임에서 졌거나 카드를 뽑을 수 없는 경우 조건을 확인한다
            continue




        # 딜러 조건 1 1이거나 7 이상일 경우

        flag2 = True
        flag = False
        while True:
            dealer_point = 0
            dealer_list = sum_user(dealer_card)
            for dealer in dealer_list: # 모든 경우의 수를 순회하면서
                if 17 <= dealer <= 21 : # 플레이어가 17 이상의 수를 확보했을 경우
                    dealer_point = max(dealer,dealer_point) # 해당 점수를 기록한다
            if dealer_point > 0:
                break
            for dealer in dealer_list: # 모든 점수가 21점 이상일 경우
                if dealer <=21:
                    flag = False
            if flag: # 패배한다
                ret += 2
                flag = True
                break
            for dealer in dealer_list: # 모든 점수가 17점 이하일 경우
                if dealer < 17:
                    flag2 = True
                else:
                    flag2 = False
            if flag2: # 모든 점수가 17점 이하인 경우
                if i < len(cards): # 카드를 뽑을 수 있다면
                    dealer_card.append(cards[i])
                    i +=1
                else: # 카드를 뽑을 수 없다면
                    flag = True
        if flag: # 게임에서 졌거나 카드를 뽑을 수 없는 경우 조건을 확인한다
            continue


        if player_point > dealer_point:
            ret += 2
        elif player_point < dealer_point:
            ret += -2
        else:
            ret += 0
    return ret

print(solution([12, 7, 11, 6, 2, 12]))