import pygame
from Entities import Entity, Boat


pygame.init()


screen_w = 1317
screen_h = 656

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Wolf Sheep Cabbage Game")

#Animal Size: 105 75
#Boat size: 290 150


game_clock = pygame.time.Clock()
game_font = pygame.font.Font("Imgs/nimrod_mt.ttf", 48)



background = pygame.image.load("Imgs/Background.jpeg").convert()
boat = Boat("boat",screen, 270, 300 ,"Imgs/Boat.png")
wolf = Entity("wolf",screen, 90, 350, "Imgs/Wolf.png")
sheep = Entity("sheep", screen, 90, 450, "Imgs/Sheep.png")
cabbage = Entity("cabbage", screen, 90, 550, "Imgs/Cabbage.png")

animals = [wolf, sheep, cabbage]

for animal in animals:
    animal.set_side("LEFT")
    animal.set_left(screen_w - 250, animal.get_y())

game_crash = False


def game_over():
    text = game_font.render("GAME OVER", True, (0,0,0))
    screen.blit(text,(520, 280))
    for animal in animals:
        animal.set_x(2000)
        animal.set_y(2000)

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
                if not boat.get_content() == None:        
                    boat.get_content().set_mov(-5)
            elif event.key == pygame.K_RIGHT:
                boat.set_mov(5)
                if not boat.get_content() == None:
                    boat.get_content().set_mov(5)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                boat.set_mov(0)
                if not boat.get_content() == None:   
                    boat.get_content().set_mov(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()
            for animal in animals:
                if animal.isClickedOn(click_x,click_y):
                    if (boat.get_x() == 270) and (boat.get_content() == None):
                        boat.enter_boat(animal)
                        animal.set_x(boat.get_x()+50)
                        animal.set_y(boat.get_y()-25)
                     
                              

    if boat.get_x() <= 510:
        boat.set_side("LEFT")
            
           
    elif boat.get_x() <= 750:
        boat.set_side("RIGHT")

                   
       
    boat.move()
    if not boat.get_content() == None:
        boat.get_content().move()
        boat.get_content().set_rect()
        boat.get_content().set_side(boat.get_side())
    if boat.get_x() <=270:
        boat.set_x(270)
        boat.set_direction("LEFT")
        
       
    elif boat.get_x() >= 750:
        boat.set_x(750)
        
        if not boat.get_content() == None:
            x,y = boat.get_content().get_left()
            boat.get_content().set_x(x)
            boat.get_content().set_y(y)
            boat.get_content().set_direction("LEFT")
            boat.leave_boat()

            
    if wolf.get_side() == sheep.get_side() and not wolf.get_side() == boat.get_side():
        game_over()
        
    if sheep.get_side() == cabbage.get_side() and not sheep.get_side() == boat.get_side():
        game_over()
        
    boat.draw()
    wolf.draw()
    sheep.draw()
    cabbage.draw()
    pygame.display.update()
    game_clock.tick(60)

pygame.quit()
quit()
