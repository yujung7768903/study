import sys
from itertools import combinations
import copy

def bfs(room, virus):
    virus_zone = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while virus:
        x, y = virus.pop()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
                room[nx][ny] = 2
                virus_zone += 1
                virus.append((nx, ny))

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
    print(lab)
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
        print(f"========= 벽 위치: {comb} =========")
        room = copy.deepcopy(lab)
        for k, j in comb:
            room[k][j] = 1
        safe_zone_num = zero_num - bfs(room, copy.deepcopy(list_virus_pos))
        print(f"🔰안전한 곳의 개수: {safe_zone_num}")
        if safe_zone_num > answer: answer = safe_zone_num

    return answer
    

n, m = map(int, sys.stdin.readline().split())
print(solution())