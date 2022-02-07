# queue 만들기
# size(), isEmpty(), enqueue(), dequeue(), front()
# enqueue(7), enqueue(5), enqueue(3), enqueue(2), dequeue(), dequeue(), enqueue(4)

from collections import deque
import queue

que = deque()

# qsize는 큐의 대략의 크기를 돌려줍니다.
def size():
    print(len(que))

def empty():
    print(True if not que else False)

def enqueue(n):
    que.append(n)

# get()은 큐에서 항목을 제거하고 반환합니다. 선택적 인자 block이 참이고 timeout이 None(기본값)이면, 항목이 사용 가능할 때까지 필요하면 블록합니다.
def dequeue():
    print(que.popleft())

def front():
    return que[0]


enqueue(7)
enqueue(5)
enqueue(3)
dequeue()
dequeue()
enqueue(4)

print(que)
