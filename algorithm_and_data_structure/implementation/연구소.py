# 시간초과
import sys
from itertools import combinations
from collections import deque
import copy

def bfs(room, virus):
    virus_zone = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    que = deque()
    visited = []
    for i in virus:
        que.append(i)
        while que:
            x, y = que.popleft()
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0 and (nx, ny) not in visited:
                    que.append((nx, ny))
                    visited.append((nx, ny))
                    virus_zone += 1
                    print(f"que: {que}")
                    print(f"visited: {visited}")

    print(f"🚫바이러스가 퍼진 곳 개수: {virus_zone}")
    return virus_zone

def solution():
    zero_num = 0
    answer = 0
    lab = []
    list_virus_pos = []
    list_0_pos = []
    for i in range(n):
        lab_low = list(map(int, sys.stdin.readline().split()))
        lab.append(lab_low)

    for j in range(n):
        for k in range(m):
            if lab[j][k] == 2:
                list_virus_pos.append((j, k))
            elif lab[j][k] == 0:
                list_0_pos.append((j, k))
                zero_num += 1
    
    # 벽 3개 가능한 조합
    comb_new_wall = list(combinations(list_0_pos, 3))
    zero_num -= 3
    for comb in comb_new_wall:
        room = copy.deepcopy(lab)
        for k, j in comb:
            room[k][j] = 1
        safe_zone_num = zero_num - bfs(room, list_virus_pos)
        print(f"🔰안전한 곳의 개수: {safe_zone_num}")
        if safe_zone_num > answer: answer = safe_zone_num
        print(answer)

    return answer
    

n, m = map(int, sys.stdin.readline().split())
print(solution())