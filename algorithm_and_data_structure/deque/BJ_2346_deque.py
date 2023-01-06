import sys
from collections import deque

# 풍선이 원형으로 둘러져있음
# 1터트림 -> 이동 -> 터트림 -> 반복
# 양수 오른쪽, 음수 왼쪽 이동

n = int(sys.stdin.readline())
list_value = deque(map(int, sys.stdin.readline().split())) # 풍선 종이에 적힌 수
list_index = deque([i + 1 for i in range(n)]) # 풍선 번호

result = []
result.append(list_index.popleft())
balloon_number = list_value[0]

while len(result) < n:
    balloon_number = list_value[result[-1] - 1]
    if balloon_number > 0:
        print(f"balloon_number = {balloon_number}")
        for i in range(balloon_number - 1):
            list_index.append(list_index.popleft())
            print(f"풍선: {list_index}")
        result.append(list_index.popleft())
        print(f"결과: {result}")
    else:
        print(f"balloon_number = {balloon_number}")
        for j in range(-1 * (balloon_number + 1)):
            list_index.appendleft(list_index.pop())
            print(f"풍선: {list_index}")
        result.append(list_index.pop())
        print(f"결과: {result}")

print(*result)
