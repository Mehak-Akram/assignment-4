#Implement an 'eraser' on a canvas.

#The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas,

#  sets all of the rectangles it is in contact with to white.

import tkinter as tk

WIDTH, HEIGHT = 400, 300
CELL_SIZE = 20
ERASER_SIZE = 40
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
PINK = "#FF69B4"  
WHITE = "#FFFFFF"

def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            x1, y1 = col * CELL_SIZE, row * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            cell = canvas.create_rectangle(x1, y1, x2, y2, fill=PINK, outline="black")
            grid[(row, col)] = cell

def erase_cells(event):
    x, y = event.x, event.y
    for (row, col), cell_id in grid.items():
        cell_x, cell_y = col * CELL_SIZE, row * CELL_SIZE
        if (cell_x < x < cell_x + CELL_SIZE + ERASER_SIZE and
            cell_y < y < cell_y + CELL_SIZE + ERASER_SIZE):
            canvas.itemconfig(cell_id, fill=WHITE)

def update_eraser(event):
    canvas.coords(eraser, event.x - ERASER_SIZE // 2, event.y - ERASER_SIZE // 2,
                  event.x + ERASER_SIZE // 2, event.y + ERASER_SIZE // 2)
    erase_cells(event)

root = tk.Tk()
root.title("Canvas Eraser")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=WHITE)
canvas.pack()

grid = {}
draw_grid()

eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="gray")

canvas.bind("<B1-Motion>", update_eraser)
canvas.bind("<Motion>", update_eraser)

root.mainloop()
