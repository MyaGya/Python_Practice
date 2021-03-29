def solution(n, stations, w):
    modify_w = w * 2 + 1

    ret = 0
    start = 0
    stations.append(n + w + 1)  # last
    for station in stations:
        end = station - w - 1
        ret += (end - start) // modify_w + 1 if (end - start) % modify_w > 0 else (end - start) // modify_w
        start = station + w
    return ret