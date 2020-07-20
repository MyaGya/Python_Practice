
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