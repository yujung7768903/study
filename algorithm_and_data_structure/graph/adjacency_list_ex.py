# 그래프를 보고 직적 값을 넣을 때
# 인접 리스트

# 가중치 x - 리스트 사용
# A=1, B=2, C=3, D=4

# a - b
# | \ |
# c   d

adjacency_list = [[], [2, 3, 4], [1, 4], [1], [1, 2]]

print(2 in adjacency_list[1]) # 1번과 2번 노드의 연결
print(3 in adjacency_list[2]) # 2번과 3번 노드의 연결
print(len(adjacency_list[1])) # 1번 노드의 차수

a, b, c, d = range(1, 5)
adjacency_list2 = [{}, {b: 3, c: 1, d: 7}, {a: 3, d: 2}, {a: 1}, {a: 7, b: 2}]
print(b in adjacency_list2[a]) # a번과 b번 노드의 연결
print(b in adjacency_list2[c]) # b번과 c번 노드의 연결
print(len(adjacency_list2[a])) # a번 노드의 차수
print(adjacency_list2[a][d]) # a와 b 노드의 가중치