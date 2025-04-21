import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders - No Images")

WHITE = (255, 255, 255)
PLAYER_COLOR = (0, 255, 0)
ENEMY_COLOR = (255, 0, 0)
BULLET_COLOR = (255, 255, 0)
BACKGROUND_COLOR = (0, 0, 30)

player_x = 370
player_y = 480
player_x_change = 0

enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 5

for _ in range(num_of_enemies):
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(3)
    enemy_y_change.append(40)

bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"

score_value = 0
font = pygame.font.Font(None, 36)

over_font = pygame.font.Font(None, 64)

def show_score():
    score = font.render("Score : " + str(score_value), True, WHITE)
    screen.blit(score, (10, 10))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (250, 250))

def player(x, y):
    pygame.draw.rect(screen, PLAYER_COLOR, (x, y, 50, 50))

def enemy(x, y):
    pygame.draw.circle(screen, ENEMY_COLOR, (x + 25, y + 25), 25)

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    pygame.draw.rect(screen, BULLET_COLOR, (x + 20, y, 10, 20))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.hypot(enemy_x - bullet_x, enemy_y - bullet_y)
    return distance < 30

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    player_x += player_x_change
    player_x = max(0, min(player_x, 750))

    for i in range(num_of_enemies):
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 3
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 750:
            enemy_x_change[i] = -3
            enemy_y[i] += enemy_y_change[i]

        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i])

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"

    player(player_x, player_y)
    show_score()

    pygame.display.update()
