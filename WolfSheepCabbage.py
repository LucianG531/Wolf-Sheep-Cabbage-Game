import pygame
from Entities import Entity



pygame.init()


screen_w = 1317
screen_h = 656

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Wolf Sheep Cabbage Game")

#Animal Size: 105 75
#Boat size: 290 150


game_clock = pygame.time.Clock()

background = pygame.image.load("Imgs/Background.jpeg").convert()
boat = Entity(screen, 270, 300 ,"Imgs/Boat.png")
wolf = Entity(screen, 90, 350, "Imgs/Wolf.png")
sheep = pygame.image.load("Imgs/Sheep.png")
cabbage = pygame.image.load("Imgs/Cabbage.png")


wolf.set_side("RIGHT")

game_crash = False

mov_boat = 0

wolf_x = 90
wolf_y = 350



wolf_flag = 0

def draw_object(obj,x,y):
    screen.blit(obj,(x,y))

while not game_crash:

    screen.fill((0,0,0))

    screen.blit(background, (0,0))   
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_crash = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                boat.set_mov(-5)
                if wolf.get_pos():
                    wolf.set_mov(-5)
            elif event.key == pygame.K_RIGHT:
                boat.set_mov(5)
                if wolf.get_pos():
                    wolf.set_mov(5)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                boat.set_mov(0)
                if wolf.get_pos():
                    wolf.set_mov(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()
            if wolf.isClickedOn(click_x,click_y):
                if(boat.get_x() == 270):
                    wolf.enter_boat()
                    wolf.set_x(boat.get_x()+50)
                    wolf.set_y(boat.get_y()-25)
                   
                                           
                   
        #    elif sheep.get_rect(topleft=(sheep_x,sheep_y)).collidepoint(click_x,click_y):
    
         #       print("Clicked on sheep.")
          #     elif cabbage.get_rect(topleft=(cabbage_x,cabbage_y)).collidepoint(click_x, click_y):
        
    boat.move()
    if wolf.get_pos():
        wolf.move()
    
    if boat.get_x() <=270:
        boat.set_x(270)
        boat.set_direction("LEFT")
        if wolf.get_side == "LEFT":
            wolf.set_side("RIGHT")
            wolf.leave_boat()
            wolf.set_x(90)
            wolf.set_y(350)

    elif boat.get_x() >= 750:
        boat.set_x(750)
        if wolf.get_side == "RIGHT":
            wolf.set_side("LEFT")
            wolf.leave_boat()
            wolf.set_x(1227)
            wolf.set_y(350)
    

    boat.draw()
    wolf.draw()
    draw_object(sheep, 90, 450)
    draw_object(cabbage, 90, 550)
    pygame.display.update()
    game_clock.tick(60)

pygame.quit()
quit()
