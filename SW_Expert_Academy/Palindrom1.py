#회문 1. 가장 파이썬스러운 공식을 사용
length = 8
data = []

def solve(n):
    total = 0
    for i in range (length):
        for j in range (length-n+1):
            List1 = list(data[i][j:j+n])
            if(List1 == List1[::-1]):
                total += 1
    return total

for testCase in range(1,11):
    n = int(input())
    total = 0
    for _ in range (length):

        data.append("".join(input().split()))

    total += solve(n)
    data = list(zip(*data))
    total += solve(n)
    data.clear()
    print("#{0} {1}".format(testCase, total))