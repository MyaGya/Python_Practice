import heapq

# heap구조의 stability 성질이 유지되는지 확인하는것을 목표로 한다

data = []

t = 0
for i in range(0, 10):
    heapq.heappush(data, [-6, i])
for i in range(0, 10):
    heapq.heappush(data, [-1, i])
for i in range(0, 10):
    heapq.heappush(data, [-0, i])
for i in range(0, 10):
    heapq.heappush(data, [-2, i])
for i in range(0, 10):
    heapq.heappush(data, [-4, i])
for i in range(0, 10):
    heapq.heappush(data, [-5, i])
for i in range(10, 20):
    heapq.heappush(data, [-6, i])
for i in range(20, 30):
    heapq.heappush(data, [-6, i])
for i in range(40, 50):
    heapq.heappush(data, [-6, i])

for i in range(30, 40):
    heapq.heappush(data, [-6, i,i%i+2])
for i in range(30, 40):
    heapq.heappush(data, [-6, i,i%i+1])
while len(data):
    print(heapq.heappop(data))