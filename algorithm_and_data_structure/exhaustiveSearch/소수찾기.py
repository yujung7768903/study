from itertools import permutations

minorityList = set()
def solution(numbers):
    numberList = [number for number in numbers]
    for i in range(1, len(numbers) + 1):
        permutationList = permutations(numberList, i)
        for permutation in permutationList:
            isMinority(int("".join(permutation)))

    return len(minorityList)

def isMinority(number):
    if number in [0, 1]:
        return False
    for i in range(2, int(number ** (1 / 2) + 1)):
        if number % i == 0:
            return False

    minorityList.add(number)