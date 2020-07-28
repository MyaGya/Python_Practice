#파이썬의 정렬 방법에 대한 기초적인 방법을 알아보자
from operator import itemgetter,attrgetter

data = [1,5,3,7,9,0,54,30,29,10]


#1. 기본 출력
print("1: " + str(data))

#2. 오름차순 정렬
data.sort()
print("2: " + str(data))

#3. 내림차순 정렬
data = sorted(data, reverse=True)
print("3: " + str(data))

#4 다중 배열 관련 정리
student = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ('jung', 'C', 20),
    ('ami', 'D', 30)
]
#해당 배열을 숫자 기준으로, 점수 기준으로 새로 분류하려면
#정렬에는 안정성이 보장된다는 것을 기억하자. 여러 레코드가 같은 키를 가질 대 원래의 순서가 유지된다는 것
student = sorted(sorted(student,key=itemgetter(2)), key=itemgetter(1))
print(student)

#5 딕셔너리 정리

dict1 = {1:"TEST1", 2:"TEST2", 3:"TEST3", 5:"TEST5", 4:"TEST4"}
#dict1 = sorted(dict1.items())


print(dict1)