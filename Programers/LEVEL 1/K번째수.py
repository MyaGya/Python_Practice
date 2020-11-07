def solution(array, commands):
    ret = []
    for command in commands:
        ret.append(sorted(array[command[0]-1:command[1]])[command[2]-1])
    return ret