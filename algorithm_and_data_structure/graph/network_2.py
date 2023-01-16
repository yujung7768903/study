visited = []
def solution(n, computers):
    answer = 0
    for num in range(n):
        if num not in visited:
            dfs(num, computers)
            answer += 1
    return answer

def dfs(num, computers):
    visited.append(num)
    for nextNum, status in enumerate(computers[num]):
        if nextNum not in visited and status == 1:
            dfs(nextNum, computers)

# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(3, computers))