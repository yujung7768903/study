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

    for i in range(len(id_list)):
        answer_item = 0
        for j in list_report_id[i]:
            if j in list_stopped_id:
                answer_item += 1
        answer.append(answer_item)

    # 유저가 신고한 ID가 신고당한 사람이 있는만큼 answer에 추가
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))