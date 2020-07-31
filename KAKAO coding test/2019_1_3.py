import itertools
# 불량 사용자
# 최대 8개의 데이터끼리 비교이기 때문에 단순비교로 문제를 해결한다

def check2(user, ban):
    for i in range(len(ban)):
        if ban[i] == '*':
            pass
        elif user[i] != ban[i]:
            return False
    return True

#banned_id는 다중리스트
def check1(user,banned_id):
    for i in range(len(banned_id)):
        if len(banned_id[i]) != len(user[i]):
            return False
        else:
            if check2(user[i], banned_id[i]) == False:
                return False
    return True

def solution(user_id, banned_id):
    # 후보 목록
    data = list(itertools.permutations(user_id, len(banned_id)))
    ans = []
    for user in data:
        if check1(user,banned_id) == True:
            new = set(user)
            if new not in ans:
                ans.append(new)
    return len(ans)
user_id = input().split()
banned_id = input().split()
print(solution(user_id,banned_id))
