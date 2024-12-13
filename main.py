import pygame

from os import path


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


player_rect.center = (WIDTH // 2, HEIGHT *90 // 100)

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
    
    main_display.blit(bg, (0, 0))

    main_display.blit(player, player_rect)
    pygame.display.update()