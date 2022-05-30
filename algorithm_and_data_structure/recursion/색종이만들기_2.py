import sys
n = int(sys.stdin.readline())
square = [] # 여러 개의 칸들로 이루어진 정사각형 종이
white_num = 0
blue_num = 0

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    square.append(row)

def recursion(size, part):
    part1, part2, part3, part4 = [], [] , [], []
    for i in part[0:(size // 2)]:
        part1.append(i[0:(size // 2)])
        part2.append(i[(size //2):])
    for j in part[(size //2):]:
        part3.append(j[0:(size // 2)])
        part4.append(j[(size //2):])
    for k in [part1, part2, part3, part4]:
        classify_same_color(k)
        

def classify_same_color(part):
    global white_num
    global blue_num
    present_item = part[0][0]
    for row in range(len(part)):
        for col in range(len(part)):
            if part[row][col] != present_item:
                print(f"색이 다름 | {part}")
                return recursion(len(part), part)
    # 색이 모두 같은 경우
    if present_item:
        print(f"🔵 색이 같음 | {part}")
        blue_num += 1
    else:
        print(f"⚪️ 색이 같음 | {part}")
        white_num += 1


classify_same_color(square)
print(f"하얀색 색종이 개수: {white_num}")
print(f"파란색 색종이 개수: {blue_num}")