# 메뉴 리뉴얼
# 문제 링크: https://programmers.co.kr/learn/courses/30/lessons/72411
# 어떻게 풀어야할지 모르겠음. 조합하려는 메뉴 개수보다 적을 때를 제외하는 것까지만 시도.

def solution(orders, course):
    answer = []
    for i in course:
        set_menu = []
        for orders_item in orders:
            if len(orders_item) >= i:
                set_menu.append(orders_item)
                            
    return answer