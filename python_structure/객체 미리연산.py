import time

start = time.time()
print("배열을 만드는 데 걸리는 시간 : ", end=" ")
data = [i for i in range(100000)]
end = time.time()
print(end - start)

start = time.time()
print("배열을 출력하는 데 걸리는 시간 : ", end=" ")
print(data)
end = time.time()
print(end - start)


# map 연산을 걸리는 시간
start = time.time()
print("map 연산 시간 : ", end=" ")
data2 = map(str,data)
end = time.time()
print(data2)
print(end - start)

# 그렇다면 객체 데이터 내부를 모두 바꾸어도 map 연산에는 문제가 없을까?

start = time.time()
print("리스트 값을 일부분 변경시키는 데 걸리는 시간 : ", end=" ")
for i in range(10000):
    data[i] = "XXX"
end = time.time()
print(end - start)

start = time.time()
print("원본 데이터를 변경한 후 값을 출력하는 데 걸리는 시간 : ", end=" ")
print(list(data2))
end = time.time()
print(end - start)
# 이로써 원본 데이터가 바뀌면 map리스트가 가리키고 있는 명령어는 바뀐 명령어로 실행됨을 알 수 있다.
# 따라서 따로 원본 데이터의 객체를 저장하는 것이 아닌 포인터 방식으로 가리키고 있음을 알 수 있다.
