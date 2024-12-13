import pygame


pygame.init()

FPS =  pygame.time.Clock()

WIDTH = 600
HEIGHT = 800

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load('img/bg.png'), (WIDTH, HEIGHT))



playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    main_display.blit(bg, (0, 0))
    pygame.display.update()