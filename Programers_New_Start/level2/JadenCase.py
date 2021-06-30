def solution(s):
    sliced_s = s.split(" ")
    ans = []
    for case in sliced_s:
        ans.append(case.capitalize())
    return " ".join(ans)


print(solution("3people unFollowed me"))