import pygame
from Entities import Entity, Boat


pygame.init()


# Setting background size equal to background image size

screen_w = 1317
screen_h = 656

# Creating the game window

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Wolf Sheep Cabbage Game")

#Animal Size: 105 75
#Boat size: 290 150


# Initializing the game clock
game_clock = pygame.time.Clock()


# Initializing the game font
game_font = pygame.font.Font("Imgs/nimrod_mt.ttf", 48)


# Loading the images for the background and all entities  the initial game state
background = pygame.image.load("Imgs/Background.jpeg").convert()
boat = Boat("boat",screen, 270, 300 ,"Imgs/Boat.png")
wolf = Entity("wolf",screen, 90, 350, "Imgs/Wolf.png")
sheep = Entity("sheep", screen, 90, 450, "Imgs/Sheep.png")
cabbage = Entity("cabbage", screen, 90, 550, "Imgs/Cabbage.png")


# Adding all animals to a list to easly operate on all at the same time when needed

animals = [wolf, sheep, cabbage]


for animal in animals:

    # All animals are initially on the left side

    animal.set_side("LEFT")
    
    # Setting where the animal is placed once moved to the right side

    animal.set_right(screen_w - 250, animal.get_y())


# Variable to check if game is still running

game_crash = False

# Method to define behaviour in case a game loss condition

def game_over():
    text = game_font.render("GAME OVER", True, (0,0,0))
    screen.blit(text,(520, 280))
    for animal in animals:
        animal.set_x(2000)
        animal.set_y(2000)


def game_won():
    text = game_font.render("YOU WON!", True, (0,0,0))
    screen.blit(text, (520,280))
    for animal in animals:
        animal.set_x(2000)
        animal.set_y(2000)

# Game loop

while not game_crash:
    
    # Drawing background

    screen.fill((0,0,0))

    screen.blit(background, (0,0))   
    
    # Defining behaviour for different events

    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            game_crash = True
        
        # If user presses the left key, the boat's and boat content's speed parameter is set to -5 (So boat moves left)
        # If user presses the right key, the boat's and boat content's speed parameter is set to 5 (So boat moves right)
        # If user lets go of either key, the boat's and boat content's speed parameter is set to 0 (So the boat stops moving)

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
        
        # User can click on an animal
        # If animal is clicked on and the boat has no content, and the boat and animal are on the same side, 
        #then the animal enters the boat

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = pygame.mouse.get_pos()
            for animal in animals:
                if animal.isClickedOn(click_x,click_y):
                    if (boat.get_x() == 270 or boat.get_x() == 750) and animal.get_side() == boat.get_side():
                        if boat.get_content() == None:

                            boat.enter_boat(animal)
                            animal.set_x(boat.get_x()+50)
                            animal.set_y(boat.get_y()-25)
                            animal.set_rectangle(boat.get_x()+50, boat.get_y()-25)
                            animal.set_direction(boat.get_side())

                        elif boat.get_content() == animal:
                            if boat.get_side() == "LEFT":
                                x,y = animal.get_left()
                                orientation = "LEFT" 
                            elif boat.get_side() == "RIGHT":
                                x,y = animal.get_right()
                                orientation = "RIGHT"
                            
                            animal.set_x(x)
                            animal.set_y(y)
                            animal.set_direction(orientation)
                            animal.set_rectangle(x,y)
                            boat.leave_boat()

    # Boat side determined by which half of the screen it finds itself in
    # This is done to give the player some leeway in case they make a mistake and want to correct it

    if boat.get_x() <= 510:
        boat.set_side("LEFT")
            
           
    elif boat.get_x() <= 750:
        boat.set_side("RIGHT")

                   
    # Move the boat and its contents

    boat.move()
    if not boat.get_content() == None:
        boat.get_content().move()
        boat.get_content().set_side(boat.get_side())
    
    # Prevents boat from leaving the boundaries of the water on the screen

    if boat.get_x() <=270:
        boat.set_x(270)
        boat.set_direction("LEFT")
        if not boat.get_content() == None:
            boat.get_content().set_x(boat.get_x()+50)
            boat.get_content().set_rectangle(boat.get_x()+50, boat.get_y()-25)
    elif boat.get_x() >= 750:
        boat.set_x(750)
        if not boat.get_content() == None:
            boat.get_content().set_x(boat.get_x()+50)        
            boat.get_content().set_rectangle(boat.get_x()+50, boat.get_y()-25)
 
    # Game conditions are as follows:
    # Wolf and sheep cannot be on the same side if the boat is not there
    # Sheep and cabbage cannot be on the same side if the boat is not there

    if wolf.get_side() == sheep.get_side() and not wolf.get_side() == boat.get_side():
        game_over()
        
    if sheep.get_side() == cabbage.get_side() and not sheep.get_side() == boat.get_side():
        game_over()
   
   # TODO: Dont end game before player clicked last animal and put it into right place

    if  wolf.get_side() == sheep.get_side() and sheep.get_side() == cabbage.get_side() and cabbage.get_side() == "RIGHT" and boat.get_x() == 750:
        game_won()


    # Draws all entities to the screen

    boat.draw()
    wolf.draw()
    sheep.draw()
    cabbage.draw()
    
    # Updates the game screen and sets the game clock to 60
    pygame.display.update()
    game_clock.tick(60)

pygame.quit()
quit()
