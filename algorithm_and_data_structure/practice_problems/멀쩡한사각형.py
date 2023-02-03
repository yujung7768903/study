# 틀림 / 정확성 50%
import math

def solution(w,h):
    if w >= h:
        return (w * h) - math.ceil(w/h) * h
    return (w * h) - math.ceil(h/w) * w

print(solution(8, 1))
print(solution(2, 2))
print(solution(7, 3))
print(solution(100000000, 999999999))