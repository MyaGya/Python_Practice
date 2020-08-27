def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 4, reverse=True)
    return str(int(''.join(numbers)))

print(solution([3,30,34,5,9]))
