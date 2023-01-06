col = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

input_value = input()
x = int(input_value[1])
y = col[input_value[0]]
print(x, y)

def solution():
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + (2 * dx[i])
        ny = y + (2 * dy[i])
        for j in [-1, 1]:
            rx = nx + dx[(i + j) % 4]
            ry = ny + dy[(i + j) % 4]
            if 0 < rx < 9 and 0 < ry < 9:
                answer += 1
    
    return answer

print(solution())