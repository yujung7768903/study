import sys

n = int(sys.stdin.readline())
list_num = []

for i in range(n):
    num = int(sys.stdin.readline())
    list_num.append(num)

for i in sorted(list_num):
    print(i)