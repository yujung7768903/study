import sys
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

room = []
for i in range(n):
    room_row = list(map(int, sys.stdin.readline().split()))
    room.append(room_row)
    

def clean(row, col, dir, count):
    # 1번 단계
    if room[row][col] == 0:
        room[row][col] = 2
        count += 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # 2a번 단계
    for i in range(4):
        dir = (dir - 1) % 4
        nx = row + dx[dir]
        ny = col + dy[dir]
        if 0 < nx < n and 0 < ny < m and room[nx][ny] == 0:
            return clean(nx, ny, dir, count)
    nx = row + dx[((dir + 2) % 4)]
    ny = col + dy[((dir + 2) % 4)]
    # 2b번 단계
    if room[nx][ny] == 1:
        return count
    else:
        return clean(nx, ny, dir, count)
    
print(clean(r, c, d, 0))