# LIS를 구하는 알고리즘을 O(N^2)이 아닌 O(NlogN)으로 구현을 해야하는 문제
# lower_bound를 이용하여 푸는 문제. 파이썬에는 관련 라이브러리가 없어서 직접 구현해야함
# lower_bound: 처음으로 특정 숫자 이상인 값이 나오는 인덱스를 반환해주는 함수

n = int(input())
arr = list(map(int,input().split()))

def lower_bound(start,end,target):
    if start>end:
        return start
       
    mid = (start+end)//2
    
    if answer[mid] > target:
        return lower_bound(start,mid-1,target)
    elif answer[mid] == target:
        return mid
    else:
        return lower_bound(mid+1,end,target)

answer = []
for num in arr:
    if len(answer) == 0:
        answer.append(num)
        continue

    if answer[-1] < num:
        answer.append(num)
    else:
        idx = lower_bound(0, len(answer)-1, num)
        answer[idx] = num


print(len(answer))