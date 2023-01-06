import itertools

def solution(numbers, target):
    answer = 0
    indexList = [i for i in range(len(numbers))]
    for num in range(len(numbers)):
        combList = itertools.combinations(indexList, num)
        # print(f"combList: {list(combList)}")
        for comb in combList:
            print(f"comb: {comb}")
            newNumbers = numbers.copy()
            for index in comb:
                newNumbers[index] *= -1
            print(f"newNumbers: {newNumbers}, sum: {sum(newNumbers)}, sum(newNumbers) == {target}: {sum(newNumbers) == target}")
            if sum(newNumbers) == target:
                answer += 1
        print(f"combList: {list(combList)}")

    return answer

numbers = [1, 1, 1, 1, 1]
print(solution(numbers, 3))

# 최대 반복 횟수
# 20 (numbers 개수) *