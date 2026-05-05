import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Jump")

player = pygame.Rect(180, 500, 40, 40)
speed = 5

obstacles = []
score = 0

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    if random.randint(1, 35) == 1:
        obstacles.append(pygame.Rect(random.randint(0, 360), -40, 40, 40))

    for obs in obstacles[:]:
        obs.y += 4

        if obs.y > HEIGHT:
            obstacles.remove(obs)
            score += 1

        if player.colliderect(obs):
            running = False

    pygame.draw.rect(screen, (0, 255, 0), player)

    for obs in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obs)

    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
