import tkinter as tk
from tkinter import messagebox
import random
import time

class Minesweeper:
    def __init__(self, master):
        self.master = master
        self.master.title("Minesweeper")

        self.rows = 9
        self.columns = 9
        self.mines = 10
        self.flags = 0
        self.start_time = None
        self.running = False

        self.buttons = {}
        self.board = []
        self.create_widgets()
        self.create_board()
        self.place_mines()
        self.calculate_numbers()

    def create_widgets(self):
        self.timer_label = tk.Label(self.master, text="Time: 0", font=("Helvetica", 14))
        self.timer_label.grid(row=0, column=0, columnspan=self.columns)

        for x in range(self.rows):
            for y in range(self.columns):
                b = tk.Button(self.master, width=3, height=1,
                              command=lambda x=x, y=y: self.reveal_cell(x, y))
                b.bind("<Button-3>", lambda event, x=x, y=y: self.flag_cell(x, y))
                b.grid(row=x + 1, column=y)
                self.buttons[(x, y)] = b

        self.master.after(1000, self.update_timer)

    def create_board(self):
        self.board = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.mines:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            if self.board[x][y] != "M":
                self.board[x][y] = "M"
                mines_placed += 1

    def calculate_numbers(self):
        for x in range(self.rows):
            for y in range(self.columns):
                if self.board[x][y] == "M":
                    continue
                count = 0
                for i in range(max(0, x-1), min(self.rows, x+2)):
                    for j in range(max(0, y-1), min(self.columns, y+2)):
                        if self.board[i][j] == "M":
                            count += 1
                self.board[x][y] = count

    def reveal_cell(self, x, y):
        if not self.running:
            self.start_time = time.time()
            self.running = True

        button = self.buttons[(x, y)]
        if button["state"] == "disabled":
            return

        button.config(state="disabled", relief="sunken")

        value = self.board[x][y]
        if value == "M":
            button.config(text="💣", background="red")
            self.game_over(False)
        elif value == 0:
            button.config(text="", background="#ccc")
            for i in range(max(0, x-1), min(self.rows, x+2)):
                for j in range(max(0, y-1), min(self.columns, y+2)):
                    if (i, j) != (x, y):
                        self.reveal_cell(i, j)
        else:
            button.config(text=str(value), background="#ddd")

        self.check_win()

    def flag_cell(self, x, y):
        button = self.buttons[(x, y)]
        if button["state"] == "disabled":
            return
        current = button["text"]
        if current == "":
            button.config(text="🚩", disabledforeground="red")
            self.flags += 1
        elif current == "🚩":
            button.config(text="")
            self.flags -= 1

    def game_over(self, won):
        for (x, y), button in self.buttons.items():
            if self.board[x][y] == "M":
                button.config(text="💣", state="disabled")
        msg = "🎉 You Win!" if won else "💣 Game Over!"
        if won:
            elapsed = int(time.time() - self.start_time)
            messagebox.showinfo("Minesweeper", f"You Win! 🏆\nTime: {elapsed} seconds")
        else:
            messagebox.showerror("Minesweeper", "You hit a bomb 💣 !\nBetter luck next time.")

        self.running = False

    def check_win(self):
        for (x, y), button in self.buttons.items():
            if self.board[x][y] != "M" and button["state"] != "disabled":
                return
        self.game_over(True)

    def update_timer(self):
        if self.running:
            elapsed = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed}")
        self.master.after(1000, self.update_timer)


if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()
