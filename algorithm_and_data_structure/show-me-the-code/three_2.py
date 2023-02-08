# dy[i][j]에는 3가지 경우가 존재: 1. A[i] 와 B[j]가 연결된 경우 2. A[i]가 사용되지 않은 경우 2. B[j]가 사용되지 않은 경우

n, m, c = map(int, input().split())
wMap = []
for _ in range(c):
    wMap.append(list(map(int, input().split())))
aList = list(map(lambda x: int(x) - 1, input().split()))
bList = list(map(lambda x: int(x) - 1, input().split()))
dy = [[0 for _ in range(len(bList))] for _ in range(len(aList))]

for i, aNum in enumerate(aList):
    for j, bNum in enumerate(bList):
        wList = [wMap[aNum][bNum], 0, 0]
        if i > 0 and j > 0:
            wList[0] += dy[i - 1][j - 1]
        if i > 0:
            wList[1] = dy[i - 1][j]
        if j > 0:
            wList[2] = dy[i][j - 1]
        dy[i][j] = max(wList)
print(dy[len(aList) - 1][len(bList) - 1])