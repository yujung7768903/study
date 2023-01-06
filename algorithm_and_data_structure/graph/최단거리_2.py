# 정확성: 39.8
# 효율성: 7.5
# 합계: 47.4 / 100.0
import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(maps):
    stack = [[0,0]]
    while len(stack) > 0:
        newStack = []
        for i in range(len(stack)):
            startX, startY = stack.pop()
            print(f"startX: {startX}, startY: {startY}, stack: {stack}")
            if startX == len(maps) - 1 and startY == len(maps[0]) - 1:
                return maps[startX][startY]
            for i in range(4):
                newX = startX + dx[i]
                newY = startY + dy[i]
                if newX < 0 or newX >= len(maps) or newY < 0 or newY >= len(maps[0]):
                    continue
                if maps[newX][newY] == 1:
                    maps[newX][newY] = maps[startX][startY] + 1
                    newStack.append([newX, newY])
                    print(f"    newStack: {newStack}")
                    printMap(maps)
        stack = newStack

    return -1


def printMap(maps):
    for map in maps:
        print(f"    {map}")
    print()

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,1,1],[1,1,1],[1,1,1]]

print(solution(maps))
