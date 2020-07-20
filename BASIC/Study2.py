
#여러 줄 한번에 쓰기
multiline="""
TEST ECHO
1 2 3
"""
print(multiline)

testStr = "Life is Good"
print(testStr[0:4])
'''
ERROR CASE1
testStr2 = "ABCD"
testStr2[0] = 'B'
'''
print("ERROR IS %d"%98)

testStr3 = "i eat {0} applies"
print(testStr3.format(10))

testStr4 = "i eat {number} applies"
print(testStr4.format(number=30))

#f문자열 포맷팅 사용법
name = "홍길동"
age = 30
testStr5 = f"나의 이름은 {name}입니다, 나이는 {age+1}입니다"
print(testStr5)

#문자열 캐스팅 함수

testStr6 = str(123)
testStr6 += str(1)
print(testStr6)



#리스트에서 특정 문자열 찾아내기
some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']

    #길게 쓰면
for s in some_list:
    if "abc" in s:
        print("있다")
        break; #하나만 찾으면 뒤는 안 찾음


    #짧게 쓰면
if any("abc" in s for s in some_list):
    print("있다")


#특정 문자열을 포함하는 문자열 출력하기
some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']

#길게 쓰면
resultlist = []
for s in some_list:
    if "abc" in s:
        resultlist.append(s)

#짧게 쓰면
matching = [s for s in some_list if "abc" in s]

print (matching)

a = [1,2,3]
b = [4,5]
print(a+b)