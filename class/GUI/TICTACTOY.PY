import tkinter as tk
from tkinter import messagebox
import random

# --- Game Setup ---
root = tk.Tk()
root.title("Tic-Tac-Toe 🤖")
root.configure(bg="#2b2d42")

# --- Global Variables ---
player = "X"
ai = "O"
buttons = [[None for _ in range(3)] for _ in range(3)]
game_active = True

# --- Functions ---
def is_moves_left(board):
    return any(cell["text"] == "" for row in board for cell in row)

def evaluate(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0]["text"] == board[i][1]["text"] == board[i][2]["text"]:
            if board[i][0]["text"] == ai:
                return 10
            elif board[i][0]["text"] == player:
                return -10
        if board[0][i]["text"] == board[1][i]["text"] == board[2][i]["text"]:
            if board[0][i]["text"] == ai:
                return 10
            elif board[0][i]["text"] == player:
                return -10

    # Diagonals
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]:
        if board[0][0]["text"] == ai:
            return 10
        elif board[0][0]["text"] == player:
            return -10

    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]:
        if board[0][2]["text"] == ai:
            return 10
        elif board[0][2]["text"] == player:
            return -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j]["text"] == "":
                    board[i][j]["text"] = ai
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j]["text"] = ""
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j]["text"] == "":
                    board[i][j]["text"] = player
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j]["text"] = ""
        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j]["text"] == "":
                board[i][j]["text"] = ai
                move_val = minimax(board, 0, False)
                board[i][j]["text"] = ""
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def highlight_winner(coords):
    global game_active
    for (i, j) in coords:
        buttons[i][j].config(bg="#8ac926")
    game_active = False

def check_winner():
    global game_active
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            highlight_winner([(i, 0), (i, 1), (i, 2)])
            return buttons[i][0]['text']
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            highlight_winner([(0, i), (1, i), (2, i)])
            return buttons[0][i]['text']
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        return buttons[0][0]['text']
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        return buttons[0][2]['text']
    if not is_moves_left(buttons):
        game_active = False
        return "Draw"
    return None

def ai_move():
    if not game_active:
        return
    i, j = find_best_move(buttons)
    buttons[i][j].config(text=ai, fg="#ffbe0b")
    winner = check_winner()
    if winner:
        end_game(winner)
        return
    turn_label.config(text="Your Turn (X)")

def end_game(winner):
    if winner == "Draw":
        messagebox.showinfo("Draw 🤝", "It's a draw!")
    elif winner == player:
        messagebox.showinfo("🎉 You Win!", "Congratulations! You defeated the AI!")
    else:
        messagebox.showinfo("💻 AI Wins!", "Better luck next time!")
    disable_buttons()

def disable_buttons():
    global game_active
    game_active = False

def enable_buttons():
    global game_active
    game_active = True
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="#3a506b")

def on_click(row, col):
    if not game_active or buttons[row][col]['text'] != "":
        return
    buttons[row][col].config(text=player, fg="#edf2f4")
    winner = check_winner()
    if winner:
        end_game(winner)
        return
    turn_label.config(text="AI's Turn (O)")
    root.after(600, ai_move)

def reset_game():
    enable_buttons()
    turn_label.config(text="Your Turn (X)")

# --- UI Layout ---
title = tk.Label(root, text="🤖 Tic-Tac-Toe AI", font=("Arial Rounded MT Bold", 28),
                 fg="#edf2f4", bg="#2b2d42")
title.pack(pady=10)

turn_label = tk.Label(root, text="Your Turn (X)", font=("Arial", 16),
                      fg="#edf2f4", bg="#2b2d42")
turn_label.pack(pady=5)

frame = tk.Frame(root, bg="#2b2d42")
frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(
            frame, text="", font=("Arial", 28, "bold"), width=5, height=2,
            bg="#3a506b", activebackground="#5bc0be", fg="#edf2f4",
            command=lambda r=i, c=j: on_click(r, c)
        )
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

reset_btn = tk.Button(root, text="🔁 Reset Game", font=("Arial", 14, "bold"),
                      bg="#ef233c", fg="white", activebackground="#d90429",
                      command=reset_game)
reset_btn.pack(pady=15)

root.mainloop()