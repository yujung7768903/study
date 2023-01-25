maxCnt = 0
def solution(k, dungeons):
    dfs(k, dungeons, 0)
    return maxCnt

def dfs(k, dungeons, cnt):
    global maxCnt
    if cnt > maxCnt:
        maxCnt = cnt
    for dungeon in dungeons:
        remainDungeons = dungeons.copy()
        remainDungeons.remove(dungeon)
        if k >= dungeon[0]:
            dfs(k - dungeon[1], remainDungeons, cnt + 1)




dungeons = [[80,20],[50,40],[30,10]]


print(solution(80, dungeons))