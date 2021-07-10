def solution(numbers, hand):
    expected_left_finger_list = {1: [0, 0], 4: [1, 0], 7: [2, 0]}
    expected_right_finger_list = {3: [0, 2], 6: [1, 2], 9: [2, 2]}
    unknown_hand = {2: [0, 1], 5: [1, 1], 8: [2, 1], 0: [3, 1]}

    left_finger = [3, 0]
    right_finger = [3, 2]
    answer = ""

    def move_left_finger(next_position):
        nonlocal answer
        nonlocal left_finger
        answer += "L"
        left_finger = next_position

    def move_right_finger(next_position):
        nonlocal answer
        nonlocal right_finger
        answer += "R"
        right_finger = next_position

    for number in numbers:
        if number in expected_left_finger_list:
            move_left_finger(expected_left_finger_list[number])
        elif number in expected_right_finger_list:
            move_right_finger(expected_right_finger_list[number])
        else:
            left_finger_distance = abs(unknown_hand[number][0] - left_finger[0]) + \
                                        abs(unknown_hand[number][1] - left_finger[1])
            right_finger_distance = abs(unknown_hand[number][0] - right_finger[0]) + \
                                    abs(unknown_hand[number][1] - right_finger[1])

            if left_finger_distance > right_finger_distance:
                move_right_finger(unknown_hand[number])
            elif left_finger_distance < right_finger_distance:
                move_left_finger(unknown_hand[number])
            else:
                if hand == "right":
                    move_right_finger(unknown_hand[number])
                else:
                    move_left_finger(unknown_hand[number])

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
