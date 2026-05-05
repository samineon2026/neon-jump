import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Jump")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 100)
RED = (255, 50, 50)

player = pygame.Rect(180, 500, 40, 40)
speed = 6

obstacles = []
ob_speed = 5

score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def reset():
    global obstacles, score, player
    obstacles = []
    score = 0
    player.x = 180
    player.y = 500

running = True
game_over = False

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:

        if keys[pygame.K_LEFT] and player.x > 0:
            player.x -= speed
        if keys[pygame.K_RIGHT] and player.x < WIDTH - 40:
            player.x += speed

        if random.randint(1, 25) == 1:
            obstacles.append(pygame.Rect(random.randint(0, WIDTH-40), -40, 40, 40))

        for obs in obstacles[:]:
            obs.y += ob_speed

            if obs.y > HEIGHT:
                obstacles.remove(obs)
                score += 1

            if player.colliderect(obs):
                game_over = True

        pygame.draw.rect(screen, GREEN, player)

        for obs in obstacles:
            pygame.draw.rect(screen, RED, obs)

        draw_text(f"Score: {score}", 10, 10)

    else:
        draw_text("GAME OVER", 120, 250, RED)
        draw_text("Press R to Restart", 80, 300)

        if keys[pygame.K_r]:
            reset()
            game_over = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
