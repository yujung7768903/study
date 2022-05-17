input_value = input()

total = 0
list_s = []
for i in input_value:
    if i.isdigit(): total += int(i)
    else: list_s.append(i)

result = ''.join(sorted(list_s))
if total > 0:
    result += str(total)

print(result)