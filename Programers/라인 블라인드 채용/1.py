from collections import defaultdict

def solution(boxes):
    check_box = defaultdict(int)
    for L in boxes:
        check_box[L[0]] += 1 # 박스 0번의 수
        check_box[L[1]] += 1 # 박스 1번의 수
    # check_box가 짝수인 수는 값을 알아서 찾아 갈 수 있다
    check_box = list({i:check_box[i] for i in check_box if check_box[i] % 2 == 1}) # 짝수 제거
    return len(check_box) //2

print(solution([[1,2],[2,3],[3,10],[5,11]]))