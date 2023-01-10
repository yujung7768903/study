# 문제: 백준 2606번 바이러스
# 문제 링크: https://www.acmicpc.net/problem/2606

n = int(input())
m = int(input())

numDict = {key: [] for key in range(n + 1)}
visited = []

for _ in range(m):
    a, b = map(int, input().split(" "))
    numDict[a].append(b)
    numDict[b].append(a)

def dfs(start):
    visited.append(start)
    for next in numDict[start]:
        if not next in visited:
            dfs(next)

dfs(1)
print(len(visited) - 1)