# 문제 풀이 시간: 34.3s

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dirDict = {"U": 0, "R": 1, "D": 2, "L": 3}
graph = [[0 for _ in range(21)] for _ in range(21)]
graph[10][10] = 1

def solution(dirs):
    answer = 0
    x = 10
    y = 10
    for dir in dirs:
        for _ in range(2):
            if (x == 20 and dir == "U") or (x == 0 and dir == "D") or (y == 0 and dir == "L") or (y == 20 and dir == "R"): continue
            x += dx[dirDict[dir]]
            y += dy[dirDict[dir]]
            if graph[x][y] == 1: continue
            graph[x][y] = 1
            if x % 2 == 1 or y % 2 == 1: answer += 1

    return answer

# print(solution("ULURRDLLU")) # 정답 7
print(solution("LULLLLLLU")) # 정답 7
