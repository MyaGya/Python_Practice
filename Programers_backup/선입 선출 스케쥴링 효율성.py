def solution(n, cores):
    answer = 0
    L = 0
    R = max(cores) * n
    while L<=R:
        midtime = (L+R)//2
        complete_number = len(cores)
        available_complete_number = 0
        for core in cores:
            complete_number += midtime //core
            if midtime % core == 0:
                available_complete_number+= 1

        if n > complete_number:
            L = midtime +1
        elif n <= complete_number - available_complete_number:
            R = midtime -1
        else:
            count = 0
            for i in range(len(cores)):
                if midtime % cores[i] == 0:
                    count += 1
                    if count == n - (complete_number - available_complete_number):
                        return i + 1

print(solution(6, [6,6,6]))