n = input()

def solution():
    answer = 0
    for hour in range(int(n) + 1):
        for min in range(60):
            for sec in range(60):
                if '3' in str(hour) or '3' in str(min) or '3' in str(sec):
                    answer += 1
    
    return answer


print(solution())