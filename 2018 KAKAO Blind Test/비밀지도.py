def solution(n, arr1, arr2):
    ans = []
    tmp = [bin(value)[2:] for value in (arr1[i] | arr2[i] for i in range(n))]
    for i in tmp:
        s = '0' * (n-len(i)) + i
        s = s.replace('1','#')
        s = s.replace('0',' ')
        ans.append(s)
    return ans



print(solution(6,[46,33,33,22,31,50],[27,56,19,14,14,10]))