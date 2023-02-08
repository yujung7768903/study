# 문제 풀이 시간: 13분

def solution(n, words):
    useWordList = []
    for index, word in enumerate(words):
        if len(useWordList) > 0 and (word in useWordList or useWordList[-1][-1] != word[0]):
            return [index % n + 1, index // n + 1]
        useWordList.append(word)

    return [0, 0]


# Test

# words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# print(solution(3, words))

words = ["hello", "observe", "effect", "rake", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(5, words))