# stack 만들기
# size(), isEmpty(), push(), pop(), top()
# push() -> push(5) -> push(3) -> pop() -> push(4)

from collections import deque

stack = deque()

def size():
    print(len(stack))

def isEmpty():
    print(True if not stack else False)

def push(n):
    stack.append(n)

def pop():
    print(stack.pop())

def top():
    return stack[-1]

push(7)
push(5)
push(3)
push(2)
pop()
pop()
push(4)
print(stack)