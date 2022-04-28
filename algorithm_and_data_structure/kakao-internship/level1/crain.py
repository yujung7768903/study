def solution(board, moves):
    basket = []
    answer = 0
    for i in moves:
        print(f"===={i}번째 줄====")
        for j in range(len(board)):
            if board[j][i-1] > 0:
                print(f"🤡[{j}][{i-1}]위치의 인형 뽑음.")
                basket.append(board[j][i-1])
                board[j][i-1] = 0
                print(basket)
                break
        if len(basket) >=2 and basket[-1] == basket[-2]:
            basket = basket[0:-2]
            answer += 2      
            
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))