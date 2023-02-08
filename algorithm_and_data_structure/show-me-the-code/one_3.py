# 시간 초과

import re
from itertools import combinations
from functools import reduce

def countTotal(startIdx, endIdx):
    plusSum = reduce(lambda acc, cur: acc + cntList[cur], range(startIdx, endIdx + 1, 2), 0)
    minusSum = reduce(lambda acc, cur: acc + cntList[cur], range(startIdx + 1, endIdx + 1, 2), 0)
    print(f"plusSum: {plusSum}, minusSum: {minusSum}, 절대값: {abs(plusSum - minusSum)}")
    return abs(plusSum - minusSum)

def solution():
    if len(set(cntList)) == 1: return cntList[0]

    maxCnt = max(cntList)
    print(cntList)
    print(list(combinations(range(len(cntList)), 2)))
    for startIdx, endIdx in combinations(range(len(cntList)), 2):
        newCnt = countTotal(startIdx, endIdx)
        if newCnt > maxCnt:
            maxCnt = newCnt

    return maxCnt

n = int(input())
inputList = input().split()
pattern = re.compile("1+|2+")
cntList = list(map(len, pattern.findall("".join(inputList))))
print(solution())

# print(pattern.findall("211212111"))
# print(list(map(len, pattern.findall("211212111"))))

# n = int(input())
# inputList = map(int, input().split())
