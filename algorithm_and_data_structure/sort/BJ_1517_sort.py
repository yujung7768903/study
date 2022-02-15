n = int(input())
list_num = list(map(int, input().split()))
swap_num = 0

for i in range(len(list_num) - 1):
    for j in range(len(list_num) - 1 - i):
        if list_num[j] > list_num[j + 1]:
            list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]
            swap_num += 1

print(swap_num)