from collections import Counter
from collections import deque


def solution(priorities, location):
    data = Counter(priorities)
    priorities = deque(priorities)
    max_waiting = max(priorities)
    ans = 0

    while not (location == 0 and max_waiting == priorities[location]):
        if max_waiting == priorities[0]:  # case pop
            priorities.popleft()
            data[max_waiting] -= 1
            ans += 1
            if data[max_waiting] == 0:  # make max_waiting
                del data[max_waiting]
                max_waiting = max(data.keys())
        else:
            priorities.append(priorities.popleft())

        location -= 1
        if location == -1:
            location = len(priorities) - 1

    return ans + 1
