# deque(double ended queue): 데이터의 양끝에 원소를 추가할 수 있는 구조
# insert(i, x): i위치에 x추가 / count(x): x의 개수 반환 / index(x): x의 위치 반환 / clear(): 전체 삭제

# 구현 함수: append(), pop(), extend(), insert(), remove(), reverse(), clear()

from collections import deque

deq = deque([4, 5, 6])

deq.append(7)
deq.appendleft(3)
print(deq)

deq.pop()
deq.popleft()
print(deq)

print("==== extend ====")
# extend는 기존의 리스트에 추가하는 리스트의 원소를 모두 넣음
# append vs extend
# append를 할 경우: [4, 5, 6, [1, 2, 3]]
# extend를 할 경우: [4, 5, 6, 1, 2, 3,]
li = [1,2,3]
deq.extend(li)
print(deq)
deq.extendleft(li) # deque 왼쪽에 list의 원소들이 역순으로 추가됨
print(deq)

deq.insert(0, 0)
print(deq)
deq.remove(0)
print(deq)

print(deq.count(4))
print(deq.index(4)) #  4의 인덱스를 찾아줌. 2개가 있을 땐 앞에 있는 원소의 인덱스만 반환함.

print("deq:", deq)
print("합:", sum(deq))

print("==== clear ====")
deq.clear()
print("deq:", deq)

print("길이:", len(deq))