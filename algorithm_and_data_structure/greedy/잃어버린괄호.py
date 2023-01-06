# 무조건 음수 갑이 커지게. - 뒤에 있는 값들 묶기

def solution(args):
    args = args.split("-")
    answer = sum(map(int, args[0].split("+"))) # 처음으로 -가 나오기 전까지 모두 더하기

    for i in args[1:]:
        answer -= sum(map(int, i.split("+")))
    
    return answer

n = input()
print(solution(n))

# 시간 복잡도 분석
# -의 개수가 k라고 할 때, 소스코드의 시간복잡도는 O(k)이다.
# 이 알고리즘의 시간 복잡도는 -의 개수에만 영향을 받는다.