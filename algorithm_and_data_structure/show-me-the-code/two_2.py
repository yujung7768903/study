import time
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(que):
    while len(que) > 0:
        startX, startY = que.popleft()
        graph[startX][startY] = '1'
        for i in range(4):
            nextX = (startX + dx[i]) % n
            nextY = (startY + dy[i]) % m
            if graph[nextX][nextY] == '0':
                que.append([nextX, nextY])

n, m = map(int, input().split())
graph = []
cnt = 0
for i in range(n):
    graph.append(input().split(" "))

startTime = time.time()
for x in range(n):
    for y in range(m):
        if graph[x][y] == '0':
            que = deque([[x, y]])
            bfs(que)
            cnt += 1

print(cnt)

print(f"총 소요 시간: {time.time() - startTime}")