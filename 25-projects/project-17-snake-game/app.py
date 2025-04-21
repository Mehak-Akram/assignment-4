import pygame
import time
import random

pygame.init()


window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

pygame.display.set_caption('Snake Game - by Mehak')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50]]

food_pos = [random.randrange(1, (window_x // 10)) * 10,
            random.randrange(1, (window_y // 10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.topleft = (10, 10)
    else:
        score_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (window_x // 10)) * 10,
                    random.randrange(1, (window_y // 10)) * 10]
    food_spawn = True

    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    if (snake_pos[0] < 0 or snake_pos[0] > window_x-10) or (snake_pos[1] < 0 or snake_pos[1] > window_y-10):
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    show_score(1, white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(25)
