# 선형 탐색
# [3, 1, 5, 9, 8, 6, 7, 4, 10, 2] 6, 2, 11

def sequentialSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    
    return -1

li = [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]
print(sequentialSearch(li, 6))
print(sequentialSearch(li, 2))
print(sequentialSearch(li, 11))