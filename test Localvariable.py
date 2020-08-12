import copy
def Function1(data):
    print(f"Function1 Data : {data}")
    print(f"Function1 ID : {id(data)}")
    data.append(2)
    Function2(data)

def Function2(data):
    print(f"Function2 Data : {data}")
    print(f"Function2 ID : {id(data)}")
    data.append(3)



data = [1]
Function1(data)

print(data)


print("="*50)
a = [[1,2], [3,4]]

b = copy.copy(a)

#a[0] = [5,6]
#a[1] = [7,8]
a[0].append(10)
print(a)
print(b)


print(id(1))
print(id(1))
print(id(1))