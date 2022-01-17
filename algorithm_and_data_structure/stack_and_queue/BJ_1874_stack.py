import sys

repeat = int(input())
stack = []
push_or_pop = []
push_count = 1
result = ""


def make_sequence(value):
    global push_count
    if value >= push_count:
        for i in range(push_count, value + 1):
            stack.append(i)
            push_count += 1
            push_or_pop.append("+")
        stack.pop()
        push_or_pop.append("-")
        return push_or_pop
    elif value == stack[-1]:
        stack.pop()
        push_or_pop.append("-")
        return push_or_pop
    else:
        return "NO"

def print_result(result):
    if result == "NO":
        print("NO")
    else:
        print("\n".join(result))
    
for i in range(repeat):
    input_value = int(sys.stdin.readline().split("\n")[0])
    if result == "NO":
        continue
    result = make_sequence(input_value)
print_result(result)
