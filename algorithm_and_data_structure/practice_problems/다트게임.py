import re

scoreList = [0, 0, 0]
def solution(dartResult):
    pattern = re.compile("\d+[SDT][*#]?")
    roundInfoList = pattern.findall(dartResult)

    for index, roundInfo in enumerate(roundInfoList):
        calScore(index, roundInfo)
        print(scoreList)
    return sum(scoreList)

def calScore(index, roundInfo):
    scorePattern = re.compile("\d+")
    score = int(scorePattern.findall(roundInfo)[0])

    if "D" in roundInfo:
        score = score ** 2
    if "T" in roundInfo:
        score = score ** 3
    if "#" in roundInfo:
        score *= -1
    if "*" in roundInfo:
        score *= 2
        if index >= 1:
            scoreList[index - 1] *= 2

    scoreList[index] = score

# print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
# print(solution("1S2D*3T"))
# print(solution("1S2D*3T"))