# 참고한 수학 공식: https://math.stackexchange.com/questions/205700/solving-a-series-n1-n-n2-n3-n4-nn-1
# 문제 풀이 시간: 1시간

# I 이전 단어 구해보기
# 한자리 단어
# 2 개
# 두 자리인 단어
# 2 * 5
# 세 자리 단어
# 2 * (5 * 2) 개
# 세 자리인 단어
# 2 * (5 ** 3)
# 네 자리인 단어
# 2 * (5 ** 4) 개

dict = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
def solution(word):
    answer = 0
    for index, alp in enumerate(word):
        answer += dict[alp] * ((5 ** (5 - index) - 1) / 4)

    return int(answer) + len(word)