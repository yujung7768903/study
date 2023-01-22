def f(x):
    sumList = set()
    for i in range(1, int(x**(1/2)) + 1):
        if x % i == 0:
            sumList.add(i)
            sumList.add(int(x / i))
    print(f"i: {x} | 합: {sum(sumList)} | 약수 리스트: {sorted(sumList)}")
    return sum(sumList)

def g(x):
    answer = 0
    for i in range(1, x + 1):
        answer += f(i)
    return answer

n = int(input())
print(g(n))
f(50)