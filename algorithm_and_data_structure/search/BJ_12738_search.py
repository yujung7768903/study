import sys

n = int(sys.stdin.readline())
list_num = list(map(int, sys.stdin.readline().split()))

# tartget보다 크거나 같은 수가 처음으로 나오는 인덱스
def lower_bound(start, end, target): # 시작 인덱스, 끝 인덱스, 타겟
    if start > end:
        return start

    mid = (start + end) // 2 # 중간 인덱스
    if answer[mid] == target:
        return mid
    elif answer[mid] < target:
        return lower_bound(mid + 1, end, target)
    else:
        return lower_bound(start, mid - 1, target)
    

answer = []
answer.append(list_num[0])
for i in list_num[1:]:
    if answer[-1] < i:
        answer.append(i)
    elif answer[-1] > i:
        idx = lower_bound(0, len(answer) - 1, i)
        answer[idx] = i

print(len(answer))




# 시간 초과된 방법
# for i in range(1, n):
#     print(f"=== i : {i} ===")
#     deq_element = []
#     deq_element.append(list_num[i - 1])
#     if i < (n - max_lengh):
#         for j in list_num[i:]:
#             print(f"j : {j}")
#             if deq_element[-1] < j:
#                 deq_element.append(j)
#         if max_lengh < len(deq_element):
#             max_lengh = len(deq_element)

# print(max_lengh)