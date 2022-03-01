import sys

# 시간이 가장 적게 걸리는 사람이 앞에 설 때 -> 최솟값

n = int(sys.stdin.readline())
list_time = list(map(int, sys.stdin.readline().split()))

list_time.sort()
result = 0

for i in range(n):
    result += list_time[i] * (n - i)

print(result)