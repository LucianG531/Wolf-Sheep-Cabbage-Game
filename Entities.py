#!/usr/bin/env python

"""

Class that defines most properties of an entity in our game

"""
import pygame

# Entity class which represents all objects the player can interact with

class Entity:
    
    def __init__(self,name,screen,pos_x, pos_y, img):
        self.name = name
        self.screen = screen
        self.x = pos_x
        self.y = pos_y
        self.image = pygame.image.load(img)
        self.rectangle = self.image.get_rect(topleft=(self.x,self.y))
        self.mov = 0
        self.direction = "RIGHT"
        self.side = ""
       
       # Default entity positions when they are either on the right or the left side of the screen
        self.right_x = 0
        self.right_y = 0
        self.left_x = pos_x
        self.left_y = pos_y
    
    # Change the coordinates of the rectangle corresponding to the entity's image

    def set_rectangle(self, x, y):
        self.rectangle.x = x
        self.rectangle.y = y

    # Returns this entity's rectangle

    def get_rectangle(self):
        return self.rectangle
    
    # Sets this entity's speed parameter

    def set_mov(self,x):
        self.mov = x
    
    # Draws the entity to the screen, facing a certain direction

    def draw(self):
        if(self.direction) == "RIGHT":
            self.screen.blit(self.image,(self.x, self.y))
        if(self.direction) == "LEFT":
            self.screen.blit(pygame.transform.flip(self.image,True,False),(self.x,self.y))
    
    # Various getters and setters
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_direction(self,d):
        self.direction = d
    def get_mov(self):
        return self.mov
    def set_side(self,x):
        self.side = x
    def get_side(self):
        return self.side

    # Moves the entity to the right or left, depending on its speed parameter

    def move(self):
        if(self.mov >=0):
            self.direction = "RIGHT"
        else:
            self.direction = "LEFT"
        self.x = self.x + self.mov
        self.rectangle.x = self.rectangle.x+self.mov 
    
    # Help function, checks if the point given by x and y is inside this entity's rectangle
    # Is used in the game loop to check if the user has clicked on this entity

    def isClickedOn(self, x, y):
        return self.rectangle.collidepoint(x,y)
    
    # Checks if the entities are the same (in our case the name will be unique)

    def __eq__(self,other):
        if not isinstance(other, Entity):
            return NotImplemented
        return self.name == other.name
    
    # Getters and setters for default left/right position of the entity

    def set_right(self, x,y):
        self.right_x = x
        self.right_y = y
    
    def get_right(self):
        return (self.right_x, self.right_y)
    
    def get_left(self):
        return (self.left_x, self.right_y)

# Class boat, which is a special type of entity that can contain other entities and move them accross the screen with itself

class Boat(Entity):
   
    
    def __init__(self, name, screen, pos_x, pos_y,  img):
       Entity.__init__(self, name,screen, pos_x, pos_y, img)
       self.contains = None
       
   # Overloads the move method from Entity, as boat does not have a rectangle

    def move(self):
        if(self.mov >=0):
            self.direction = "RIGHT"
        else:
            self.direction = "LEFT"
        self.x = self.x + self.mov

    # Puts the Entity obj inside of the boat

    def enter_boat(self, obj):
        self.contains = obj

    # Kicks all entities out of the boat

    def leave_boat(self):
        self.contains = None
    
    # Returns the entity that is inside of the boat at the moment

    def get_content(self):
        return self.contains
    

