import pygame

pygame.init()


screen_w = 1317
screen_h = 656

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Wolf Sheep Cabbage Game")

#Animal Size: 105 75
#Boat size: 290 150


game_clock = pygame.time.Clock()

background = pygame.image.load("Imgs/Background.jpeg").convert()
boat = pygame.image.load("Imgs/Boat.png")
wolf = pygame.image.load("Imgs/Wolf.png")
sheep = pygame.image.load("Imgs/Sheep.png")
cabbage = pygame.image.load("Imgs/Cabbage.png")


game_crash = False


boat_x = 500
boat_y = 300
mov_boat = 0

wolf_x = 90
wolf_y = 350

def draw_object(obj,x,y):
    screen.blit(obj,(x,y))

while not game_crash:
    click_wolf = False
    screen.fill((0,0,0))

    screen.blit(background, (0,0))   
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_crash = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mov_boat = -5
            elif event.key == pygame.K_RIGHT:
                mov_boat = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                mov_boat = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()
            if wolf.get_rect(topleft=(wolf_x,wolf_y)).collidepoint(click_x,click_y):
                if(boat_x == 290):
                    
           
        #    elif sheep.get_rect(topleft=(sheep_x,sheep_y)).collidepoint(click_x,click_y):
         #       print("Clicked on sheep.")
          #     elif cabbage.get_rect(topleft=(cabbage_x,cabbage_y)).collidepoint(click_x, click_y):
        
    boat_x += mov_boat
    
    if boat_x <=290:
        boat_x = 290
    elif boat_x >= 750:
        boat_x = 750
    
    draw_object(boat,boat_x,boat_y)
    draw_object(wolf,wolf_x,wolf_y)
    draw_object(sheep, 90, 450)
    draw_object(cabbage, 90, 550)
    pygame.display.update()
    game_clock.tick(60)

pygame.quit()
quit()
