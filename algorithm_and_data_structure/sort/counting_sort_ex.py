# 계수 정렬
# [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]

def countingSort(array):
    count_array = [0] * (max(array) + 1)

    for i in range(len(array)):
        count_array[array[i]] += 1
        print(count_array)

    array.clear()

    for i in range(len(count_array)):
        for j in range(count_array[i]):
            array.append(i)
        print(count_array)

    return array

li = [3, 1, 3, 9, 3, 6, 7, 4, 10, 2]
print(countingSort(li))
