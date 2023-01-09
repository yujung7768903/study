# 문제: 백준 1389번 케빈 베이컨의 6단계 법칙
# 문제 링크: https://www.acmicpc.net/problem/1389

from collections import deque

n, m = map(int, input().split(" ")) # n: 유저의 수, m: 관계의 수
friendDict = {key: set() for key in range(n + 1)}

for _ in range(m):
    a, b = map(int, input().split(" "))
    friendDict[a].add(b)
    friendDict[b].add(a)

def solution():
    minSum = []  # 현재까지 케빈 베이컨의 수가 가장 작은 친구 번호, 케빈 베이컨 수
    for start in range(1, n + 1):
        result = bfs(start)
        if len(minSum) == 0 or result < minSum[1]:
            minSum = [start, result]
    return minSum[0]

def bfs(start):
    deq = deque([[start, 0]]) # 원소: 친구 번호, 시작 친구로부터 떨어진 단계
    endList = [start]
    total = 0
    while len(deq) > 0:
        friend, stage = deq.popleft()
        stage += 1
        for nextFriend in friendDict[friend]:
            if not nextFriend in endList:
                endList.append(nextFriend)
                deq.append([nextFriend, stage])
                total += stage
    return  total

print("===== [결과] =====")
print(solution())