def solution(board, moves):
    answer = 0
    basket = []
    # 인형뽑기 문제
    # 리스트의 기본기능만 사용하여 간단히 구현가능
    for move in moves:
        for r in range(len(board[0])):
            if(board[r][move-1]!=0):
                basket.append(board[r][move-1])
                board[r][move-1] = 0
                if(len(basket)>=2 and basket[-1]==basket[-2]):
                    basket.pop()
                    basket.pop()
                    answer += 2
                break
    return answer