# 시간초과 해결

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report)) # 중복 제거
    list_report_to = defaultdict(list) # key: 신고한 유저, value: 그 유저가 신고한 id 리스트
    list_report_from = defaultdict(list) # key: 신고당한 유저, value: 해당 유저를 신고한 id

    for i in report:
        user_id, report_id = i.split()
        list_report_to[user_id].append(report_id)
        list_report_from[report_id].append(user_id)

    print(f"list_report_to: {list_report_to}")
    print(f"list_report_from: {list_report_from}")

    for id in id_list:
        report_mail_num = 0
        for report_id in list_report_to[id]:
            if len(list_report_from[report_id]) >= k: # 유저가 신고한 id가 k번 이상 신고당했으면, report_mail_num 1증가
                report_mail_num += 1
        answer.append(report_mail_num)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

# 필요한 연산의 수: report 원소 개수 + (id 개수 x 그 id가 신고한 id 개수)
# 최악의 경우: 200,000 + 1000 x 999 = 1,199,000