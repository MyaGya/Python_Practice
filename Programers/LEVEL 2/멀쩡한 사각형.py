import math
def solution(w,h):
    #전체 사각형 - (겹치는 지점이 없을 경우 제외 사각형의 크기 w + h 에서 겹치는지점인 gcd(w,h)를 뺸 위치
    answer = w*h - (w + h - math.gcd(w,h))
    return answer