def solution(number, limit, power):
    answer = 0
    totalList = []
    for num in range(1, number + 1):
        numList = set([1, num])
        # 약수 구하기
        for i in range(2, int(num ** (1/2)) + 1):
            if num % i == 0:
                numList.add(i)
                numList.add(int(num / i))
        totalList.append(len(numList))
    for total in totalList:
        if total > limit:
            total = power
        answer += total

    return answer

print(solution(5, 3, 2))