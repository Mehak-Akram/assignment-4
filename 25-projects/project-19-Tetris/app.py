import pygame
import random

pygame.init()

WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30

COLUMNS = WIDTH // BLOCK_SIZE
ROWS = HEIGHT // BLOCK_SIZE

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  
    (0, 0, 255),    
    (255, 165, 0),  
    (255, 255, 0),  
    (0, 255, 0),    
    (160, 32, 240), 
    (255, 0, 0)     
]

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0],
     [1, 1, 1]],     # J
    [[0, 0, 1],
     [1, 1, 1]],     # L
    [[1, 1],
     [1, 1]],        # O
    [[0, 1, 1],
     [1, 1, 0]],     # S
    [[0, 1, 0],
     [1, 1, 1]],     # T
    [[1, 1, 0],
     [0, 1, 1]]      # Z
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris by Mehak")

clock = pygame.time.Clock()

def create_grid():
    return [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]

def draw_grid(grid):
    for y in range(ROWS):
        for x in range(COLUMNS):
            pygame.draw.rect(screen, grid[y][x],
                             (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    for x in range(COLUMNS):
        pygame.draw.line(screen, GRAY, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, HEIGHT))
    for y in range(ROWS):
        pygame.draw.line(screen, GRAY, (0, y * BLOCK_SIZE), (WIDTH, y * BLOCK_SIZE))

def draw_shape(shape, position, color):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, color,
                                 ((position[0] + x) * BLOCK_SIZE,
                                  (position[1] + y) * BLOCK_SIZE,
                                  BLOCK_SIZE, BLOCK_SIZE), 0)

def valid_position(shape, grid, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = off_x + x
                new_y = off_y + y
                if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS:
                    return False
                if new_y >= 0 and grid[new_y][new_x] != BLACK:
                    return False
    return True

def add_shape_to_grid(shape, grid, offset, color):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[off_y + y][off_x + x] = color

def clear_lines(grid):
    new_grid = [row for row in grid if BLACK in row]
    lines_cleared = ROWS - len(new_grid)
    while len(new_grid) < ROWS:
        new_grid.insert(0, [BLACK for _ in range(COLUMNS)])
    return new_grid, lines_cleared

def rotate(shape):
    return [ [ shape[y][x] for y in range(len(shape)) ][::-1] for x in range(len(shape[0])) ]

def main():
    grid = create_grid()
    current_shape = random.choice(SHAPES)
    current_color = random.choice(COLORS)
    shape_pos = [COLUMNS // 2 - len(current_shape[0]) // 2, 0]
    fall_time = 0
    fall_speed = 500
    score = 0
    running = True

    while running:
        screen.fill(BLACK)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time > fall_speed:
            shape_pos[1] += 1
            if not valid_position(current_shape, grid, shape_pos):
                shape_pos[1] -= 1
                add_shape_to_grid(current_shape, grid, shape_pos, current_color)
                grid, lines = clear_lines(grid)
                score += lines * 100
                current_shape = random.choice(SHAPES)
                current_color = random.choice(COLORS)
                shape_pos = [COLUMNS // 2 - len(current_shape[0]) // 2, 0]
                if not valid_position(current_shape, grid, shape_pos):
                    print("Game Over! Score:", score)
                    running = False
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shape_pos[0] -= 1
                    if not valid_position(current_shape, grid, shape_pos):
                        shape_pos[0] += 1
                if event.key == pygame.K_RIGHT:
                    shape_pos[0] += 1
                    if not valid_position(current_shape, grid, shape_pos):
                        shape_pos[0] -= 1
                if event.key == pygame.K_DOWN:
                    shape_pos[1] += 1
                    if not valid_position(current_shape, grid, shape_pos):
                        shape_pos[1] -= 1
                if event.key == pygame.K_UP:
                    rotated = rotate(current_shape)
                    if valid_position(rotated, grid, shape_pos):
                        current_shape = rotated

        draw_grid(grid)
        draw_shape(current_shape, shape_pos, current_color)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
