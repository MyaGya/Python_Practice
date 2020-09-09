import copy
test1 = [1,2,3]
test2 = copy.copy(test1)
test3 = copy.deepcopy(test1)

print("각각의 id주소는 다음과 같다")
print(id(test1))
print(id(test2))
print(id(test3))

print("각각의 0번값의 주소는 다음과 같다")
print(id(test1[0]))
print(id(test2[0]))
print(id(test3[0]))


test1 = [[1,2],[2,3],[3,4]]
test2 = copy.copy(test1)
test3 = copy.deepcopy(test1)

print("각각의 id주소는 다음과 같다")
print(id(test1))
print(id(test2))
print(id(test3))

print("각각의 0번값의 주소는 다음과 같다")
print(id(test1[0]))
print(id(test2[0]))
print(id(test3[0]))

print("각각의 0번값의 값은 다음과 같다")
print((test1[0]))
print((test2[0]))
print((test3[0]))
'''
print("test1의 0번 값을 수정한 값은 다음과 같다")
test1[0] = 1
print((test1[0]))
print((test2[0]))
print((test3[0]))
'''
'''
print("test1의 0번 값을 수정한 값은 다음과 같다")
test1[0] = [1,2,3,4]
print((test1[0]))
print((test2[0]))
print((test3[0]))
'''
print("test1의 0번 값을 추가한 값은 다음과 같다")
test1[0].append(5)
print((test1[0]))
print((test2[0]))
print((test3[0]))

print("\\")

