# 같은 음 반복
def solution(n):
    return "수박" * (n // 2) + "수" if n % 2 == 1 else "수박" * (n // 2)
