# 1. 트라이 사용
class Node:
    def __init__(self):
        self.count = 0
        self.child = dict()


class Tri:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        pointer = self.head
        for c in word:
            # 값이 없는 경우
            if c not in pointer.child:
                pointer.child[c] = Node()
            pointer = pointer.child[c]
            # 분기 추가
            pointer.count += 1

    def search(self, word):
        pointer = self.head
        ret = 0
        for c in word:
            pointer = pointer.child[c]
            ret += 1
            if pointer.count == 1:
                break
        return ret
def solution(words):
    answer = 0
    Tree = Tri()
    for s in words:
        Tree.insert(s)
    for s in words:
        answer += Tree.search(s)
    return answer

data = input().split(',')
print(solution(data))