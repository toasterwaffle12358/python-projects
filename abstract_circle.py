#-----------------------#
# abstract art generator
#-----------------------#

#importing stuff
import pygame as pygame
import time as time
import random as random

#initializing pygame
pygame.init()

#setting up the screen
screen = pygame.display.set_mode([500,500])
screen.fill((255,255,255))

#setting up brightness
brightness = 5

#running loop
running = True
while running:
  pygame.display.flip()
  doty = random.randint(1,499)
  dotx = random.randint(1,499)
  randred = random.randint(1,254)
  randblue = random.randint(1,20)
  randgreen = random.randint(1,20)

  #setting up gradiant
  colorx = dotx / 4
  colory = doty / 4
  colorfull = colory + colorx * (random.randint(1,100)/100)

  
  #making size
  size = random.randint(1,50)

  #drawing the circles
  pygame.draw.circle(screen,(colorfull,colorfull,colorfull), (doty,dotx), size)


  #pause loop
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_p:
        pauseloop = True
        while pauseloop:
            events = pygame.event.get()
            for event in events:
              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                  pauseloop = False
