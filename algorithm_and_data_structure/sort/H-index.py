def solution(citations):
    answer = 0
    citations.sort()
    for i in range(1, len(citations) + 1):
        bigNum = 0
        for index, number in enumerate(citations):
            if i > number: continue
            if i < number:
                bigNum = len(citations) - index
                break
            if i == number:
                bigNum = len(citations) - index + 1
                break
        if bigNum >= i:
            print(f"answer: {answer} -> {i}")
            answer = i

    return answer

# citiations = [3, 0, 6, 1, 5] # 0, 1, 3, 5, 6
# citiations = [3]
# citiations = [1,1,1,1,1,1,100]
# citiations = [1,2,3,4,5]
citiations = [2,4,6,8,10,12]
# citiations = [4,4,6,6,6,6]

print(solution(citiations))