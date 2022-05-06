def solution(board, skill):
    answer = len(board) * len(board[0])
    for item in skill:
        type = item[0]
        degree = item[5]
        
        if type == 1: # 적의 공격
            print("=== 적의 공격 ===")
            print(board)
            for x in range(item[1], item[3] + 1):
                for y in range(item[2], item[4] + 1):
                    # 건물이 파괴되는 경우 (원래는 1이상 -> 0 또는 음수)
                    if board[x][y] > 0 and board[x][y] <= degree:
                        print(f"(파괴됨 / ({x}, {y}) = {board[x][y]})")
                        answer -= 1
                    board[x][y] -= degree
            print(board)
                    
        else: # 아군 지원
            print("=== 아군 지원 ===")
            print(board)
            for x in range(item[1], item[3] + 1):
                for y in range(item[2], item[4] + 1):
                    if board[x][y] <= 0 and abs(board[x][y]) < degree:
                        print(f"(복구됨 / ({x}, {y}) = {board[x][y]})")
                        answer += 1
                    board[x][y] += degree
            print(board)

    return answer


board_ex = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill_ex = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board_ex, skill_ex))

# skill x board = 250,000 x 1,000 x 1,000 = 250,000,000,000