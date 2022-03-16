# bfs 공부 필요

import sys

n = int(sys.stdin.readline())
paint = []
list_xy = []

for i in range(n):
    input_paint = list(sys.stdin.readline().strip())
    paint.append(input_paint)

paint_r = []
paint_g = []
paint_b = []

for i in range(n - 1):
    for j in range(n):
        if paint[i][j] == paint[i + 1][j]:
            if paint[i][j] == "R":
                paint_r.append
        if paint[i][j] == paint[i][j + 1]:
            

print(paint)