import sys

board = int(sys.stdin.readline().strip())
sequence = list(map(int, input().split()))

def find_nge(list, index):
    for i in range(index + 1, len(list)):
        print(f"list[{index}]: {list[index]} < list[{i}]: {list[i]} = {list[index] < list[i]}")
        if list[index] < list[i]:
            print(f"result: {list[i]}")
            return list[i]

    return -1

nges = []
for i in range(len(sequence)):
    print("=========")
    print(f"i: {i}")
    nges.append(find_nge(sequence, i))

print(*nges)

# import sys

# board = int(sys.stdin.readline().strip())
# sequence = sys.stdin.readline().split()

# nges = []
# for i in range(board):
#     for j in range(i + 1, board):
#         if sequence[i] < sequence[j]:
#             print(f"{sequence[j]} 추가")
#             nges.append(sequence[j])
#             break
#         else: nges.append(-1)

# print(*nges)