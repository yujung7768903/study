import sys
from collections import deque

n = int(sys.stdin.readline().strip())
que = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    que.append((x, y))

que = sorted(que)

# for i in range(len(que)):
#     print(f"=== i: {i} ===")
#     for j in range(len(que) - i - 1):
#         if que[j][0] > que[j + 1][0]:
#             que[j], que[j + 1] = que[j + 1], que[j]
#         elif que[j][0] == que[j + 1][0]:
#             if que[j][1] > que[j + 1][1]:
#                 que[j], que[j + 1] = que[j + 1], que[j]
#         print(que)
                
for i in que:
    print(f"{i[0]} {i[1]}")