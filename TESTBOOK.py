import time


start = time.time()
data = [i for i in range(10000000)]
end = time.time()
print(end-start)



start = time.time()

data2 = map(str,data)
data[0] = 10

end = time.time()
print(end-start)

print(list(data2)[0])

