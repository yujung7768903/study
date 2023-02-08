lower = list("abcdefghijklmnopqrstuvwxyz")
upper = list("abcdefghijklmnopqrstuvwxyz".upper())

def solution(s, n):
    inputList = list(s)
    print(inputList)
    answer = ''
    for item in inputList:
        if item == " ":
            answer += " "
        elif item.islower():
            answer += lower[(lower.index(item) + n) % len(lower)]
        else:
            answer += upper[(upper.index(item) + n) % len(upper)]
    return answer

# print(solution("AB", 1))
print(solution("ABZ", 4))