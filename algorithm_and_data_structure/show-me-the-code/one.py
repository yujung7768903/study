n = int(input())
inputList = map(int, input().split(" "))

maxCnt = 0
leftNum = 0
rightNum = 0

for dir in inputList:
    if dir == 1:
        leftNum += 1
    else:
        rightNum += 1

    if leftNum >= rightNum and (leftNum - rightNum) > maxCnt:
        maxCnt = leftNum - rightNum
    elif (rightNum - leftNum) > maxCnt:
        maxCnt = rightNum - leftNum
print(maxCnt)
