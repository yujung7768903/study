# import sys
# from collections import deque

# time = 0
# snake_pos = deque([(1, 1)]) # 꼬리가 맨 앞, 머리가 맨 뛰

# live = True
# #[o o o - - -] [1, 2] / [1, 4] / 3
# #[o - o - - -] [1, 3] / [2, 4] / 3
# #[o o o - - -] [1, 4] / [3, 4] / 3
# #[- - - - - -] [2, 4] / [4, 4] / 3 # 길이가 3인 뱀이 아래로 꺾으면 꼬리는 3초 후에 내려온다.
# #[- - - - - -] [4, 3]
# #[- - - - - -]
# # 3초 후 오른쪽으로 꺾는다고 할 때,
# # 머리입장: 3초 후 오른쪽으로 꺾음
# # 꼬리입장: (몸통 길이 - 1) 후 꺾음

# # 1 2 3 4 5 6 7 8 9 10 
# #[o - - - - - - - - - - - - - - - - - - -] 1
# #[- - - - - - - - - - - - - - - - - - - -] 2
# #[- - - - - - - - - - - - - - - - - - - -] 3
# #[- - + - - - - - - - - - - - - - - - - -] 4
# #[- - - - - - - - - - - - - - - - - - - -] 5
# #[- - - - - - - - + - - - - - + - - - - -] 6
# #[- - - - - - - - - + o o o - - - - + - -] 7
# #[- - - - - - - - - - o - o - - - - - - -] 8
# #[- - - - - - - - - - o - o - - - - - - -] 9
# #[- - - + - - - - - + o o o - - - - - - -] 10
# #[- - - - - - - - + - - - - - - - - - - -] 11
# #[- - - - - - - - - - - - - - - - - - - -] 12
# #[- - - - + - - - - - - - + - - - - - - -] 13
# #[- - - - - - - - - - - - + - - - - - - -] 14
# #[- - - - - - - - - - - - - - - - - - - -] 15
# #[- - - - - - - - - - - - - - - - - - - -] 16
# #[- - - - - - - - - - - - - - - - - - - -] 17
# #[- - - - - - - - - - - - - - - - - - - -] 18
# #[- - - - - - - - - - - - - - - - - - - -] 19
# #[- - - - - - - - - - - - - + - - - - - -] 20

# directions = ["up", "right", "down", "left"]
# dir_index = 1
# def turn_snake(dir):
#     global dir_index
#     # 방향 바꾸기
#     if dir == "L":
#         dir_index = (dir_index - 1) % 4
#     if dir == "D":
#         dir_index = (dir_index + 1) % 4

# # def move_snake(position, move_time):
# #     global live
# #     if snake_dir == "right":
# #         position[1] += move_time
# #     elif snake_dir == "left":
# #         position[1] -= move_time
# #     elif snake_dir == "up":
# #         position[0] -= move_time
# #     elif snake_dir == "down":
# #         position[0] += move_time

# def move_snake(dir):
#     global live
#     global snake_pos
#     head_pos = snake_pos[-1]
#     if dir == "right":
#         snake_pos.append((head_pos[0],head_pos[1] + 1))
#     elif dir == "left":
#         snake_pos.append((head_pos[0],head_pos[1] - 1))
#     elif dir == "up":
#         snake_pos.append((head_pos[0] - 1,head_pos[1]))
#     elif dir == "down":
#         snake_pos.append((head_pos[0] + 1,head_pos[1]))


# board_size = int(sys.stdin.readline().strip())

# apple_num = int(sys.stdin.readline().strip())
# apple_positions = []

# for i in range(apple_num):
#     apple_position = sys.stdin.readline().strip()
#     row = int(apple_position.split()[0])
#     col = int(apple_position.split()[1])
#     apple_positions.append((row, col))

# turn_num = int(sys.stdin.readline().strip())
# turn_times = []
# dirs = []

# for i in range(turn_num):
#     turn = sys.stdin.readline().strip()
#     turn_times.append(int(turn.split()[0]))
#     dirs.append(turn.split()[1])

# while live == True:
#     time += 1

#     move_snake(directions[dir_index])
#     snake_pos[0] = snake_pos[0]

#     # 회전
#     if time in turn_times:
#         time_index = turn_times.index(time)
#         turn_snake(dirs[time_index])
#         print(f"시간: {time}, {directions[dir_index]} 으로 회전")

#     if snake_pos[-1] not in apple_positions:
#         snake_pos.popleft()
#         print("시간:", time, "뱀 이동:",snake_pos)
#     else:
#         print(f"🍎 {snake_pos[-1]} 위치에 있는 사과 먹음")
#         apple_positions.remove(snake_pos[-1])
#         print("시간:", time, "뱀 이동:",snake_pos)

#     # 생사 확인
#     if (snake_pos[-1][0] < 1) or (snake_pos[-1][0] > board_size) or (snake_pos[-1][1] < 1) or (snake_pos[-1][1] > board_size):
#         live = False
#     if time == 90:
#         print(f"머리 위치: {snake_pos[-1]}")
#         print(f"꼬리 위치: {snake_pos[0]}")
#     if len(snake_pos) > 1 and snake_pos[-1] == snake_pos[0]:
#         live = False

# # 시간 추가
# # 머리 이동
# # 사과 먹었는지 여부 확인 (머리 위치 == 사과 위치)
# # 위의 여부에 따라 꼬리 없애거나 놔두기
# # 특정 시간 지나면 방향 전환
# # 죽었는지 확인
# # 죽었으면 시간 반환

# print("\n==== 종료 ====")
# print("뱀 위치:", snake_pos)
# print("시간:", time)


import sys
import itertools
from collections import deque

time = 0
snake_pos = deque([(1, 1)]) # 꼬리가 맨 앞, 머리가 맨 뛰

live = True
directions = ["up", "right", "down", "left"]
dir_index = 1
def turn_snake(dir):
    global dir_index
    # 방향 바꾸기
    if dir == "L":
        dir_index = (dir_index - 1) % 4
    if dir == "D":
        dir_index = (dir_index + 1) % 4
        
def move_snake(dir):
    global live
    global snake_pos
    head_pos = snake_pos[-1]
    if dir == "right":
        snake_pos.append((head_pos[0],head_pos[1] + 1))
    elif dir == "left":
        snake_pos.append((head_pos[0],head_pos[1] - 1))
    elif dir == "up":
        snake_pos.append((head_pos[0] - 1,head_pos[1]))
    elif dir == "down":
        snake_pos.append((head_pos[0] + 1,head_pos[1]))


board_size = int(sys.stdin.readline().strip())

apple_num = int(sys.stdin.readline().strip())
apple_positions = []

for i in range(apple_num):
    apple_position = sys.stdin.readline().strip()
    row = int(apple_position.split()[0])
    col = int(apple_position.split()[1])
    apple_positions.append((row, col))

turn_num = int(sys.stdin.readline().strip())
turn_times = []
dirs = []

for i in range(turn_num):
    turn = sys.stdin.readline().strip()
    turn_times.append(int(turn.split()[0]))
    dirs.append(turn.split()[1])

while live == True:
    time += 1
    
    # 이동
    move_snake(directions[dir_index])

    # 생사 확인
    if (snake_pos[-1][0] < 1) or (snake_pos[-1][0] > board_size) or (snake_pos[-1][1] < 1) or (snake_pos[-1][1] > board_size):
        live = False
    if len(snake_pos) > 1 and snake_pos[-1] in deque(itertools.islice(snake_pos, 0, len(snake_pos)-1)):
        live = False
        
    # 회전
    if time in turn_times:
        time_index = turn_times.index(time)
        turn_snake(dirs[time_index])

    if snake_pos[-1] not in apple_positions:
        snake_pos.popleft()
    else: 
        print(f"시간: {time}, 🍎 {snake_pos[-1]} 위치에 있는 사과 먹음")
        apple_positions.remove(snake_pos[-1])
    
    print("시간:", time, "뱀 이동:",snake_pos)


print(time)
