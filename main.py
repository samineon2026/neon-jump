import pygame
import sys
import random

pygame.init()

# اندازه صفحه
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Jump")

clock = pygame.time.Clock()

# رنگ‌ها
BLACK = (0, 0, 0)
NEON = (0, 255, 200)

# بازیکن
player = pygame.Rect(180, 500, 40, 40)
velocity_y = 0
gravity = 0.5
jump_power = -10

# پلتفرم‌ها
platforms = [pygame.Rect(150, 550, 100, 10)]

score = 0
font = pygame.font.SysFont(None, 30)

def draw_text(text, x, y):
    img = font.render(text, True, NEON)
    screen.blit(img, (x, y))

while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player
