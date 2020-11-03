from itertools import permutations, product, combinations
# 순열과 조합을 구하는 대표 코드를 기술한다

Data = [1, 2, 3, 4]
# 순서를 상관쓰는 순열
tmp = list(permutations(Data, 2))
print (tmp)

# 순서가 상관없는 순열

tmp = list(combinations(Data, 2))
print(tmp)

# 다중리스트를 한번에 조합

tmp = [["a","b","c"],['1','2','3'],["가","나","다"]]
tmp = list(product(*tmp))
print(tmp)


# 2~4명의 주자로 이루어진 달리기 대회 랭킹을 보여주는 함수
def save_ranking(first, second, third=None, fourth=None):
    rank = {}
    rank[1], rank[2] = first, second
    rank[3] = third if third is not None else 'Nobody'
    rank[4] = fourth if fourth is not None else 'Nobody'
    print(rank)

# positional arguments 2개 전달
save_ranking('ming', 'alice')
# positional arguments 2개와 keyword argument 1개 전달
save_ranking('alice', 'ming', third='mike')
# positional arguments 2개와 keyword arguments 2개 전달 (단, 하나는 positional argument 형태로 전달)
save_ranking('alice', 'ming', 'mike', fourth='jim')