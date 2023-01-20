# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    genresDict = {}
    totalCntDict = {}
    for i, genre, play in zip(range(len(genres)), genres, plays):
        genresDict[genre] = genresDict.get(genre, []) + [[play, i]]
        totalCntDict[genre] = totalCntDict.get(genre, 0) + play
    totalCntDict = sorted(totalCntDict.items(), key =lambda item: -item[1])
    print(totalCntDict)
    print(genresDict)
    for genre in [totalInfo[0] for totalInfo in totalCntDict]:
        genresDict[genre] = sorted(genresDict[genre], key=lambda item: -item[0])
        for j in genresDict[genre][:2]:
            answer.append(j[1])

    return answer
