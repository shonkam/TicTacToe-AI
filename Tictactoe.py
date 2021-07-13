# setup board
board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}


# prints board to the console/terminal
def showBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# finds the best move for the AI player using minimax algorithm
def AIMove():
    bestScore = -500
    bestMove = 0
    # goes through every open position on the board
    for key in board.keys():
        if board[key] == ' ':
            board[key] = AIMark
            score = minimax(board, False)
            board[key] = ' '
            # saves the highest reward position
            if score > bestScore:
                bestScore = score
                bestMove = key
    # returns the move that return the highest reward
    return bestMove

# minimax algorithm is used to calculate the best move for the AI player
def minimax(board, isMaximizing):

    # negative reward for player win
    if checkWin() == 1:
        return -10
    # positive reward for AI win
    elif checkWin() == 2:
        return 10
    # 0 rewards for draw
    elif checkDraw():
        return 0

    if (isMaximizing):
        bestScore = -500

        for key in board.keys():
            if board[key] == ' ':
                board[key] = AIMark
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score

        return bestScore

    else:
        bestScore = 500
        for key in board.keys():
            if board[key] == ' ':
                board[key] = playerMark
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


# asks for AI/human player to make a move
def makeMove(mark):
    while True:
        if(mark == 'X'):
            print('Player, please make your move')
            try:
                move = input()
                if board[move] == ' ':
                    board[move] = mark
                    break
                else:
                    print('That move has already been made, please make another move')
            except (ValueError, TypeError, KeyError):
                print('Invalid input')
        else:
            print('AI, make your move')
            computerMove = AIMove()
            board[computerMove] = AIMark
            break

# checks if the game ends in a draw
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

# checks if there is winner
def checkWin():
    # each individual winning pattern is checked
    if board['1'] == board['2'] == board['3'] != ' ':
        if board['1'] == 'X':
            return 1
        else:
            return 2
    elif board['4'] == board['5'] == board['6'] != ' ':
        if board['4'] == 'X':
            return 1
        else:
            return 2
    elif board['7'] == board['8'] == board['9'] != ' ':
        if board['7'] == 'X':
            return 1
        else:
            return 2
    elif board['1'] == board['4'] == board['7'] != ' ':
        if board['1'] == 'X':
            return 1
        else:
            return 2
    elif board['2'] == board['5'] == board['8'] != ' ':
        if board['2'] == 'X':
            return 1
        else:
            return 2
    elif board['3'] == board['6'] == board['9'] != ' ':
        if board['3'] == 'X':
            return 1
        else:
            return 2
    elif board['1'] == board['5'] == board['9'] != ' ':
        if board['1'] == 'X':
            return 1
        else:
            return 2
    elif board['7'] == board['5'] == board['3'] != ' ':
        if board['7'] == 'X':
            return 1
        else:
            return 2

# rematch
def rematch(val):
    if val == 'y' or val == 'Y':
        return True
    else:
        return False

# follows the amount of moves and prints the outcome 
def game():

    turn = playerMark

    # 9 is the maxium amount of available moves
    for i in range(9):
        showBoard(board)
        # if turn count can't be divided by 2, it must be player 2's turn
        if i % 2:
            turn = AIMark
        else:
            turn = playerMark
        makeMove(turn)

        # after 5 moves a win is possible
        if i >= 4:
            if checkWin() == 1:
                print('****************')
                showBoard(board)
                print('****************')
                print('Player won')
                print('****************')
                break
            elif checkWin() == 2:
                print('****************')
                showBoard(board)
                print('****************')
                print('AI won')
                print('****************')
                break
            elif checkDraw():
                print('****************')
                showBoard(board)
                print('****************')
                print('Draw')
                print('****************')

    #ask for rematch
    val = input('Rematch?(y/n)')
    if rematch(val):
        for keys in board:
            board[keys] = ' '
        game()
    else:
        exit()

playerMark = 'X'
AIMark = 'O'

if __name__ == "__main__":
    game()
