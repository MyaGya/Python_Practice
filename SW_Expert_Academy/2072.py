
T = int(input())

for test_case in range(1, T+1):
    numberList = [s for s in map(int, input().split()) if s % 2 == 1]
    print("#%s %s"%(test_case, str(sum(numberList))))
