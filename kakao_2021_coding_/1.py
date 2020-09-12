def solution(new_id):
    # 1
    if new_id:
        new_id = new_id.lower()
    # 2
    if new_id:
        new_id = "".join([i for i in new_id
                          if i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.'])
    # 3
    if new_id:
        tmp = new_id[0]
        for i in range(1, len(new_id)):
            if tmp[-1] == '.' and new_id[i] == '.':
                continue
            tmp += new_id[i]
        new_id = tmp
    # 4
    if new_id:
        if new_id == '.':
            new_id = ''
        else:
            if new_id[0] == '.':
                new_id = new_id[1:]
            if new_id[-1] == '.':
                new_id = new_id[:-1]

    # 5
    if not new_id:
        new_id = 'a'

    # 6
    if 16 <= len(new_id):
        if new_id[14] == '.':  # 마지막이 .
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]

    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id