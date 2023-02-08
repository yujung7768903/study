# 틀림 / 정확성 50%
# 반례 5, 3 -> 정답: 8 / 오답인 9가 나옴
# 가로가 1일 때 세로의 길이를 계산 -> 쓸 수 없는 사각형 계산
import math

def solution(w,h):
    print("=================")
    if w >= h:
        print(f"나누기: {w/h}, 올림: {math.ceil(w/h)}")
        return (w * h) - math.ceil(w/h) * h
    print(f"나누기: {h/w}, 올림: {math.ceil(h/w)}")
    return (w * h) - math.ceil(h/w) * w

# print(solution(8, 1))
# print(solution(2, 2))
print(solution(5, 3))
# print(solution(10, 9))
# print(solution(100000000, 999999999))