# def solution(citations):
#     answer = 1
#     citations.sort()
#     for index, number in enumerate(citations):
#         if len(citations) - index >= number: answer = number
#         else:
#             if len(citations) - index > answer: answer = len(citations) - index
#             break
#
#     return answer

def solution(citations):
    citations.sort(reverse=True)
    for i, j in enumerate(citations, start=1):
        print(f"i: {i}, j: {j}")
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


# citiations = [3, 0, 6, 1, 5] # 0, 1, 3, 5, 6
# citiations = [3]
# citiations = [1,1,100,101,102,103,104]
# citiations = [1,2,3,4,5]
citiations = [2, 4, 6, 8, 10, 12]
# citiations = [4,4,6,6,6,6,6]

print(solution(citiations))
