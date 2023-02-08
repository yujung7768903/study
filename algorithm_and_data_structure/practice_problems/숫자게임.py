# 문제 풀이 시간: 20s

from collections import deque

def solution(aList, bList):
    answer = 0
    aList.sort()
    leftB = deque(sorted(bList))
    for a in aList:
        for _ in range(len(leftB)):
            if a < leftB.popleft():
                answer += 1
                break
    return answer

# a = [5,1,3,7]
# b = [2,2,6,8]

a = [1,3,7]
b = [2,2,6,8]
print(solution(a, b)) # 결과 3
a = [2,2,2,2]
b = [1,1,1,1]
print(solution(a, b)) # 결과 0
# 이기면 승점 1점, 비기면 0점