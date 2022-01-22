from collections import deque
import sys

deq = deque()

def push_front(value):
    deq.appendleft(value)

def push_back(value):
    deq.append(value)

def pop_front():
    print(-1 if not deq else deq.popleft())

def pop_back():
    print(-1 if not deq else deq.pop())

def size():
    print(len(deq))

def empty():
    print(1 if not deq else 0)

def front():
    print(-1 if not deq else deq[0])

def back():
    print(-1 if not deq else deq[-1])

repeat = int(input())

for i in range(repeat):
    c = sys.stdin.readline().strip()
    print(c)
    command = c.split()
    if command[0] == "push_front":
        push_front(command[1])
    elif command[0] == "push_back":
        push_back(command[1])
    elif command[0] == "pop_front":
        pop_front()
    elif command[0] == "pop_back":
        pop_back()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "front":
        front()
    else:
        back()