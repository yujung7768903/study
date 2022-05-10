def solution(n, k):
    count = 0 # 연산 횟수

    while n >= k:
        share, rest = divmod(n, k)
        n = share
        count += (rest + 1) # 나머지만큼 빼기 연산 + 나누기 연산

    count += (n - 1) # 마지막으로 남은 수 빼기

    return count

print(solution(26, 3))

# N으로 나누어 떨어진다면, 무조건 N으로 나눠야함. (더 좋은 것을 고르는 것)
# N으로 나누는 방법은 1을 빼는 것보다 N을 항상 더 작게 만들기 때문에, 그리디 방법으로 최적의 해를 구할 수 있다.