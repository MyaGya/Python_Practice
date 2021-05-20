def solution(numbers, target):
    answer = 0

    def bfs(index, max_length, sum_numbers):
        if index == max_length:
            nonlocal answer
            if sum_numbers == target:
                answer += 1
            return

        sum_numbers += numbers[index]
        bfs(index + 1, max_length, sum_numbers)
        sum_numbers -= numbers[index]
        sum_numbers -= numbers[index]
        bfs(index + 1, max_length, sum_numbers)
        sum_numbers += numbers[index]

    bfs(index=0, max_length=len(numbers), sum_numbers=0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
