# 메뉴 리뉴얼
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72411
# 어떻게 풀어야할지 모르겠음. 조합하려는 메뉴 개수보다 적을 때를 제외하는 것까지만 시도.
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        list_combinations = [] # 주문별 가능한 조합의 모음
        for orders_item in orders:
            print(f"주문: {orders_item}")
            list_combinations.extend(list(combinations(sorted(orders_item), i)))
            print(f"가능한 조합의 모음: {list_combinations}")
        print(f"===결과: {Counter(list_combinations).most_common()}===")

    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
