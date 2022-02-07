# import sys

# n_and_k = sys.stdin.readline().strip().split()
# n = int(n_and_k[0])
# k = int(n_and_k[1])

# del_check_list = [0] * n
# result = []
# present_num = 0

# def delete_k():
#     global present_num
#     for i in range(n):
#         count = 0
#         while count < k:
#             present_num += 1
#             if present_num > n:
#                 present_num = present_num % n
#             if del_check_list[present_num - 1] == 0:
#                 count += 1
#         result.append(present_num)
#         del_check_list[present_num - 1] = 1
#     print("<", end="")
#     for i in result:
#         if i != result[-1]:
#             print(i, end=", ")
#         elif i == result[-1]:
#             print(i, end="")
#     print(">")

# delete_k()


# 다른 방법
# 맨 앞의 값을 맨 뒤로 보내기(k - 1번 )
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
que = deque([i for i in range(1, n + 1)])
result = []

while que:
    for i in range(k - 1):
        que.append(que.popleft())
    result.append(que.popleft())

print("<", end="")
# int로는 join을 사용할 수 없음. str로 변경해야함
print(", ".join(map(str,result)), end="")
print(">")
