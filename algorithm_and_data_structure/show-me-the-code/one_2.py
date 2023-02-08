n = int(input())
inputList = list(map(int, input().split(" ")))

cnt = 0
maxCnt = 0
lastDir = inputList[0]

for dir in inputList:
    if dir == lastDir:
        cnt += 1
        if cnt > maxCnt:
            maxCnt = cnt
    else:
        cnt -= 1
print(maxCnt)