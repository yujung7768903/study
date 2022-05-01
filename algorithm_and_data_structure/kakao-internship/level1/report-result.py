# 시간 초과

def solution(id_list, report, k):
    answer = []
    report = list(set(report)) # 중복 제거
    list_stopped_id = [] # 정지된 id 리스트
    list_report_id = [] # 유저별 신고한 id 리스트
    # k번 이상 신고되면 정지 아이디 리스트에 추가
    for i in id_list:
        # 유저별 신고당한 횟수
        report_num = 0
        list_report_id_item = []
        for j in report:
            user_id, report_id = j.split()
            if i == user_id:
                list_report_id_item.append(report_id)
            if i == report_id:
                report_num += 1
        # 유저별로 신고한 사람 정리
        list_report_id.append(list_report_id_item)
        # 신고당한 횟수가 k이상이면 정지
        if report_num >= k:
            list_stopped_id.append(i)
    print(list_stopped_id)
    print(list_report_id)

    for i in range(len(id_list)):
        report_mail_num = 0
        for report_id in list_report_id[i]:
            if report_id in list_stopped_id: # 유저가 신고한 id가 정지된 id 리스트에 있으면 report_mail_num 1증가
                report_mail_num += 1
        answer.append(report_mail_num)

    # 유저가 신고한 ID가 신고당한 사람이 있는만큼 answer에 추가
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

# 필요한 연산의 수: (id의 개수 x report 원소 개수) + (id 개수 x 그 id가 신고한 id 개수)
# 최악의 경우: 1000 x 200,000 + 1000 x 999 = 200000000 + 999000 = 200,999,000