'''
def solution(brown, yellow):
    nm = brown + yellow
    for n in range(1, nm+1):
        if nm%n != 0:
            continue
        m = nm//n
        if (n-2)*(m-2) == yellow:
            return sorted([n, m], reverse = True)
'''

def solution(brown, yellow):
    xy = brown + yellow
    for tmp_x in range(1, xy + 1):  # tmp x
        if yellow % tmp_x == 0:
            tmp_y = yellow // tmp_x
            if tmp_y * 2 + tmp_x * 2 + 4 == brown:
                return sorted([tmp_x+2, tmp_y+2], reverse=True)


print(solution(10,2))