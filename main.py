
# https://replit.com/@FrancescoBrusch/techcamp-2022-day2?v=1

import pygame
from random import randint
from time import sleep
pygame.init()
screen = pygame.display.set_mode((300,300))

# state variables
x = 10
y = 10
vx = 0
vy = 0

# target state
target_x = 100
target_y = 150
target_vx = 1
target_vy = 2
box_on_target = False
score = 0




def is_point_in_rect(x, y, rx, ry, rw, rh):
  return rx < x < rx+rw and ry < y < ry+rh

def render():
  pygame.draw.rect(screen, (100,100,100),   (0,0,300,300))

  pygame.draw.rect(screen, (0,255,0), (x, y, 100, 100))
  if box_on_target == True:
    pygame.draw.rect(screen, (255,0,0), (target_x,
                                       target_y, 
                                       30, 30))
  else:
    pygame.draw.rect(screen, (0,0,255), (target_x,
                                     target_y, 
                                     30, 30))

  
  pygame.display.flip()

def controller():
  global x, y, vx, vy, target_x, target_y, box_on_target, target_vx, target_vy, score
  pygame.event.get()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    vy -= 0.1
  if keys[pygame.K_DOWN]:
    vy += 0.1
  if keys[pygame.K_LEFT]:
    vx -= 0.1
  if keys[pygame.K_RIGHT]:
    vx += 0.1

  if is_point_in_rect(target_x, target_y,
                     x, y, 100, 100) and \
     is_point_in_rect(target_x + 30, target_y + 30,
                     x, y, 100, 100):
    box_on_target = True
  else:
    box_on_target = False

  if keys[pygame.K_SPACE]:
    if box_on_target:
      target_x = randint(0,299-30)
      target_y = randint(0,299-30)
      target_vx = randint(-2,2)
      target_vy = randint(-2,2)

      score = score +1
      print(score)
    
  
    
  x = x + vx
  y = y + vy
  if x + 100 > 300: 
    vx = -0.8 * vx
    x = 300-100
  if x < 0: 
    vx = -0.8*vx
    x = 0
  
  if y + 100 > 300: 
    vy = -0.8*vy
    y = 200
  if y < 0: 
    vy = -0.8*vy
    y = 0

  # target movement
  target_x = target_x + target_vx
  target_y = target_y + target_vy

  if target_x > 300: target_x = 0
  if target_x < 0: target_x = 300
  if target_y > 300: target_y = 0
  if target_y < 0: target_y = 300
  
  #vy += 0.1

while True:
  render()
  controller() # advance the state
  sleep(0.01)
    

