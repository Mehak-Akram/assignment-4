import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe (AI)")

current_player = "X"  
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def make_move(row, col):
    global current_player

    if board[row][col] == "" and current_player == "X":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O"
            root.after(500, ai_move)  

def ai_move():
    global current_player

    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move:
        row, col = best_move
        board[row][col] = "O"
        buttons[row][col].config(text="O")

    if check_winner("O"):
        messagebox.showinfo("Game Over", "AI (O) wins!")
        reset_game()
    elif check_draw():
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()
    else:
        current_player = "X"

def minimax(board_state, depth, is_maximizing):
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board_state[i][j] == "":
                    board_state[i][j] = "O"
                    score = minimax(board_state, depth + 1, False)
                    board_state[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board_state[i][j] == "":
                    board_state[i][j] = "X"
                    score = minimax(board_state, depth + 1, True)
                    board_state[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw():
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            root,
            text="",
            font=("Arial", 40),
            width=5,
            height=2,
            command=lambda row=i, col=j: make_move(row, col)
        )
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
