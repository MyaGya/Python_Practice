def solution(s):
    convert_result = 0
    delete_zero_count = 0
    loop_counter = 0
    while convert_result != 1:
        loop_counter += 1
        convert_result = s.count('1')
        delete_zero_count += s.count('0')
        s = bin(convert_result)[2:]

    return [loop_counter, delete_zero_count]


print(solution("110010101001"))
