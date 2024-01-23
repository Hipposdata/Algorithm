def solution(board, moves):
    answer = 0
    # 뽑힌 인형 저장할 빈 스택 정의
    stack = []
    # 인형뽑는 번호 칸 반복 
    for i in moves:
        # num-> 각 번호 칸의 높이 / j를 0으로 초기화
        num = 0  
        while num < len(board):
             # 인형을 만났을 때
            if board[num][i-1] != 0: 
                # 스택에 인형이 존재하고 뽑힌 인형과 스택에 쌓인 마지막 인형과 같은 경우
                if len(stack) > 0 and stack[-1] == board[num][i-1]:  
                    stack.pop()  # 스택에서 해당 인형 제거
                    answer += 2  # 인형 두 개가 사라지므로 +2
                else:
                    stack.append(board[num][i-1])  # 스택에 인형 추가
                board[num][i-1] = 0  # 뽑기 기계속 인형 제거
                break  # 다음 move로 넘어감
            num += 1  # 높이 한칸 줄어듬 
    return answer