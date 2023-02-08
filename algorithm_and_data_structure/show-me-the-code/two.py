dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(startX, startY):
    graph[startX][startY] = 1
    for i in range(4):
        nextX = (startX + dx[i]) % n
        nextY = (startY + dy[i]) % m
        if graph[nextX][nextY] == 0:
            dfs(nextX, nextY)

n, m = map(int, input().split())
graph = []
cnt = 0
for _ in range(n):
    graph.append(list(map(int, input().split(" "))))

for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            dfs(x, y)
            cnt += 1

print(cnt)