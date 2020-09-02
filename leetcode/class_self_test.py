class TEST:
    def __init__(self):
        self.value = 1

    def Solution(self):
        print(id(TEST))
        self.value += 1

    def Solution2(self):
        print(id(TEST))
        self.value += 10


USER = TEST()
print(id(USER))
print(id(USER.Solution()))
print(id(USER.Solution2()))
print(USER.value)


# sorting test
a = [[1,'a'],[2,'b'],[2,'c'],[2,'a'],[1,'d'],[1,'f'],[1,'g']]
sorted(a, key=lambda x: (x[1]))
print(a)