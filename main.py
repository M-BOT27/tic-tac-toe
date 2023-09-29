import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize variables
player_x = "X"
player_o = "O"
current_player = player_x
game_board = [""] * 9

# Function to handle button click
def handle_click(index):
    global current_player
    if game_board[index] == "" and not check_winner():
        game_board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")
        if current_player == player_x:
            current_player = player_o
        else:
            current_player = player_x
    check_winner()

# Check if there's a winner
def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    
    for combo in winning_combinations:
        if game_board[combo[0]] == game_board[combo[1]] == game_board[combo[2]] != "":
            messagebox.showinfo("Tic Tac Toe", f"Player {game_board[combo[0]]} wins!")
            root.quit()
            return True
    
    if "" not in game_board:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        root.quit()
        return True

# Create the game board
row = 0
col = 0
buttons = []
for index in range(9):
    button = tk.Button(root, text="", height=3, width=6, font=("Helvetica", 24))
    button.config(command=lambda idx=index: handle_click(idx))
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 2:
        col = 0
        row += 1
    buttons.append(button)


root.mainloop()
