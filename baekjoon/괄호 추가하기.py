
def dfs(L:list):
    if len(L) == 1:
        global ans
        ans = max(ans, int(L[0]))
        return

    for i in range(0, len(L)-1, 2):
        new_L = []
        for j in range(i):
            new_L.append(L[j])

        if L[i+1] == '+':
            new_L.append(int(L[i]) + int(L[i+2]))
        elif L[i+1] == '-':
            new_L.append(int(L[i]) - int(L[i + 2]))
        else:
            new_L.append(int(L[i]) * int(L[i + 2]))

        for j in range(i+3,len(L)):
            new_L.append(L[j])
        dfs(new_L)


ans = -10**10
n = int(input())
s = input()
L = list(s)

dfs(L)
print(ans)