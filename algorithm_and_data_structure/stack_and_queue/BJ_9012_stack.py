import sys

n = int(input())

def check_vps(value):
    predicate = 0
    for item in value:
        if item == "(":
            predicate += 1 
        elif item == ")": 
            predicate -= 1;
        
        if predicate < 0:
            return "NO"

    return "YES" if predicate == 0 else "NO"

for i in range(n):
    input_value = sys.stdin.readline().split("\n")[0]
    print(check_vps(input_value))