import random
import os.path
import json
random.seed()

def draw_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
    pass

def welcome(board):
    print("Welcome to the 'Unbeatable Noughts and Crosses!'Game.\nThe board layout is show below:" )
    draw_board(board)
    print("When prompted, enter the number correspondig to the square you want.")
    pass

def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    while True:
        try:
            move = input("Enter your move as row,col (e.g., 1,2): ")
            row, col = map(int, move.split(','))
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter row and col as numbers between 0 and 2.")
    return row,col

def choose_computer_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                if check_for_win(board, 'O'):
                    board[row][col] = ' '  
                    return row, col
                board[row][col] = ' '  

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_for_win(board, 'X'):
                    board[row][col] = ' '  
                    return row, col
                board[row][col] = ' '

    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)
    return row,col

def check_for_win(board, mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True

    for col in range(3):
        if all(row[col] == mark for row in board):
            return True

    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False


def check_for_draw(board):
    return all(cell != ' ' for row in board for cell in row)
    return True

def play_game(board):
    initialise_board(board)
    draw_board(board)
    
    while True:
        print("Player's turn (X):")
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("Congratulations! You win!")
            return 1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

        print("Computer's turn (O):")
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins! Better luck next time.")
            return -1
        if check_for_draw(board):
            print("It's a draw!")
            return 0


def menu():
    print("Main Menu:")
    print("1. Play the Game")
    print("2. Save your Score in the leaderboard")
    print("3. Load and disply the Leaderboard")
    print("q. End the program")
    return input("Enter your choice : ").strip()
    return choice

def load_scores():
    try:
        with open('leaderboard.txt', 'r') as file:
            scores = {}
            for line in file:
                name, score = line.strip().split(':')
                scores[name] = int(score)
            return scores
    except FileNotFoundError:
        return {}
    return leaders

def save_score(score):
    name = input("Enter your name: ").strip()
    with open('leaderboard.txt', 'a') as file:
        file.write(f"{name}:{score}\n")
    return

def display_leaderboard(leaders):
    print("Leaderboard:")
    for name, score in sorted(leaders.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {score}")
    pass
