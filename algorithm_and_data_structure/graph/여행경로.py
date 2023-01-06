adjMap = {}
answer = []

def solution(tickets):
    for ticket in tickets:
        start = ticket[0]
        end = ticket[1]

        adjMap[start] = adjMap[start] + [end] if start in adjMap else [end]

    tour("ICN")
    return answer

def tour(start):
    answer.append(start)
    if (start in adjMap and len(adjMap[start]) > 0):
        end = sorted(adjMap[start])[0]
        adjMap[start].remove(end)
        tour(end)
        
    
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# route = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
route = ["ICN", "JFK", "HND", "IAD"]

print(solution(tickets))