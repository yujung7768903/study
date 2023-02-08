n = int(input())
inputList = list(map(lambda x: -1 if x == "2" else 1, input().split()))

acc = 0
accList = []
for i in inputList:
    acc += i
    accList.append(acc)

print(accList)

print(max(accList + [0]) - min(accList + [0]))