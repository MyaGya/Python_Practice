def solution(numbers):
    numbers = list(map(str, numbers))
    return str(int("".join(sorted(numbers, key=lambda x: x * 4, reverse=True))))


print(solution([3,30,34,5,9]))
