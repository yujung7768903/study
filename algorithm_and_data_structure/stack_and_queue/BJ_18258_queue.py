# 시간초과로 문제를 틀림
# queue를 import해서 쓸 때 더 오래걸림
# 파이썬 리스트의 가장 앞의 데이터를 지우면, 데이터를 인덱스에 맞게 한 칸씩 앞으로 당겨서 다시 써주게 됨 -> 시간복잡도 0(n)
# 가장 앞을 가르키는 인덱스값을 변수로 만들어 사용

import sys

que = []
que_size = 0
pop_count = 0

def push(value):
    global que_size
    que.append(value)
    que_size += 1

def pop():
    global que_size
    global pop_count
    if que_size > 0:
        print(que[pop_count])
        pop_count += 1
        que_size -= 1
    else:
        print(-1)

def size():
    global que_size
    print(que_size)

def empty():
    print(1 if que_size == 0 else 0)

def front():
    print(-1 if que_size == 0 else que[pop_count])

def back():
    print(-1 if que_size == 0 else que[-1])

repeat = int(sys.stdin.readline().split('\n')[0])

for i in range(repeat):
    command = sys.stdin.readline().split('\n')[0].split()
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