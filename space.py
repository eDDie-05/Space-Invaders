import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Font
font = pygame.font.SysFont("Arial", 36)

# Player settings
player_width = 60
player_height = 20
player_speed = 7

player = pygame.Rect(
    WIDTH // 2 - player_width // 2,
    HEIGHT - 60,
    player_width,
    player_height
)

# Bullet settings
bullet_width = 5
bullet_height = 15
bullet_speed = 10

bullets = []

# Enemy settings
enemy_width = 50
enemy_height = 30
enemy_speed = 2

enemies = []

for row in range(4):
    for col in range(8):
        enemy = pygame.Rect(
            80 + col * 80,
            50 + row * 60,
            enemy_width,
            enemy_height
        )
        enemies.append(enemy)

# Enemy direction
enemy_direction = 1

# Score
score = 0



def draw_player():
    pygame.draw.rect(screen, GREEN, player)



def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)



def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)



def move_bullets():
    for bullet in bullets[:]:
        bullet.y -= bullet_speed

        if bullet.bottom < 0:
            bullets.remove(bullet)



def move_enemies():
    global enemy_direction

    move_down = False

    for enemy in enemies:
        enemy.x += enemy_speed * enemy_direction

        if enemy.right >= WIDTH or enemy.left <= 0:
            move_down = True

    if move_down:
        enemy_direction *= -1

        for enemy in enemies:
            enemy.y += 20



def check_collisions():
    global score

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break



def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (20, 20))



def game_over(message):
    screen.fill(BLACK)

    over_text = font.render(message, True, YELLOW)
    score_text = font.render(f"Final Score: {score}", True, WHITE)

    screen.blit(over_text, (WIDTH // 2 - 140, HEIGHT // 2 - 40))
    screen.blit(score_text, (WIDTH // 2 - 140, HEIGHT // 2 + 10))

    pygame.display.update()
    pygame.time.delay(3000)

    pygame.quit()
    sys.exit()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(
                    player.centerx - bullet_width // 2,
                    player.y,
                    bullet_width,
                    bullet_height
                )
                bullets.append(bullet)

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed

    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Move objects
    move_bullets()
    move_enemies()

    # Check collisions
    check_collisions()

    # Lose condition
    for enemy in enemies:
        if enemy.bottom >= player.top:
            game_over("GAME OVER")

    # Win condition
    if len(enemies) == 0:
        game_over("YOU WIN!")

    # Drawing
    screen.fill(BLACK)

    draw_player()
    draw_bullets()
    draw_enemies()
    show_score()

    pygame.display.update()
    clock.tick(FPS)
