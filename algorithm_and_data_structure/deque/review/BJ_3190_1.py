import sys
from collections import deque
import itertools

snake = deque([(1,1)]) # 머리가 맨 뒤

board_size = int(sys.stdin.readline())

# 사과
apple_num = int(sys.stdin.readline())
list_apple = []
# 사과의 위치
for i in range(apple_num):
    apple_x, apple_y = map(int, sys.stdin.readline().split())
    list_apple.append((apple_x, apple_y))

# 방향
turn_num = int(sys.stdin.readline())
list_turn_time = []
list_turn_dir = []
# 방향 변환 정보
for i in range(turn_num):
    turn_time, turn_dir = sys.stdin.readline().split()
    list_turn_time.append(int(turn_time))
    list_turn_dir.append(turn_dir)

def change_dir(dir, turn_dir):
    if turn_dir == "D":
        return (dir + 1) % 4
    else:
        return (dir - 1) % 4


live = True
time = 0
present_dir = 0 # right 0, down 1, left 2, up 3
while live == True:
    time += 1
    print(f"time: {time}")

    # 이동
    if present_dir == 0:
        snake.append((snake[-1][0], snake[-1][1] + 1))
    elif present_dir == 1:
        snake.append((snake[-1][0] + 1, snake[-1][1]))
    elif present_dir == 2:
        snake.append((snake[-1][0], snake[-1][1] - 1))
    if present_dir == 3:
        snake.append((snake[-1][0] - 1, snake[-1][1]))

    # 생사 확인
    if 1 <= snake[-1][0] <= board_size and 1 <= snake[-1][1] <= board_size and snake[-1] not in deque(itertools.islice(snake, 0, len(snake)-1)):
        # 사과 확인
        if snake[-1] in list_apple:
            print(f"🍎 {snake[-1]}위치에 있는 사과 먹음")
            list_apple.remove(snake[-1])
        else:
            snake.popleft()
        print(f"🐍: {snake}")

        # 방향 전환
        if time in list_turn_time:
            turn_index = list_turn_time.index(time)
            present_dir = change_dir(present_dir, list_turn_dir[turn_index])
            print(f"방향: {present_dir}")
    else:
        print(time)
        live = False