# 문제 풀이 시간: 약 40분

cnt = 0

def solution(n, wires):
    global cnt
    answer = -1
    numDict = {key: [] for key in range(1, n + 1)}
    for wire in wires:
        numDict[wire[0]].append(wire[1])
        numDict[wire[1]].append(wire[0])
    for removeWire in wires:
        cnt = 0
        visited = []
        dfs(removeWire[0], removeWire, numDict, visited)
        if answer == -1 or abs(n - 2 * cnt) < answer:
            answer = abs(n - 2 * cnt)
    return answer

def dfs(start, removeWire, numDict, visited):
    global cnt
    visited.append(start)
    cnt += 1
    for next in numDict[start]:
        if next not in visited and [start, next] != removeWire:
            dfs(next, removeWire, numDict, visited)

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(9, wires))