import sys

n = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))
list_nge = [-1] * n
stack_index = []

for i in range(len(list_a)):
    while stack_index and list_a[stack_index[-1]] < list_a[i]:
        list_nge[stack_index[-1]] = list_a[i]
        stack_index.pop()
    stack_index.append(i)

print(*list_nge)