def solution(brown, yellow):
    for divisor in getDivisorList(yellow):
        if 2 * (divisor + yellow // divisor) + 4 == brown:
            return [divisor + 2, int(yellow / divisor) + 2]


def getDivisorList(number):
    divisorList = []
    for i in range(1, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            divisorList.append(int(number / i))

    return divisorList

print(solution(10, 2))

# 위의 코드 더 짧게 만들어보기
def solution2(brown, yellow):
    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i == 0:
            if 2 * (i + int(yellow / i)) + 4 == brown:
                return [i + 2, int(yellow / i) + 2]