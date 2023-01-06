# 그래프를 보고 직적 값을 넣을 때
# 정점과 간선 표현

# a - b
# | \ |
# c   d
edge1 = [[1, 2], [1, 3], [1, 4], [2, 4]]

# 가중치 O - 딕셔너리 사용
# A, B, C, D

a, b, c, d = range(1, 5)
edge2 = [[a, b], [a, c], [a, d], [b, d]]

print(edge1)
print(edge2)
