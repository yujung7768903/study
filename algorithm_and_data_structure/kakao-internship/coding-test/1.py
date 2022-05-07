# 통과

def solution(survey, choices):
    answer = ''
    dict_type_score = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        elif choices[i] > 4: # 동의 관련 선택지
            dict_type_score[survey[i][1]] += (choices[i] - 4)
        else: # 비동의 관련 선택지
            dict_type_score[survey[i][0]] += (4 - choices[i])
            
    for j in range(0, 7, 2):
        list_key = list(dict_type_score.keys())
        list_value = list(dict_type_score.values())
        if list_value[j] >= list_value[j + 1]:
            answer += list_key[j]
        else:
            answer += list_key[j + 1]
    
    print(answer)
    return answer

# ex1
survey1 = ["AN", "CF", "MJ", "RT", "NA"]
choice1 = [5, 3, 2, 7, 5]
solution(survey1, choice1)