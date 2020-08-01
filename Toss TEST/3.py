from collections import deque

data = input().split()

box = deque()

for s in data:
    # 데이터가 없는 경우
    if s not in box:
        if len(box) < 5:
            box.append(s)
        # 크기 5개 이하
        else:
            box.popleft()
            box.append(s)
    # 데이터가 있는 경우
    else:
        # 삭제 후 맨 뒤로 재편셩
        for i in range(len(box)):
            if box[i] == s:
                break
        del box[i]
        box.append(s)
    tmp = ""
    for s in reversed(box):
        tmp += s +" "
    print(tmp[0:-1])