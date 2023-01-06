from collections import deque
from time import time
from unittest import result

def bfs(al, co, time, pos_problem, impos_problem):
    que = deque()
    que.append((al, co, time))
    result = []
    while que[-1][0] < impos_problem[0] or que[-1][1] < impos_problem[1]:
        x, y, cost = que.pop()
        # 공부할 때
        x1, y1, cost1 = x, y, cost
        if impos_problem[0] > x:
            cost1 += (impos_problem[0] - x)
            x1 = impos_problem[0]
        if impos_problem[1] > y:
            cost1 += (impos_problem[1] - y)
            y1 = impos_problem[1]
        que.append((x1, y1, cost1))
        if not result:
            result = [x1, y1, cost1]
        elif result and result[-1] > cost1:
            result = [x1, y1, cost1]
            
        print(que)
        # 문제풀 때
        x2 = x + pos_problem[2]
        y2 = y + pos_problem[3]
        cost2 = cost + pos_problem[4]
        que.append((x2, y2, cost2))
        print(que)
    if result and result[-1] > cost2:
        result = [x2, y2, cost2]
    
    print(result)
    return result[0], result[1], result[2]
        

def solution(alp, cop, problems):
    answer = 0
    list_pos_problem = [] # 풀 수 있는 문제
    list_impos_problem = problems # 못 푸는 문제
    problems.sort()
    # 풀 수 있는 문제 모두 풀기 & 풀 수 있는 문제와 못 푸는 문제 분류하기
    while alp < problems[-1][0] or cop < problems[-1][1]:
        print("=============================")
        print(f"📍현재: 알고력 {alp}, 코딩력 {cop}")
        problem = list_impos_problem[0]
        print(f"📍문제: {problem}")
        if alp >= problem[0] and cop >= problem[1]: # 문제 풀기
            alp += problem[2]
            cop += problem[3]
            answer += problem[4]
            list_pos_problem.append(problem)
            list_impos_problem.remove(problem)
            print(f"누적 시간: {answer}")
        elif not len(list_pos_problem): # 풀 수 있는 문제가 없을 때
            # 공부한 시간
            if problem[0] > alp:
                study_time += (problem[0] - alp)
            if problem[1] > cop:
                study_time += (problem[1] - cop)
            print(f"공부할 때 걸리는 시간: {study_time}")
            alp = problem[0]
            cop = problem[1]
            answer += study_time
            print(f"공부 후: 알고력 {alp}, 코딩력 {cop}, 소요시간: {study_time}")
            print(f"누적 시간: {answer}")
        else:
            print(f"bfs({alp}, {cop}, {answer}, {list_pos_problem[-1]}, {problem})")
            alp, cop, answer = bfs(alp, cop, answer, list_pos_problem[-1], problem)
            list_pos_problem.append(problem)
            list_impos_problem.remove(problem)

    return answer

# ex1
ex1_alp = 0
ex1_cop = 0
ex1_problems = [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
print(solution(ex1_alp, ex1_cop, ex1_problems))