import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계
    new_id = re.sub("[^a-z0-9\-_\.]", '', new_id)
    # 3단계
    new_id = re.sub("\.\.+", '.', new_id)
    # 4단계
    new_id = re.sub('^\.|\.$', '', new_id)
    # 5단계
    if new_id == '':
        new_id = 'a'
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[-1] == '.':
        new_id = new_id[0:-1]
    # 7단계
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    answer = new_id
    return answer

# 정규 표현식
# |는 or의 의미
# ^은 []안에 있을 때는 not의 의미, 아닐 때에는 문자열의 시작을 의미
# $은 문자열의 끝을 의미. foo$는 문자열 끝의 foo를 의미
# *은 0번 이상 반복, +는 한 번 이상 반복