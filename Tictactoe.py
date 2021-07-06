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

# main function which includes the gameplay functionality


def game():

    player1 = 'X'
    player2 = 'O'

    # 9 is the maxium amount of available moves
    for i in range(9):
        showBoard(board)
        # if turn count can't be divided by 2, it must be player 2's turn
        if i % 2:
            # turn is over after a valid move is made
            while True:
                print('player 2, please make your move')
                try:
                    move = input() 
                    if board[move] == ' ':
                        board[move] = player2
                        break
                    else:
                        print('That move has already been made, please make another move')
                except (ValueError, TypeError, KeyError):
                    print('Invalid input')
        # if turn count can be divided by 2, it must be player 1's turn
        else: 
            while True:
                print('player 1, please make your move')
                try:
                    move = input() 
                    if board[move] == ' ':
                        board[move] = player1
                        break
                    else:
                        print('That move has already been made, please make another move')
                except (ValueError, TypeError, KeyError):
                    print('Invalid input')

        # after 5 moves a win is possible
        if i >= 4:
            # each individual winning pattern is checked
            if board['1'] == board['2'] == board['3'] != ' ':
                if board['1'] == 'X':
                    print('***********************')
                    showBoard(board)
                    print('player 1 won the game')
                    break
                else:
                    print('***********************')
                    showBoard(board)
                    print('player 2 won the game')
                    break

            elif board['4'] == board['5'] == board['6'] != ' ':
                if board['4'] == 'X':
                    print('***********************')
                    showBoard(board)
                    print('player 1 won the game')
                    break
                else:
                    print('***********************')
                    showBoard(board)
                    print('player 2 won the game')
                    break

            elif board['7'] == board['8'] == board['9'] != ' ':
                if board['7'] == 'X':
                    print('***********************')
                    showBoard(board)
                    print('player 1 won the game')
                    break
                else:
                    print('***********************')
                    showBoard(board)
                    print('player 2 won the game')
                    break

            elif board['1'] == board['4'] == board['7'] != ' ':
                if board['1'] == 'X':
                    print('***********************')
                    showBoard(board)
                    print('player 1 won the game')
                    break
                else:
                    print('***********************')
                    showBoard(board)
                    print('player 2 won the game')
                    break

            elif board['2'] == board['5'] == board['8'] != ' ':
                if board['2'] == 'X':
                    print('***********************')
                    showBoard(board)
                    print('player 1 won the game')
                    break
                else:
                    print('***********************')
                    showBoard(board)
                    print('player 2 won the game')
                    break

            elif board['3'] == board['6'] == board['9'] != ' ':
                if board['3'] == 'X':
                    print('***********************')
                    showBoard(board)
                    print('player 1 won the game')
                    break
                else:
                    print('***********************')
                    showBoard(board)
                    print('player 2 won the game')
                    break

            elif board['1'] == board['5'] == board['9'] != ' ':
                if board['1'] == 'X':
                    print('***********************')
                    showBoard(board)
                    print('player 1 won the game')
                    break
                else:
                    print('***********************')
                    showBoard(board)
                    print('player 2 won the game')
                    break

            elif board['7'] == board['5'] == board['3'] != ' ':
                if board['7'] == 'X':
                    print('***********************')
                    showBoard(board)
                    print('player 1 won the game')
                    break
                else:
                    print('***********************')
                    showBoard(board)
                    print('player 2 won the game')
                    break

            else:
                print('***********************')
                showBoard(board)
                print('The game is a draw')

    #rematch option + reset board      
    rematch = input('Rematch?(y/n)')
    if rematch == 'y' or rematch == 'Y':
        for keys in board:
            board[keys] = ' '
        game()
    
    else: exit


if __name__ == "__main__":
    game()