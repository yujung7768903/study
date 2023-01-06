from collections import deque

def bfs(room, x, y):
    print(f"bfs({x}, {y})")
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    que = deque()
    que.append((x, y, 0))
    visited = [(x, y)]

    while que:
        print(que)
        x, y, cost = que.popleft()
        if cost == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visited:
                print(f"({nx}, {ny} 방문: 값: {room[nx][ny]})")
                if room[nx][ny] == 'P':
                    print("❌")
                    return False
                elif room[nx][ny] == 'O':
                    que.append((nx, ny, cost + 1))
                    visited.append((nx, ny))
    
    print("⭕️")
    return True


def solution(places):
    answer = []
    for index, place in enumerate(places):
        result = True
        print(f"=== {index + 1}번 방 ===")
        for i in range(5):
            print(f"i: {i}")
            for j in range(5):
                if place[i][j] == 'P':
                    result = bfs(place, i, j)
                if not result:
                    break
            if not result:
                break
        if not result:
            answer.append(0)
        else:
            answer.append(1)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))