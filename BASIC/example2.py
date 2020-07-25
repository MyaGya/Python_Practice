class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


'''
Calculator를 상속
뺄셈 기능 확장
'''


class UpgradeCalculator(Calculator):
    def sub(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.sub(7)

print(cal.value)


# Q2
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if (self.value > 100):
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# Q3

L1 = [1, -2, 3, -5, 8, -3]
L = list(filter(lambda x: x >= 0, L1))
print(L)

print(int(hex(234), 16))

# 06
L1 = [1, 2, 3, 4]
L = list(map(lambda x: x * 3,L1))
print(L)

# 08
print(round(17/3, 4))

#1000미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라
Max = 1000
result = [s for s in range(1,1000) if s % 3 == 0 or s % 5 == 0]

print(sum(result))