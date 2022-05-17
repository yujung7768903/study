def solution(board, dir):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    x, y = 1, 1
    plan = dir.split()
    for i in plan:
        if i == 'U' and x > 1:
            x, y = x + dx[0], y + dy[0]
        elif i == 'R' and x < int(board):
            x, y = x + dx[1], y + dy[1]
        elif i == 'D' and x < int(board):
            x, y = x + dx[2], y + dy[2]
        elif i == 'L' and x > 1:
            x, y = x + dx[3], y + dy[3]

    return f"{x} {y}"

n = input()
s = input()
print(solution(n, s))