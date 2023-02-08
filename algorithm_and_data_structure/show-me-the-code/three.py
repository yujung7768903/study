n, m, c = map(int, input().split())
wMap = []
for _ in range(c):
    wMap.append(list(map(int, input().split())))
nList = list(map(int, input().split()))
mList = list(map(int, input().split()))
print(wMap)

# loopRange = nList if len(nList) <= len(mList) else mList
# score = 0
# maxScore = 0
# for crossNum in range(loopRange):
#     nCombList = list(combinations([i for i in range(len(nList))], crossNum))
#     mCombList = list(combinations([i for i in range(len(mList))], crossNum))

def calScore(nComb, mComb, crossNum):
    score = 0
    for index in range(crossNum):
        nIndex = nComb[index]
        mIndex = mComb[index]
        score += wMap[nList[nIndex] - 1][mList[mIndex] - 1]
        print(f"nIndex: {nIndex}, mIndex: {mIndex}, 만족도: {wMap[nList[nIndex] - 1][mList[mIndex] - 1]}")
    return score
