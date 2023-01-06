# 신고 결과 받기 다른 사람 풀이 방법

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

# 필요한 연산의 수: 2 x report 원소 개수
# 최악의 경우: 2 x 200,000 = 400,000