import sys

# 풍선이 원형으로 둘러져있음
# 1터트림 -> 이동 -> 터트림 -> 반복
# 양수 오른쪽, 음수 왼쪽 이동
# [2, 1, -3, -1]
# [-1, 2, 1]
#

n = int(sys.stdin.readline())
list_value = list(map(int, sys.stdin.readline().split()))

