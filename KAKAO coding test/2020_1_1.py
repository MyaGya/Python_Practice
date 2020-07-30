#문제 형식을 따르지 않았음.

def solution(data, length):
    #문자열 자르기
    newdata = [data[i:i+length] for i in range(0,len(data),length)]
    print(newdata[0])
    count = 0
    prev = 0
    result = str()
    for i in range(len(newdata)):
        if newdata[i] == newdata[prev]:
            count+=1
        else:
            if count == 1:
                result+= str(newdata[prev])
            else:
                result+= str(count) + str(newdata[prev])
            prev = i
            count = 1
    if count == 1:
        result += str(newdata[prev])
    else:
        result += str(count) + str(newdata[prev])
    return len(result)

data = input()

#반복
Min = 1000
for i in range(1, (len(data)//2)+2):
    Min = min(Min, solution(data,i))

print(Min)
