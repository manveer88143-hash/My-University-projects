# simple Tic tac toe game human vs human

board = ["1","2","3","4","5","6","7","8","9"]

def print_board(board):
    print(f"{board[0]}  | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f"{board[3]}  | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f"{board[6]}  | {board[7]} | {board[8]}")
    print()

  
''' ask player to enter position'''
def player_input(board , player):
    while True:
        try:
            position = int(input(f"player {player} enter your number (1-9): "))
            if position < 1 or position > 9:
                print("invalid input. Please enter number between 1 and 9")
                continue
            # board is 0-indexed; convert
            idx = position - 1
            if board[idx] in ['X', 'O']:
                print("position is already taken, please choose another position")
                continue
            else:
                board[idx] = player
                break
        except ValueError:
            print("invalid input. Please enter a valid number between 1-9")    
            
def check_winner(board):
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8], #row
        [0,3,6], [1,4,7], [2,5,8], #column
        [0,4,8], [2,4,6]  #diagnols
    ]         

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    return None

def play_game():
    board = [str(i) for i in range(1,10)]
    current_player = "X"
    for turn in range(9):
        print_board(board)
        player_input(board, current_player)
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"congratulations! player {winner} wins!")
            return winner
        current_player = "O" if current_player == "X" else "X"
    print_board(board)
    print("It's a tie!")
    return "Tie"


if __name__ == '__main__':
    play_game()            