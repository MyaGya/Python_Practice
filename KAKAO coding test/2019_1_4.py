table = dict()

def solution(k, room_number):
    global table
    ans = []
    for number in room_number:
        tmp = []
        while table.get(number) is not None:
            tmp.append(number)
            number = table[number]
        ans.append(number)
        table[number] = number+1
        for i in range(len(tmp)):
            table[tmp.pop()] = number+1
    return ans


k = int(input())
room_number = list(map(int, input().split()))

print(solution(k, room_number))