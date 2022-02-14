import sys
from collections import deque

que = deque()

n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    que.append(i + 1)

select_num = list(map(int, sys.stdin.readline().split()))

cal_num = 0

while select_num:
    if select_num[0] == que[0]:
        que.remove(select_num[0])
        select_num.remove(select_num[0])
        print(f"1번 연산 수행 / que: {que}")
    elif que.index(select_num[0]) <= (len(que) - 1) - que.index(select_num[0]):
        que.append(que.popleft())
        cal_num += 1
        print(f"2번 연산 수행 / que: {que}")
    else:
        que.appendleft(que.pop())
        cal_num += 1
        print(f"3번 연산 수행 / que: {que}")

print(f"정답: {cal_num}")