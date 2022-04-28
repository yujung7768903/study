# 문자열 압출
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/60057

from timeit import repeat
import re

def solution(s):
    list_s = []
    # for i in range(len(s)//2):
    #     for j in range(0, len(s), i):
    #         list_s.append(j)
    #     present_num = list_s[0]
    #     repeat_num = 1
    #     if present_num == list_s[1]:
            
        

    answer = 0
    return answer

string1 = 'aabbaccc'
p = re.compile('a+|b+|c+')
m = p.findall(string1)
print(m)