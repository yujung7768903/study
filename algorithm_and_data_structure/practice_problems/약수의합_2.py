import time


def f(x, resultList):
    resultListItem = set([1, x])
    for i in range(2, int(x**(1/2)) + 1):
        if x % i == 0:
            resultListItem.add(i)
            resultListItem.add(int(x / i))
            for j in resultList[int(x / i)]:
                if j not in resultListItem:
                    resultListItem.add(j)
                    resultListItem.add(int(x / j))
            break
    resultList.append(resultListItem)
    return sum(resultListItem)

def g(x):
    answer = 0
    resultList = [[]]
    for i in range(1, x + 1):
        answer += f(i, resultList)
    return answer

def f2(x):
    sumList = set()
    for i in range(1, int(x**(1/2)) + 1):
        if x % i == 0:
            sumList.add(i)
            sumList.add(int(x / i))
    return sum(sumList)

def g2(x):
    answer = 0
    for i in range(1, x + 1):
        answer += f2(i)
    return answer

n = int(input())
start = time.time()
g(n)
print(f"총 소요 시간: {time.time() - start}")
print("============= 비교 ================")
start = time.time()
g2(n)
print(f"총 소요 시간: {time.time() - start}")

# 첫 번째 방법과 소요 시간 비교

# 경우1
# 100000
# 총 소요 시간: 0.4919612407684326
# ============= 비교 ================
# 총 소요 시간: 0.8321149349212646

# 경우 2
# 300000
# 총 소요 시간: 1.7059047222137451
# ============= 비교 ================
# 총 소요 시간: 4.675907135009766