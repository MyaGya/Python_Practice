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


print(List)