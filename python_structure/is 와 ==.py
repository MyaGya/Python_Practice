# 1000의 길이를 갖는 랜덤 문자열이 100000개가 모인 리스트에서 원하는 값을 찾는 데에 걸리는 is와 ==의 시간

import time
import random
data = []

start = time.time()
print("배열을 만드는 데 걸리는 시간 : ", end=" ")
for i in range(100000):
    tmp = ""
    for i in range(100):
        tmp += chr(random.randrange(ord('a'),ord('z')))
    data.append(tmp)
end = time.time()
print(end - start)


ans = data[99999]




start = time.time()
print("is를 사용해서 비교하는 시간 : ", end=" ")

for i in range(100000):
    if data[i] is ans:
        print("TEST")
end = time.time()
print(end - start)




start = time.time()
print("==을 사용해서 비교하는 시간 : ", end=" ")

for i in range(100000):
    if data[i] == ans:
        print("TEST")
end = time.time()
print(end - start)



