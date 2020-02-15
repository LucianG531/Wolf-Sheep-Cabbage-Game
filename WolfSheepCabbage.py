import pygame

pygame.init()


screen_w = 840
screen_h = 839

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Wolf Sheep Cabbage Game")

# Left border : 95 695
# Right border: 750 695


game_clock = pygame.time.Clock()

background = pygame.image.load("Imgs/Background.jpeg").convert()
boat = pygame.image.load("Imgs/boat.png")



game_crash = False


x = 100
y = 500
mov_x = 0


def make_boat(x,y):
    screen.blit(boat,(x,y))


while not game_crash:
   
    screen.fill((0,0,0))

    screen.blit(background, (0,0))   
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_crash = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mov_x = -5
            elif event.key == pygame.K_RIGHT:
                mov_x = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mov_x = 0
    x += mov_x
    
    if x <=-135:
        x = -135
    elif x >= 400:
        x = 400
   
    make_boat(x,y)
    pygame.display.update()
    game_clock.tick(60)

pygame.quit()
quit()
