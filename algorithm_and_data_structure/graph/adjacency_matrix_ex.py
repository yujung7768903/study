# 그래프를 보고 직접 값을 넣을 때
# 인접 행렬

# 가중치 x - (0, 1로 표현)
# a - b
# | \ |
# c   d

adjacency_matrix = [[], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0]]

print(bool(adjacency_matrix[1][2])) # 1번과 2번 노드의 연결
print(bool(adjacency_matrix[2][3])) # 2번과 3번 노드의 연결
print(sum(adjacency_matrix[1])) # 1번 노드의 차수

# 가중치 o (0, 가중치로 표현)
a, b, c, d = range(1, 5)
adjacency_matrix = [[], [0, 0, 3, 1, 7], [0, 3, 0, 0, 2], [0, 1, 0, 0, 0], [0, 7, 2, 0, 0]]

print(bool(adjacency_matrix[a][b])) # a번과 b번 노드의 연결
print(bool(adjacency_matrix[b][c])) # b번과 c번 노드의 연결
print(len(adjacency_matrix[a]) - adjacency_matrix[a].count(0)) # a노드의 차수
print(adjacency_matrix[a][d]) # a와 d 노드의 가중치