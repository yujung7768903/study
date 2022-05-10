import sys
from collections import defaultdict

def solution(n):
    answer = 0
    dict_alp = defaultdict(int)
    for i in range(n):
        word = sys.stdin.readline().strip()
        for index, j in enumerate(word[::-1]): # 일의 자리 숫자부터 돌기
            dict_alp[j] += (10 ** index)
            print(dict_alp)
    
    list_value = list(dict_alp.values())
    list_value.sort(reverse=True) # 내림차순으로 정렬
    
    for k, num in enumerate(list_value):
        answer += (9 - k) * num

    return answer
    
n = int(sys.stdin.readline())
print(solution(n))