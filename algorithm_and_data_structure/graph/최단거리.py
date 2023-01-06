# 정확성: 28.6
# 효율성: 7.5
# 합계: 36.1 / 100.0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solution(maps):
    if isImpossible(maps, len(maps), len(maps[0])):
        return -1

    bfs(maps, [[0, 0]])
    return maps[-1][-1]

def bfs(maps, que):
    while len(que) > 0:
        startX, startY = que.pop()
        print(f"startX: {startX}, startY: {startY}")
        if startX == len(maps) - 1 and startY == len(maps[0]) - 1:
            break
        for i in range(4):
            newX = startX + dx[i]
            newY = startY + dy[i]
            if newX < 0 or newX >= len(maps) or newY < 0 or newY >= len(maps[0]):
                continue
            if maps[newX][newY] == 1:
                maps[newX][newY] = maps[startX][startY] + 1
                que.append([newX, newY])
                print(f"    que: {que}")
                printMap(maps)


def isImpossible(maps, h, w):
    if maps[h - 1][w - 2] == 0 and maps[h - 2][w - 1] == 0:
        return True
    return False


def printMap(maps):
    for map in maps:
        print(f"    {map}")

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))