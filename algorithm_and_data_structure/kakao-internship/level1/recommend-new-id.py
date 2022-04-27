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
