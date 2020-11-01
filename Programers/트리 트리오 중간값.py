from collections import defaultdict, deque


def find_farthest(stack: deque, tree_dict, n):
    visited = [False for _ in range(n + 1)]
    while stack:
        start, depth = stack.popleft()
        visited[start] = True
        for i in tree_dict[start]:
            if visited[i]:
                continue
            stack.append((i, depth+1))
    return start,depth


def solution(n, edges):
    tree_dict = defaultdict(list)

    for edge in edges:
        tree_dict[edge[0]].append(edge[1])
        tree_dict[edge[1]].append(edge[0])

    # first step
    stack = deque()
    stack.append((1,0))
    start, _ = find_farthest(stack, tree_dict, n)

    # second step
    stack = deque()
    stack.append((start,0))
    end, depth = find_farthest(stack, tree_dict, n)

    return depth - 1

print(solution(5, [[1,5],[2,5],[3,5],[4,5]]	))
