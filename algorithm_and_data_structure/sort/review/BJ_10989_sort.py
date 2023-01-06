import sys

n = int(sys.stdin.readline())
zero_list = [0] * 10001

for i in range(n):
    input_value = int(sys.stdin.readline())
    zero_list[input_value] += 1

# i는 0부터 인덱스 값 = 숫자 값, zero_list[0]은 해당 숫자 갯수
for i in range(len(zero_list)):
    if zero_list[i] != 0:
        for j in range(zero_list[i]):
            print(i)