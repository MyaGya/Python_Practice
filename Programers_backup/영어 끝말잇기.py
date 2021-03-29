def solution(n, words):
    history = {words[0]:True}
    for i in range(1,len(words)):
        if (words[i][0] != words[i-1][-1]) or words[i] in history:
            return [i%n+1,i//n+1]
        else:
            history[words[i]] = True
    else:
        return [0,0]