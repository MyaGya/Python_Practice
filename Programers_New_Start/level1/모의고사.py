def solution(answers):
    user1 = [1, 2, 3, 4, 5]
    user2 = [2, 1, 2, 3, 2, 4, 2, 5]
    user3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    user1_point = 0
    user2_point = 0
    user3_point = 0

    for i in range(len(answers)):
        if answers[i] == user1[i % len(user1)]:
            user1_point = user1_point + 1
        if answers[i] == user2[i % len(user2)]:
            user2_point = user2_point + 1
        if answers[i] == user3[i % len(user3)]:
            user3_point = user3_point + 1
    result = [[1, user1_point], [2, user2_point], [3, user3_point]]
    result.sort(key=lambda x: x[1])
    return [L[0] for L in result if L[1] == max(user1_point, user2_point, user3_point)]


print(solution([1, 2, 3, 4, 5]))
