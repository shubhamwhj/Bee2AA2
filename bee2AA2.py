import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
  
#load the images in dict
images={}
images["bg"] = pygame.image.load("bg.png").convert_alpha()
images["base"] = pygame.image.load("base.png").convert_alpha()
images["bee"] = pygame.image.load("bee.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()

groundx=0
speed=5
g=0.5

bee= pygame.Rect(100,250,30,30)

    
def gravity(): 
    global speed
    speed=speed+g   
    bee.y= bee.y + speed

def flap():
    global speed
    speed=-10

def show():
    global speed
    print(speed)
    
 
while True:    
    screen.fill((50,150,255))
    screen.blit(images["bg"],[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flap()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                flap()
    
    show()        
    gravity()
    
    groundx =groundx-5
    
    if groundx< -330:
        groundx=0
    
    screen.blit(images["bee"],bee) 
    screen.blit(images["base"],[groundx,550])
    
    pygame.display.update()
    clock.tick(30)
    
    
    
    

