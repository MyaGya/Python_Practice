def solution(phone_book):
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True

print(solution(['119', '97674223', '1195524421',"8888", "ab"]))
