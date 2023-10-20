import tkinter as tk
from tkinter import messagebox
import math

# The board is represented as a list of 9 cells, indexed 0-8, left to right, top to bottom.
# Each cell can be 'X', 'O', or empty ' '.
board = [' ' for _ in range(9)]

# Define the winning combinations
WINNING_COMBINATIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                        (0, 4, 8), (2, 4, 6)]  # Diagonals

# Function to check if the game is over (either one player wins or it's a draw)
def is_game_over(board):
    for combo in WINNING_COMBINATIONS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return True, board[combo[0]]
    if ' ' not in board:
        return True, 'Draw'
    return False, None

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, maximizing_player):
    # Terminal state: return the score
    game_over, winner = is_game_over(board)
    if game_over:
        if winner == 'X':
            return -1
        elif winner == 'O':
            return 1
        else:
            return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for the AI
def find_best_move(board):
    best_move = -1
    best_eval = -math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = i
    return best_move

# Function to handle the player's move
def player_move(index):
    if board[index] == ' ':
        board[index] = 'X'
        buttons[index].config(text='X')
        game_over, winner = is_game_over(board)
        if game_over:
            end_game(winner)
        else:
            ai_move()

# Function to make the AI's move
def ai_move():
    if not is_game_over(board)[0]:
        index = find_best_move(board)
        board[index] = 'O'
        buttons[index].config(text='O')
        game_over, winner = is_game_over(board)
        if game_over:
            end_game(winner)

# Function to reset the game
def reset_game():
    global board
    for i in range(9):
        board[i] = ' '
        buttons[i].config(text=' ')
    result_label.config(text='')
    play_button.config(state=tk.NORMAL)

# Function to start a new game
def start_new_game():
    reset_game()
    play_button.config(state=tk.DISABLED)

# Function to end the game and display the result
# Function to end the game and display the result
def end_game(winner):
    for button in buttons:
        button.config(state=tk.DISABLED)
    if winner == 'Draw':
        result_label.config(text="It's a draw!")
        messagebox.showinfo("Game Over", "It's a draw!")
    else:
        if winner == 'O':
            result_label.config(text="AI wins!")
            messagebox.showinfo("Game Over", "AI wins!")
        else:
            result_label.config(text="Human wins!")
            messagebox.showinfo("Game Over", "Human wins!")

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create buttons for the game board
buttons = []
for i in range(9):
    button = tk.Button(window, text=' ', width=10, height=3, command=lambda i=i: player_move(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Create a label to display the result
result_label = tk.Label(window, text='', font=('Helvetica', 16))
result_label.grid(row=3, columnspan=3)

# Create a "Reset" button
reset_button = tk.Button(window, text="Reset", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=2)

# Create a "AI vs Human" button to start a new game
play_button = tk.Button(window, text="AI vs Human", command=start_new_game)
play_button.grid(row=4, column=2, columnspan=2)

# Start the game
window.mainloop()

