import heapq
def solution(food_times, k):
    food_list = []
    for i,food in enumerate(food_times):
        heapq.heappush(food_list,[food,i+1])
    lazy = 0
    while food_list:
        food_list[0][0] -= lazy
        use_time = ((food_list[0][0]) * len(food_list))
        k -= use_time
        if k < 0: # 값 복원 후 빠져나감
            k += use_time
            break
        lazy += food_list[0][0] # 몇 바퀴를 돌았는가?
        heapq.heappop(food_list)
    if not food_list: # 예외처리
        return -1
    food_list.sort(key=lambda x:x[1])
    k %= len(food_list)
    return food_list[k][1]


print(solution([3,1,5],5))