import time, random

# 정렬된 List에서 값 찾기

data_set = [i for i in range(100002)]
for _ in range(1000000):
    a, b = random.randrange(0,100000), random.randrange(0,100000)
    data_set[a],data_set[b] = data_set[b],data_set[a]


start = time.time()
if 100001 in data_set:
    print('test')
end = time.time()
print(end-start)
data_set.sort()

start = time.time()
if 100001 in data_set:
    print('test')
end = time.time()
print(end-start)