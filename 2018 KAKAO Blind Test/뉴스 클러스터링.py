# 미완성, 정규표현식 연습

import re
from collections import defaultdict
# 2개의 입력값
def solution(str1, str2):
    List1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if 'a'<=str1[i].lower()<='z' and 'a'<= str1[i+1].lower() <= 'z']
    List2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if 'a'<=str2[i].lower()<='z' and 'a'<= str2[i+1].lower() <= 'z']

    
    cmpBase = defaultdict(int)
    for s in List1:
        cmpBase[s] += 1
    for s in List2:
        cmpBase[s] += 1
    intersection = [s for s in cmpBase.items() if s[1] >= 2]
    try:
        return int((len(intersection) / len(cmpBase)) * 65536)
    except ZeroDivisionError:
        return 65536


print(solution("aa1+aa2","AAAA12"))