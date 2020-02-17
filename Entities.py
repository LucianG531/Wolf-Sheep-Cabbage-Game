#!/usr/bin/env python

"""

Class that defines most properties of an entity in our game

"""
import pygame

class Entity:
    
    def __init__(self,name,screen,pos_x, pos_y, img):
        self.name = name
        self.screen = screen
        self.x = pos_x
        self.y = pos_y
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.mov = 0
        self.direction = "RIGHT"
        self.side = ""
        self.left_x = 0
        self.right_x = 0


    def set_mov(self,x):
        self.mov = x

    def draw(self):
        if(self.direction) == "RIGHT":
            self.screen.blit(self.image,(self.x, self.y))
        if(self.direction) == "LEFT":
            self.screen.blit(pygame.transform.flip(self.image,True,False),(self.x,self.y))

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
    
    def move(self):
        if(self.mov >=0):
            self.direction = "RIGHT"
        else:
            self.direction = "LEFT"
        self.x = self.x + self.mov
    
    def isClickedOn(self, x, y):
        return self.rect.collidepoint(x,y)
    
    def __eq__(self,other):
        if not isinstance(other, Entity):
            return NotImplemented
        return self.name == other.name
    
    def set_left(self, x,y):
        self.left_x = x
        self.left_y = y
    
    def get_left(self):
        return (self.left_x, self.left_y)

class Boat(Entity):
   
    
    def __init__(self, name, screen, pos_x, pos_y,  img):
       Entity.__init__(self, name,screen, pos_x, pos_y, img)
       self.contains = None
    
    def enter_boat(self, obj):
        self.contains = obj

    def leave_boat(self):
        self.contains = None
    
    def get_content(self):
        return self.contains

    def content(self, obj):
        if self.contains == obj:
            return True
        else:
            return False
