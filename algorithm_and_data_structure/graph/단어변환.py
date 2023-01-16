# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    que = deque([[begin, 0]])
    while len(que) > 0:
        startWord, stage = que.popleft()
        for word in words:
            difCnt = 0
            for index in range(len(begin)):
                if word[index] != startWord[index]:
                    difCnt += 1
            if difCnt == 1:
                if word == target:
                    return stage + 1
                que.append([word, stage + 1])

    return 0

# words = ["hot", "dot", "dog", "lot", "log", "cog"]
words = ["hot", "dog", "log", "dot", "lot", "cog"]
print(solution("hog", "lot", words))