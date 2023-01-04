# participantMap = {}
# completionMap = {}

# def solution(participant, completion):
#     for i in participant:
#         participantMap[i] = participantMap[i] + 1 if i in participantMap else 1
    
#     for j in completion:
#         completionMap[j] = completionMap[j] + 1 if j in completionMap else 1

#     for k in participantMap.keys():
#         # 참가자가 완주자 목록에 없을 때, 동명이인이 포함된 경우일 때는 완주자 목록에 있는 이름 수보다 참가한 이름의 수가 많을 때
#         if not (k in completionMap) or (participantMap[k] - completionMap[k]) > 0:
#             return k

def solution(participant, completion):
    participantMap = {key: 0 for key in participant}
    completionMap = {key: 0 for key in completion}
    
    for i in participant:
        participantMap[i] = participantMap[i] + 1
    
    for j in completion:
        completionMap[j] = completionMap[j] + 1

    for k in participantMap.keys():
        # 참가자가 완주자 목록에 없을 때, 동명이인이 포함된 경우일 때는 완주자 목록에 있는 이름 수보다 참가한 이름의 수가 많을 때
        if not (k in completionMap) or (participantMap[k] - completionMap[k]) > 0:
            return k


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))