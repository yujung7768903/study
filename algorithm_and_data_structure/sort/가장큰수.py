def solution(numbers):
    strSortList = sorted(map(str, numbers), reverse=True, key=lambda x: x + x * (4 - len(x)))
    return str(int("".join(strSortList)))

# numbers = [3, 30, 34, 340, 341, 305, 5, 9, 0]
# numbers = [6, 10, 2, 0, 1000]
numbers = [0, 0]
print(solution(numbers))
