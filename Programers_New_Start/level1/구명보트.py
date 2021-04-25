def solution(people, limit):
    people.sort()
    front_idx = 0
    answer = 0
    back_idx = len(people) - 1
    while (True):
        if front_idx > back_idx:
            break
        if front_idx == back_idx:
            answer += 1
            break

        if people[back_idx] + people[front_idx] <= limit:
            back_idx -= 1
            front_idx += 1
        else:
            back_idx -= 1
        answer += 1

    return answer
