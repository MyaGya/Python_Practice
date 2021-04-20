def solution(phone_book):
    history = {}
    phone_book.sort(key=lambda x: len(x))
    for number in phone_book:
        for i in range(1, len(number)):
            if number[0:i] in history:
                return False
        history[number] = True

    return True


print(solution(["12", "123", "1235", "567", "88"]))
