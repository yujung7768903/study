n = int(input())
inputList = set()
for _ in range(n):
    inputList.add(input())


print("\n".join(sorted(inputList, key=lambda x: (len(x), x))))