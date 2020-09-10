def solution(numbers, hand):
    fingerL = [3,0]
    fingerR = [3,2]
    ret = ""
    for i in numbers:
        if i ==  1 or i ==4 or i==7:
            ret += 'L'
            if i == 1:
                fingerL = [0,0]
            elif i == 4:
                fingerL = [1,0]
            else:
                fingerL = [2,0]
        elif i ==3 or i==6 or i==9:
            ret += 'R'
            if i == 3:
                fingerR = [0,2]
            elif i == 6:
                fingerR = [1,2]
            else:
                fingerR = [2,2]
        else:
            dest = []
            if i == 2:
                dest = [0,1]
            elif i == 5:
                dest = [1,1]
            elif i == 8:
                dest = [2,1]
            else:
                dest = [3,1]
            lenL = abs(dest[1]-fingerL[1]) + abs(dest[0]-fingerL[0])
            lenR = abs(dest[1]-fingerR[1]) + abs(dest[0]-fingerR[0])
            if (lenL == lenR and hand == 'left') or (lenL<lenR):
                fingerL = dest
                ret += 'L'
            elif lenL == lenR and hand == 'right' or (lenL>lenR):
                fingerR = dest
                ret += 'R'

    return ret

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))