# 0 또는 1과의 연산 외에는 모두 곱하는 연산이 더 큰 수를 만든다.
# 0 또는 1과는 더하기 연산이 곱하기보다 더 큰 값을 가진다.

def solution(s):
    answer = int(s[0]) # 가장 첫 번째 숫자
    for i in s[1:]:
        if answer < 2 or int(i) < 2: # 이전까지의 합이 2보다 작거나, 현재 숫자가 2보다 작을 때
            answer += int(i)
        else:
            answer *= int(i)

    return answer

print(solution('029841'))
print(solution('11111'))
print(solution('0000000001'))