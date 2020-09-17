def solution(info, query):
    # 무조건 앞에서부터 쿼리가 들어간다 또한 조건은 5개로 고정된다
    '''
    순서는 다음과 같다
    0 : JAVA / 1: python / 2. cpp / 3. -
    0 : backend / 1: frontend
    0 : junior / 1 senior
    0 : pizza / 1 chicken
    score는 그때그때 해석한다
    '''
    info = [s.split() for s in info]

    reference_data_A = ['java', 'python', 'cpp', '-']
    reference_data_B = ['backend', 'frontend', '-']
    reference_data_C = ['junior', 'senior', '-']
    reference_data_D = ['pizza', 'chicken', '-']
    # 1. 미리 경우의 수를 계산한다
    ans = dict()  # 최종 일치 인원
    A_data = [i for i in range(len(info))]  # 최초에는 모든 인원이 포함된다
    for A in range(4):  # 언어
        B_data = []
        if A == 3:
            B_data = A_data
        else:
            for i in A_data:
                if reference_data_A[A] == info[i][0]:  # 조건 만족
                    B_data.append(i)
        for B in range(3):  # 직군
            C_data = []
            if B == 2:
                C_data = B_data
            else:
                for i in B_data:
                    if B == 2 or reference_data_B[B] == info[i][1]:
                        C_data.append(i)
            for C in range(3):  # 경력
                D_data = []
                if C == 2:
                    D_data = C_data
                else:
                    for i in C_data:
                        if C == 2 or reference_data_C[C] == info[i][2]:
                            D_data.append(i)
                for D in range(3):  # 음식
                    last_data = []
                    if D == 2:
                        last_data = D_data
                    else:
                        for i in D_data:
                            if D == 2 or reference_data_D[D] == info[i][3]:
                                last_data.append(i)
                    ans[(
                    reference_data_A[A], reference_data_B[B], reference_data_C[C], reference_data_D[D])] = last_data

    # query 에 따른 결과를 가져온다
    query = [s.split() for s in query]
    ret_count = 0
    ret = []
    for L in query:
        ret_count = 0
        cmp = int(L[7])
        for i in ans[(L[0], L[2], L[4], L[6])]:
            if int(info[i][4]) >= cmp:  # 점수가 더 높은 사람이 있는 경우
                ret_count += 1
        ret.append(ret_count)
    return ret


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	))