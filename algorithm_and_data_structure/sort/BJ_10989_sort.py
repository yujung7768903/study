# 메모리 제한으로 인해 계수정렬로 풀어야함

import sys

n = int(sys.stdin.readline())

list_num = []
count = [0] * 10001

for i in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(len(count)):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
