import itertools

def solution(numbers, target):
    answer = 0
    for num in range(len(numbers)):
        combList = itertools.combinations(numbers, num)
        for comb in combList:
            minusNumSum = sum(list(comb))
            # print(f"comb: {comb}, minusNumSum: {minusNumSum}")
            if sum(numbers) - 2 * minusNumSum == target:
                answer += 1

    return answer

numbers = [4, 1, 2, 1]
print(solution(numbers, 4))
