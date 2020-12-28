def solution(routes):
    ### init ###
    routes.sort(key=lambda x: x[0])
    camera = routes[0][1]
    R = 30000
    ret = 0
    ### solution ###
    for Lst in routes:
        if R < Lst[0]:
            ret += 1
            R = Lst[1]
        else:
            R = min(R, Lst[1])
    return ret + 1