# 헷갈리기 쉬운 점
# 1) 자른 랜선의 개수가 딱 N인 키값을 찾았다고 탈출하면 안 된다. 더 큰 키값을 계속 찾으면서 최댓값을 찾아야 한다.
# 2) 자른 랜선의 개수가 N보다 많을 때 못 찾았다고 더 큰 키값만 탐색하면 안 된다. 더 큰 키값에서 못 찾을 수도 있으니까 일단 현재 최댓값을 업데이트한 뒤에 계속 찾아야 한다.
# 3) 모든 랜선을 사용할 필요는 없다. 아예 너무 짧은 랜선은 버리는 결과가 나올 수도 있다.

import sys

k, n  = map(int, sys.stdin.readline().split())

list_length = []
for i in range(k):
    length = int(sys.stdin.readline())
    list_length.append(length)

def find_max_length(input_list):
    max_length = 0 # 랜선의 최대 길이
    start = 1
    end = max(list_length)
    while start <= end:
        n_num = 0 # 랜선 갯수
        mid = (start + end) // 2 # 랜선 길이
        print(f"✂️✂️{mid}로 자름✂️✂️")
        for i in list_length:
            n_num += (i // mid)
            print(f"랜선 길이:{i}, 랜선 개수{n_num}")
        if n_num < n:
            end = mid - 1
            print(f"범위: {start} ~ {end}")
        elif n_num >= n:
            start = mid + 1
            print(f"범위: {start} ~ {end}")
            if mid > max_length:
                max_length = mid
                print(f"최댓값: {mid}")
    return max_length

print(find_max_length(list_length))