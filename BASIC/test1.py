def tmp_test():
    return 1


#Q1. 평균 점수 구하기

Subject1=80
Subject2=75
Subject3=55
print("평균점수 %d"%((Subject1+Subject3+Subject2)/3))

#Q2. 자연수 13은 홀수인가 짝수인가?

number = 13
if number%2 == 1:
    print("홀수")
else:
    print("짝수")

#Q3. 주민등록번호 881120-1068234를 YYYYMMDD와 그 뒤로 나누어보자
registrationNumber = "881120-1068234"
registrationNumber1 = registrationNumber[:6]
registrationNumber2 = registrationNumber[7:]
print("Number1 : %s Number2 : %s"%(registrationNumber1,registrationNumber2))

#Q4. 성별 확인하기

if(registrationNumber[7:8] == "1"):
    print("남")
else:
    print("여")

#Q5. 문자열 에서 replace함수를 써서 바꾸기

a = "a:b:c:d"
a = a.replace(":", "#")
print(a)

#Q6. [1, 3, 5, 4, 2]리스트를 [5, 4, 3, 2, 1]로 만들어 보자

L = [1, 3, 5, 4, 2]
#L.reverse() or
L = list(reversed(L))
print(L)

L = ['Life', 'is', 'too', 'short']
#L = ' '.join(L)
#print(L) or
result = ""
for S in L:
    result = result + S + " "
print(result)

#08. (1,2,3)튜플에 값 4를 추가하여 (1,2,3,4)를 만들어보자, 괄호를 안 치는 경우에도 튜플로 지정된다ㅣ
tup = 1,2,3
tup += 4,
print(tup)

#09. 딕셔너리 관련 문제
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
#a[[1]] = 'python'<= 오류
a[250] = 'python'
print(a)
print(a[('a',)])

#10. 딕셔너리 a에서 B에 해당되는 값을 추출해 보자
a = {'A':90, 'B':80, 'C':70}
print(a['B'])
del(a['B'])
print(a)
#추가, A와 C의 값을 바꿔보자
a.update(A = a['C'], C = a['A'])
print(a)

#11. 리스트에서 중복 숫자를 제거해 보자
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(a)
print(set(a))

#Q.12
#a와 b는 함께 선언되어있다. 즉, 해당 문법은 뒤로 해석하여 b = 1,2,3이 되고 a가 그 값을 이어받는 구조와 동일하다. 따라서 Call by reference의 구조로 해석하는것이 옳다 
a = b = [1, 2, 3]
a[1] = 4
print(b)