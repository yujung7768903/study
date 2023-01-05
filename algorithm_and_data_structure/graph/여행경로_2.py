import copy

adjMap = {} # key: 출발지, value: [도착지1, 도착지2, ...]
answerList = [] # 가능한 조합, 맨 첫번째 원소가 알파벳 순으로 앞서는 조합 (이러한 리스트를 만들지 않고도 더 좋은 방법이 있을듯함)

def solution(tickets):
    for ticket in tickets:
        adjMap[ticket[0]] = adjMap[ticket[0]] + [ticket[1]] if ticket[0] in adjMap else [ticket[1]]
    tour("ICN", [], adjMap)
    return answerList[0]

def tour(start, arr, tourMap):
    arr.append(start)
    print(f"start: {start}, arr: {arr}, tourMap: {tourMap}")
    if len(tourMap) == 0:
        answerList.append(arr)

    if start in tourMap:
        for end in sorted(tourMap[start]):
            newTourMap = copy.deepcopy(tourMap)
            newTourMap[start].remove(end)
            if len(newTourMap[start]) == 0: del newTourMap[start]
            tour(end, copy.deepcopy(arr), newTourMap)


# 🔽 TEST 🔽

# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [["A", "B"], ["A", "C"], ["C", "D"], ["D", "B"]]
# tickets = [['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

# print(solution(tickets))

