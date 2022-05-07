# 시간 초과
from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_que1 = sum(queue1)
    sum_que2 = sum(queue2)
    if (sum_que1 + sum_que2) % 2 == 1: # 두 개의 큐의 원소의 합이 홀수인 경우
        return -1
    one_que_sum = (sum_que1 + sum_que2) // 2
    print(f"각 원소는 {one_que_sum}이 되어야 함")
    while sum(queue1) != sum(queue2):
        print("===================")
        print(f"queue1: {queue1}, sum_que1: {sum(queue1)}")
        print(f"queue2: {queue2}, sum_que2: {sum(queue2)}")
        if sum(queue1) < sum(queue2):
            add_item = queue2.popleft()
            if add_item > one_que_sum:
                return -1
            queue1.append(add_item)
            answer += 1
        else:
            add_item = queue1.popleft()
            if add_item > one_que_sum:
                return -1
            queue2.append(add_item)
            answer += 1
    
    return answer

# ex1
ex1_que1 = [3, 2, 7, 2]
ex1_que2 = [4, 6, 5, 1]
print(solution(ex1_que1, ex1_que2))
# ex1
ex1_que1 = [1, 2, 1, 2]
ex1_que2 = [1, 10, 1, 2]
print(solution(ex1_que1, ex1_que2))
# ex3
ex1_que1 = [1, 1]
ex1_que2 = [1, 5]
print(solution(ex1_que1, ex1_que2))