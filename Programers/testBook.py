import heapq, random
# 목표. 힙에도 stability 성질이 적용되는지 확인하려 한다.


number = []
for i in range(100):
    tmp = random.randrange(1,100)
    tmp2 = random.randrange(1, 100)
    number.append((i, tmp, tmp2))
    tmp = random.randrange(1, 100)
    tmp2 = random.randrange(1, 100)
    number.append((i, tmp, tmp2))
random.shuffle(number)

#number = sorted(number,key = lambda x : x[1])

print(number)
heapq.heapify(number)
print(number)

while len(number):
    print(heapq.heappop(number))




heapq.heappush(number,1)
heapq.heappush(number,1)
heapq.heappush(number,1)


# replace Test

test = "A V DD g f H bn o ,. d"
print(test)

test = test.replace(" ","")
print(test)

Cond = [1,2,3]



items = [['a', 'b', 'c,'], ['1', '2', '3', '4'], ['!', '@', '#']]
print(*items)


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 4, reverse=True)
    return str(int(''.join(numbers)))

print(solution([3,30,34,5,9]))

data = [(1,2), (2,3),(3,4), (5,10), (10,5)]
data.sort(key = lambda x : x[1] - x[0])
print(data)


# Counter
from collections import Counter
clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
print([a + 1 for a in Counter([x[1] for x in clothes]).values()])


def A():

    def B():
        return 2
    return 1


