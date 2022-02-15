s = input()

list_string = []

for i in range(len(s)):
    list_string.append(s[i:])
    print(list_string)

# sort vs sorted
# sort는 리턴값이 None, sorted는 정렬된 값을 리턴함
print("결과:", sorted(list_string))
for i in sorted(list_string):
    print(i)