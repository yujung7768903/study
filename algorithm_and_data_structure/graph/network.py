visited = []

def solution(n, computers):
    answer = 0
    for number, info in enumerate(computers):
        if number not in visited:
            dfs(number, computers)
            answer += 1

    return answer

def dfs(start, computers):
    visited.append(start)
    for next, status in enumerate(computers[start]):
        if next not in visited and status == 1:
            dfs(next, computers)

computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(3, computers))