# y를 제거한 버전
import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, value, x):
        self.value = value
        self.L = None
        self.R = None
        self.x = x


class Tree:
    def __init__(self, value, x):
        self.head = Node(value, x)
        self.pre = []
        self.post = []

    def insert(self, value, x):
        pointer = self.head
        while True:
            if x < pointer.x:
                if pointer.L == None:
                    pointer.L = Node(value, x)
                    return
                pointer = pointer.L
            elif x > pointer.x:
                if pointer.R == None:
                    pointer.R = Node(value, x)
                    return
                pointer = pointer.R

    def preorder(self, pointer:Node):
        if pointer == None:
            return
        self.pre.append(pointer.value)
        self.preorder(pointer.L)
        self.preorder(pointer.R)

    def postorder(self, pointer:Node):
        if pointer == None:
            return
        self.postorder(pointer.L)
        self.postorder(pointer.R)
        self.post.append(pointer.value)


def solution(nodeinfo):
    ret = []
    for i, L in enumerate(nodeinfo):
        ret.append([L[0], L[1], i + 1])  # X, Y, value
    ret.sort(key=lambda x: (-x[1], x[2]))
    tree = Tree(0, 1000000)  # 최촛값
    for L in ret:
        tree.insert(L[2],L[0])
    tree.preorder(tree.head)
    tree.postorder(tree.head)
    return [tree.pre[1:],tree.post[:-1]]
print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))