from collections import deque

def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def start():
    direction = 1  # 초기 방향
    time = 1  # 시간
    y, x = 0, 0  # 초기 뱀 위치
    visited = deque([[y, x]])  # 방문 위치
    arr[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1:  # 사과가 없는 경우
                temp_y, temp_x = visited.popleft()
                arr[temp_y][temp_x] = 0  # 꼬리 제거
            else:
                print(f"시간:{time} | 🍎 ({y + 1, x + 1}) 위치에 있는 사과 먹음")
            arr[y][x] = 2
            visited.append([y, x])
            print("시간:", time, "| 뱀 이동:",visited)
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else:  # 본인 몸에 부딪히거나, 벽에 부딪힌 경우
            print(f"y(행): {y}, x(열): {x}, N: {N}")
            print(0 <= y < N)
            print(0 <= x < N)
            print(arr[y][x])
            return time


if __name__ == "__main__":

    # input
    N = int(input())
    K = int(input())
    arr = [[0] * N for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[a - 1][b - 1] = 1  # 사과 저장
    L = int(input())
    times = {}
    for i in range(L):
        X, C = input().split()
        times[int(X)] = C
    print(start())