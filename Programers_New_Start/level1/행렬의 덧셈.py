def solution(arr1, arr2):
    answer = [[0 for i in range(len(arr1[0]))] for i in range(len(arr1))]
    print(answer)
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer
