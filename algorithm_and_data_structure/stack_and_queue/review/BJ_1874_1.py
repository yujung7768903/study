# TEST CASE2 커버 못함
import sys
from collections import deque
# [4,3,6,8,7,5,2,1]

list_item = [1] # 스택
present_num = 1
list_result = ["+"] # push or pop

n = int(sys.stdin.readline())

input_value_list = []
for i in range(n):
    input_value = int(sys.stdin.readline())
    input_value_list.append(input_value)

def push_item():
    global present_num
    present_num += 1
    print(f"add_item: {present_num}")
    list_item.append(present_num)
    list_result.append("+")
    print(f"present_num: {present_num}")
    print(list_item)

def pop_item():
    list_item.pop()
    list_result.append("-")
    print(list_result)

for i in input_value_list:
    print("================")
    print(f"i: {i}")
    if list_item:
        print(f"list_item[-1]: {list_item[-1]}")
        if list_item[-1] > i:
            print("NO")
            break
        while list_item[-1] < i: #3
            push_item()
        if list_item[-1] == i:
            pop_item()
    else:
        push_item()
        pop_item()