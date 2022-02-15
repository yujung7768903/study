import sys
from collections import deque

deq = deque()

n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push_front":
        deq.appendleft(command[1])
    elif command[0] == "push_back":
        deq.append(command[1])
    elif command[0] == "pop_front":
        print(-1 if not deq else deq.popleft())
    elif command[0] == "pop_back":
        print(-1 if not deq else deq.pop())
    elif command[0] == "size":
        print(len(deq))
    elif command[0] == "empty":
        print(1 if not deq else 0)
    elif command[0] == "front":
        print(-1 if not deq else deq[0])
    else:
        print(-1 if not deq else deq[-1])
