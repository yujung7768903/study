# 버블 정렬
# [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]

def bubbleSort(array):
    for i in range(len(array) - 1):
        print(f"i: {i}")
        for j in range(len(array) - 1 - i):
            print(f"j: {j}")
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            print(array)
    return array

li = [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]
print(bubbleSort(li))