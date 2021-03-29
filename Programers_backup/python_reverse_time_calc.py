import time


data = [i for i in range(10000000)]
start = time.time()
data[::-1]
end = time.time()
print(end - start)
start = time.time()
data2 = reversed(data) # 미리 객체로만 만들어 놨다가 사용할 때 할당한다
end = time.time()
print(end - start)
start = time.time()
data.reverse()
end = time.time()
print(end - start)
print('='*50)
data = "abc"*1000
start = time.time()
data2 = data[::-1] # 문자열을 직접 다룰려면 이 방법밖에 없다. 이 외에는 리스트로 쪼개고 합쳐야 하며 시간복잡도가 많이 발생한다.
end = time.time()
print(end - start)

