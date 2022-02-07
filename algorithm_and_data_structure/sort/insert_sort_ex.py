# 삽입 정렬
# [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]

def insertionSort(array):
    for i in range(1, len(array)):
        print("")
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break
        print(array)
    return array

li = [3, 1, 5, 9, 8, 6, 7, 4, 10, 2];
print(insertionSort(li))