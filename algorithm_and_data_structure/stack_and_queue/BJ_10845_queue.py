# 1
# Time: 132ms

# import queue
# import sys

# que = queue.Queue()

# def push(x):
#     que.put(x)

# def pop():
#     print(-1) if que.empty() else print(que.get())

# def size():
#     print(len(que.queue))

# def empty():
#     print(1) if que.empty() else print(0)

# def front():
#     print(-1) if que.empty() else print(que.queue[0])

# def back():
#     print(-1) if que.empty() else print(que.queue[-1])

# n = int(sys.stdin.readline())

# for i in range(n):
#     command = sys.stdin.readline().split('\n')[0].split(' ')
#     if command[0] == 'push':
#         push(command[1])
#     elif command[0] == 'pop':
#         pop()
#     elif command[0] == 'size':
#         size()
#     elif command[0] == 'empty':
#         empty()
#     elif command[0] == 'front':
#         front()
#     else:
#         back()


# 2
# Time: 80ms

import sys

que = []


def push(x):
    que.append(x)

def pop():
    print(-1) if len(que) == 0 else print(que.pop(0))

def size():
    print(len(que))

def empty():
    print(1) if len(que) == 0 else print(0)

def front():
    print(-1) if len(que) == 0 else print(que[0])

def back():
    print(-1) if len(que) == 0 else print(que[-1])

n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split('\n')[0].split(' ')
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    else:
        back()