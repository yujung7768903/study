# 퀵 정렬
# [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]

def quickSort(array):
    print(array)

    if len(array) <= 1:
        print(f"정렬 완료: {array}")
        return array

    pivot = array[0]
    left, right = [], []

    for i in range(1, len(array)):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] > pivot:
            right.append(array[i])

    print(f"👈 왼쪽: {left}, ✊ 기준: {[pivot]}, 👉 오른쪽: {right}")
    return quickSort(left) + [pivot]

# li = [3, 1, 5, 9, 8, 6, 7, 4, 10, 2]
li = [5, 3, 1, 6, 8, 10, 4, 7, 2, 9]
print(f"quickSort(li): {quickSort(li)}")