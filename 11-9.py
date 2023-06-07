matrix = []
def drawBoard():
    for i in range(3):
        print('---------------')
        for j in range(3):
            print('|',matrix[i][j],' ',end=' ')
        print('|')
    print('---------------')
def check():
    for i in range(3):
        player = matrix[i][0] #i행 3개 열 (가로검사)
        if player != ' 'and player==matrix[i][1] and player==matrix[i][2]:
            return player
        player = matrix[0][i] #i열 3개 행 (세로검사)
        if player != ' ' and player == matrix[1][i] and player == matrix[2][i]:
            return player
        #대각선 검사
        player = matrix[0][0]
        if player != ' 'and player == matrix[1][1] and player == matrix[2][2]:
            return player
        player = matrix[0][2]
        if player != ' ' and player == matrix[1][1] and player == matrix[2][0]:
            return player
        return ' '
def main():
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(' ')
    drawBoard()
    turn = True
    for i in range(9):
        if turn: #X플레이어 차례
            row = eval(input('플레이어 x의 행(0,1, 또는 2) 입력:'))
            col = eval(input('플레이어 x의 열(0,1, 또는 2) 입력:'))
            matrix[row][col] = 'X'
        else: #O플레이어 차례
            row = eval(input('플레이어 x의 행(0,1, 또는 2) 입력:'))
            col = eval(input('플레이어 x의 열(0,1, 또는 2) 입력:'))
            matrix[row][col] = 'O'
        drawBoard()
        player = check()
        if player != '':
            print('플레이어', player, '가 이겼습니다.')
            break
        turn = not turn
    if i == 9:
        print('비겼습니다.')
main()