def solution(board, skill):
    count = 0
    imos = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for s in skill:
        t, r1, c1, r2, c2, degree = s

        # 공격
        if t == 1:
            imos[r1][c1] -= degree
            imos[r1][c2 + 1] += degree
            imos[r2 + 1][c1] += degree
            imos[r2 + 1][c2 + 1] -= degree
        # 회복
        elif t == 2:
            imos[r1][c1] += degree
            imos[r1][c2 + 1] -= degree
            imos[r2 + 1][c1] -= degree
            imos[r2 + 1][c2 + 1] += degree
    print(imos)
    # 왼쪽에서부터 오른쪽으로 누적합 구하기
    for row in range(len(imos)):
        for column in range(1, len(imos[0])):
            imos[row][column] += imos[row][column - 1]
    # 위쪽에서부터 아래로 누적합 구하기
    for column in range(len(imos[0])):
        for row in range(1, len(imos)):
            imos[row][column] += imos[row - 1][column]

    for row in range(len(board)):
        for column in range(len(board[0])):
            board[row][column] += imos[row][column]

            if board[row][column] > 0:
                count += 1

    return count


board_ex = [[1,2,3],[4,5,6],[7,8,9]]
skill_ex = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board_ex, skill_ex))