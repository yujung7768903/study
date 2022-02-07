# 이진 탐색
# [1, 3, 4, 6, 7, 9, 11, 13, 14, 15, 17] 6, 15, 20

def binarySearch(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        print("mid:", mid)

    return -1

li = [1, 3, 4, 6, 7, 9, 11, 13, 14, 15, 17]
print(binarySearch(li, 6))
print(binarySearch(li, 15))
print(binarySearch(li, 10))