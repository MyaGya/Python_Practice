def solution(s: str):
    translate_digit = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
                       "seven": "7", "eight": "8", "nine": "9"}
    answer = ""

    expected_digit_sentence = ""
    for c in s:
        if c.isdigit():
            answer += c
            continue

        if expected_digit_sentence + c in translate_digit:
            answer += translate_digit[expected_digit_sentence + c]
            expected_digit_sentence = ""
            continue
        expected_digit_sentence += c

    return int(answer)


print(solution("one4seveneight"))
