import math

# 소수 판별
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    convert_num = ''
    while n > 0:
        n, mod = divmod(n, k)
        convert_num += str(mod)
    convert_num = convert_num[::-1]
    print(convert_num)

    if '0' in convert_num:
        list_n = convert_num.split('0')
        print(list_n)
        for num in list_n:
            if num != '' and is_prime(int(num)):
                answer += 1
            print(answer)
    else:
        if is_prime(int(convert_num)):
            return 1
        else:
            return 0

    return answer

print(solution(1, 10))