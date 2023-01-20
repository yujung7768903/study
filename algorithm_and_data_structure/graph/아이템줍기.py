# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [[0 for _ in range(102)] for _ in range(102)]
def solution(rectangleList, characterX, characterY, itemX, itemY):
    for rectangle in rectangleList:
        for y in range(2 * rectangle[1] + 1, 2 * rectangle[3]):
            for x in range(2 * rectangle[0] + 1, 2 * rectangle[2]):
                graph[x][y] = 1

    que = deque([[2 * characterX, 2 * characterY, 0]])
    while len(que) > 0:
        print(f"que: {que}")
        x, y, cnt = que.popleft()
        graph[x][y] = 2
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if (0 < nextX <= 100) and (0 < nextY <= 100) and graph[nextX][nextY] == 0 and isAvailable(nextX, nextY):
                if nextX == 2 * itemX and nextY == 2 * itemY:
                    return int((cnt + 1) / 2)
                que.append([nextX, nextY, cnt + 1])

def isAvailable(startX, startY):
    for nx, ny in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        if graph[startX + nx][startY + ny] == 1:
            return True

    return False

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
print(solution(rectangle, 1, 3, 7, 8))
