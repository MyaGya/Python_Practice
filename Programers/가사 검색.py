import sys
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self):
        self.child = {}


class Tree:
    def __init__(self):
        self.head = Node()  # head의 최촛값은 0이다
        self.history = {}
    def insert(self, s):  # s : string
        pointer = self.head
        for ch in s:
            if ch in pointer.child:
                pointer = pointer.child[ch]
            else:
                pointer.child[ch] = Node()
                pointer = pointer.child[ch]
        pointer.child['end'] = Node()  # 문장의 종료를 알림

    def find(self, s, start: int, end: int, pointer: Node):  # pointer
        if start == end:
            if 'end' in pointer.child:  # 끝일 경우
                return 1  # 값에 1 추가
            else:
                return 0  # 아닐경우 매칭 실패

        if s[start] == '?':  # ?의 경우
            ret = 0
            for i in pointer.child:
                ret += self.find(s, start + 1, end, pointer.child[i])  # 해당 포인터로 이동하여 값 체크
            return ret
        else:
            if s[start] in pointer.child:  # 값이 있으면 리턴

                return self.find(s, start + 1, end, pointer.child[s[start]])
            else:
                return 0

        return pointer.find(s, start + 1, end, )


def solution(words, queries):
    tree = Tree()
    for s in words:
        tree.insert(s)

    ret = []
    check = dict()
    for s in queries:
        if s in check:
            ret.append(check[s])
        else:
            check[s] = tree.find(s,0,len(s),tree.head)
            ret.append(check[s])
    return ret


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))