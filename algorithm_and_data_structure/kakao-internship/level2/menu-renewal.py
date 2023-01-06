# 메뉴 리뉴얼
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72411
# 어떻게 풀어야할지 모르겠음. 조합하려는 메뉴 개수보다 적을 때를 제외하는 것까지만 시도. 
# -> 연산 횟수가 많아질 것을 걱정했는데, 입력값이 적기 때문에 가능한 조합을 구하고 가장 많이 주문된 메뉴를 answer 에 추가하는 방법으로 해결

from itertools import combinations
from collections import Counter
# 1. 가능한 조합 2. 그 중 가장 많이 주문된 조합의 주문 횟수
def solution(orders, course):
    answer = []
    for i in course:
        list_combinations = [] # 주문별 가능한 조합의 모음
        max_order_num = 0 # 가장 많이 주문된 조합의 주문 횟수
        for orders_item in orders:
            print(f"===== 메뉴: {orders_item} =====")
            list_combinations.extend(list(combinations(sorted(orders_item), i)))
            print(f"가능한 조합: {list_combinations}")
            list_set_menu = Counter(list_combinations) # key: 가능한 세트 메뉴 조합, value: 주문된 횟수
            print(len(list_set_menu))
            if len(list_set_menu) >= 1: max_order_num = max(list_set_menu.values())
        for key, value in list_set_menu.items():
            if max_order_num >= 2 and value == max_order_num:
                answer.append(''.join(key))

    return sorted(answer)

print(solution(["AB", "ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))

# 필요한 연산의 수: course 개수 x (주문 수 + 가능한 메뉴 조합 개수) = course 개수 x (주문 수 + (최대 메뉴 수를 2개씩 가능한 조합)))
# 최악의 경우: 10 x (20 + 45) = 650
