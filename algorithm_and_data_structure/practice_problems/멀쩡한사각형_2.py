# 틀림 / 정확성 72.2 (4, 6, 12, 14, 17번 실패)
import math

def solution(w,h):
    start = 0
    answer = 0
    if w < h: w, h = h, w
    print(f"반복문 범위: {[(w / h) * i for i in range(1, h + 1)]}")
    for end in [(w / h) * i for i in range(1, h + 1)]:
        print(f"start: {start}, end: {end}, answer: {answer}")
        answer += math.ceil(end) - math.floor(start)
        start = end

    return (w * h) - answer


# 정답 / 최대 공약수만큼 쪼개서 생각했을 때 쪼갠 사각형 안에서 잘린 사각형은 w + h - 1 이다. 결국 1을 최대 공약수만큼 빼주게 된다.
def solution(w,h):
    if w < h: w, h = h, w
    return (w * h) - (w + h - math.gcd(w, h))


print(solution(5, 3))
print(solution(12, 3))