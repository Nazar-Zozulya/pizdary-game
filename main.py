import pygame

from os import path

import random


pygame.init()

FPS =  pygame.time.Clock()

WIDTH = 600
HEIGHT = 800

img_dir = path.join(path.dirname(__file__), 'img')

bg = pygame.transform.scale(pygame.image.load(path.join(img_dir, 'bg.png')), (WIDTH, HEIGHT))

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
title = pygame.display.set_caption("Pizdary game")

player_width = 60
player_height = 60
player = pygame.transform.scale(pygame.image.load(path.join(img_dir, 'player.png')), (player_width, player_height))

player_rect = player.get_rect()

player_move_left = [-1,0]
player_move_right = [1,0]

def create_enemy():
    enemy_width = 60
    enemy_height = 60

    enemy = pygame.transform.scale(pygame.image.load(path.join(img_dir, 'enemy.png')), (enemy_width, enemy_height))


    enemy_x = random.randint(100, WIDTH - 100)
    enemy_y = 0 + 100

    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    return [enemy, enemy_rect]


enemies = []

# class Enemy():
#     def __init__(self):
#         self.width = 60
#         self.height = 60

#         for i in range(5):
#             # enemy_x = WIDTH * i % 100
#             i + 10
#         self.x = WIDTH * i % 100
#         print(i)
#         self.y = HEIGHT - 100
#         self.img = pygame.transform.scale(pygame.image.load(path.join(img_dir, 'enemy.png')), (self.width, self.height))
#         self.rect = self.img.get_rect()
    
#     def draw(self):
#         main_display.blit(self.img, self.rect)

# def create_enemy(enemy):
#     for i in range(5):
#         enemy.draw()
#         main_display.blit(self.img, self.rect)
#         enemies.append(Enemy)
    

    


player_rect.center = (WIDTH // 2, HEIGHT *90 // 100)

# enemy_rect.center = 





# class Player():
#     x,y = 0,0
#     red,green,blue = 0,0,0
#     width,height = 60,60

#     def draw(self):  # отрисовка
#         pygame.draw.rect(main_display, (self.red, self.green, self.blue), (self.x, self.y, self.width, self.height))




playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        for i in range(1):
            enemies.append(create_enemy())
    
    main_display.blit(bg, (0, 0))

    # enemies.append(create_enemy())

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)

    if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)
    # print(enemies)
    for enemy in enemies:
        main_display.blit(enemy[0],enemy[1])

    # main_display.blit(player, player_rect)
    main_display.blit(player, player_rect)
    pygame.display.update()