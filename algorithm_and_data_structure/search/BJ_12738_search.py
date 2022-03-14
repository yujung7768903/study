import sys
from collections import deque

n = int(sys.stdin.readline())
list_num = list(map(int, sys.stdin.readline().split()))

deq = deque()
max_lengh = 0

# 시간 초과
# for i in range(1, n):
#     print(f"=== i : {i} ===")
#     deq_element = []
#     deq_element.append(list_num[i - 1])
#     if i < (n - max_lengh):
#         for j in list_num[i:]:
#             print(f"j : {j}")
#             if deq_element[-1] < j:
#                 deq_element.append(j)
#         if max_lengh < len(deq_element):
#             max_lengh = len(deq_element)

print(max_lengh)