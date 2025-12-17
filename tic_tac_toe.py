1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
import tkinter as tk
from tkinter import messagebox

# Window setup
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

# Players
current_player = "X"
buttons = []

def check_winner():
    for i in range(3):
        # Check rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        # Check columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

def on_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player

        if check_winner():
            messagebox.showinfo("Game Over", f"🎉 Player {current_player} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "🤝 It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""

# Create 3x3 grid of buttons
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# Run the game
root.mainloop()
