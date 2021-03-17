def solution(n,cores):
    answer = 0
    min = 10001

    for i in cores:
        if min > i:
            min = i

    minTime = n / len(cores) * min
    maxTime = n * min
    midTime = (minTime + maxTime) / 2

    while(minTime < maxTime):
        count = 0
        availableCount = 0
        for i in cores:
            count += (midTime / i) + 1;
            if(midTime % i == 0):
                availableCount += 1
                count += 1



        if(count >= n):
            maxTime = midTime
        elif(count + availableCount < n):
            minTime = midTime+1
        else:
            for i in range(len(cores)):
                if midTime % cores[i] == 0:
                    count += 1

                if (count == n):
                    return i+1
        midTime = (minTime + maxTime) / 2

    return answer

print(solution(6,[6,6,6]))
