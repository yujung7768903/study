# stack 만들기
# size(), isEmpty(), push(), pop(), top()
# push() -> push(5) -> push(3) -> pop() -> push(4)

def size():
    print(len(stack))

def isEmpty():
    if len(stack) == 0:
        return True
    else: 
        return False

def push(n):
    stack.append(n)

def pop():
    n = stack[-1]
    stack.pop()
    return n

def top():
    return stack[-1]

stack = []

push(7)
push(5)
push(3)
push(2)
pop()
pop()
push(4)
print(stack)