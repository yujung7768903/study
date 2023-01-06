# deque 사용

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(maps):
    deq = deque([[0,0]])
    while len(deq) > 0:
        startX, startY = deq.popleft()
        print(f"startX: {startX}, startY: {startY}, deq: {deq}")
        if startX == len(maps) - 1 and startY == len(maps[0]) - 1:
            return maps[startX][startY]
        for i in range(4):
            newX = startX + dx[i]
            newY = startY + dy[i]
            if newX < 0 or newX >= len(maps) or newY < 0 or newY >= len(maps[0]):
                continue
            if maps[newX][newY] == 1:
                maps[newX][newY] = maps[startX][startY] + 1
                deq.append([newX, newY])
                print(f"    deq: {deq}")
                printMap(maps)

    return -1


def printMap(maps):
    for map in maps:
        print(f"    {map}")
    print()

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,1,1],[1,1,1],[1,1,1]]

print(solution(maps))
