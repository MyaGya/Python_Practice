def solution(brown, yellow):
    yellow_count = 1
    total = brown + yellow
    for width in range(1, yellow + 1):
        if yellow % width == 0:
            height = yellow // width
            example_total = 4 + height * 2 + width * 2 + width * height
            if example_total == total:
                return [height + 2, width + 2]


print(solution(10, 2))
