#딕셔너리 자료형 선언 및 사용
a = dict()
a = {1: "a"}
a[2] = 'b'

b = sorted(a.values())
print(b)


#키값으로 리스트는 사용 불가(변할 수 있음) 튜플은 사용 가능하다

a = {(1,2): "Hi"}

print (a[(1,2)])


#dict.values(), dict.keys(), dict.items()로 요소들 전체를 가져 올 수 있다.

print(a.get((0))) # None를 출력함으로써 에러로 멈추지 않게 한다

if((1,2) in a):
    print("TRUE")

#중복을 허용하지 않는 set, 집합연산시 사용. 중복시킨다음에 값을 넣어준다

tmp = [5, 3, 1, 76, 3948200000000000]
#tmp = set(tmp)
sorted(tmp)
tmp = set(tmp)
tmp = sorted(tmp)
print(tmp)




#주솟값 체크


a = [1, 2, 3, 4]
print(id(a))
b = a
print(id(a))

b.append(5)
print(a)



#스왑 swap
c = [1, 2, 3, 4]
d = [5, 6, 7, 8]

print("ID C :"+str(id(c)))
print("ID D :"+str(id(d)))
if(c == d):
    print("TRUE")
    
#실제 스왑 부분
c,d = d,c
print(c)

#c = d[:]
#print(c)
#print("ID C :"+str(id(c)))
#print("ID D :"+str(id(d)))

