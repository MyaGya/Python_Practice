N = int(input())

for i in range(1,(N//2)+1):
    if N % i == 0:
        print(i, end=" ")
print(N)