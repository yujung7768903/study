# 선택 정렬
# [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]

def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    return array

li = [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]
print(selectionSort(li))