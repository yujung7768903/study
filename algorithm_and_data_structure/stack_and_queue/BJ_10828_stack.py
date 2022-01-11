import sys

def push(x):
    stack.append(x)

# def pop():
#     if len(stack) == 0:
#         print(-1)
#     else:
#         n = stack[-1]
#         stack.pop()
#         print(n)

# one-linear
def pop():
    print(-1) if len(stack) == 0 else print(stack[-1])

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

stack = []

n = sys.stdin.readline();

for i in range(int(n)):
    input_value = sys.stdin.readline().split("\n")[0]
    command = input_value.split(" ")
    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    else:
        top()