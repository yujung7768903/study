import re

def solution(new_id):
    new_id = new_id.lower()
    print(new_id)
    new_id = re.sub("[^a-z0-9\-_\.]", '', new_id)
    new_id = re.sub("\.\.+", '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    if new_id[-1] == '.':
        new_id = new_id[0:-1]
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]
    answer = new_id
    return answer

# 정규 표현식
# |는 or의 의미
# ^은 []안에 있을 때는 not의 의미, 아닐 때에는 문자열의 시작을 의미
# $은 문자열의 끝을 의미. foo$는 문자열 끝의 foo를 의미
# *은 0번 이상 반복, +는 한 번 이상 반복