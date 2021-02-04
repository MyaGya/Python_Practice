def solution(s: str):
    delete_zero_count = 0
    loop_count = 0
    while s != "1":
        loop_count += 1
        delete_zero_count += s.count("0")
        s = "".join(["1" for i in range(s.count("1"))])
        s = bin(len(s))[2:]

    return [delete_zero_count, loop_count]


print(solution("110010101001"))
