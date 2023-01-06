# 문자열 압출
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60057
# 해결 못함.

import string
import re

def solution(s):
    answer = len(s)
    count = 0
    # 단위수대로 문자열 자르기
    for i in range(1, len(s)//2 + 1):
        present_item = s[0:i]
        list_s = []
        print(f"=== i: {i} ===")
        for j in range(0, len(s), i):
            list_s.append(s[j:j + i])
        print(list_s)













#         list_s_item = list(set(list_s))
#         print(f"s를 {i}로 나눴을 때 원소: {list_s_item}")
#         compile_rule = ''
#         for i in list_s_item:
#             if i == len(list_s_item):
#                 compile_rule += f"{i}+"
#             else:
#                 compile_rule += f"{i}+|"
#         p = re.compile(compile_rule)
#         m = p.findall(s)
#         print(m)
#         # 문자열 압축
#         string_length = ''
#         for i in m:
#             if len(i) > 1:
#                 string_length = string_length + str(len(i)) + i
#             else:
#                 string_length = string_length + i
#         print(string_length)
#         if len(string_length) < answer:
#             answer = len(string_length)

#     return answer

# print(solution('aabbaccc'))

# string1 = 'aabbaccc'
# compile_rule = ''
# for i in string.ascii_lowercase:
#     if i == len(string.ascii_lowercase):
#         compile_rule += f"{i}+"
#     else:
#         compile_rule += f"{i}+|"

# p = re.compile(compile_rule)
# m = p.findall(string1)
# string_length = ''
# for i in m:
#     if len(i) > 1:
#         string_length = string_length + str(len(i)) + i
#     else:
#         string_length = string_length + i
        
# print(m)
# print(string_length)
