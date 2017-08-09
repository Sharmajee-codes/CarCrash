import pygame, pygame.mixer
import time
import random

pygame.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.3)

accel = pygame.mixer.Sound('accel.wav')
accel.set_volume(0.01)
carbreak = pygame.mixer.Sound('break.wav')
carbreak.set_volume(0.04)
horn = pygame.mixer.Sound('horn.wav')
horn.set_volume(0.07)
carcrash = pygame.mixer.Sound('crash.wav')
carcrash.set_volume(0.04)
display_width = 600
display_height = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
car_width = 45
car_height = 100



gameDisplay = pygame.display.set_mode((display_width,display_height))
carImg = pygame.image.load('lambo.png')
pygame.display.set_caption('Crash Car')
carImgIcon = pygame.image.load('car.png')
pygame.display.set_icon(carImgIcon)
clock = pygame.time.Clock()
pause = False
oppcarImg = pygame.image.load('Polcar.png')

crashedCarImg = pygame.image.load('Boom.png')

def opp_dodged(count):
    font = pygame.font.SysFont(None, 25)
    scoretext = font.render("Score: "+str(count),True,white)
    gameDisplay.blit(scoretext,(0,0))
    
    
def oppcar(oppx,oppy):
    gameDisplay.blit(oppcarImg,(oppx,oppy))
     
    
def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textsurface = font.render(text,True,black)
    return textsurface, textsurface.get_rect() 

def message_display(text):
    Largetext = pygame.font.SysFont('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text,Largetext)
    TextRect.center = (display_width/2),(display_height/2)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash(x,y):
    accel.stop()
    gameDisplay.blit(crashedCarImg,(x,y))
    carcrash.play()
    pygame.mixer.music.stop()
    message_display('You Crashed ')
    pygame.display.update()
    

def button(url,invUrl,x,y,w,h, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    btn = pygame.image.load(url)
    btn = pygame.transform.scale(btn,(w,h))
    gameDisplay.blit(btn,(x,y))
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        btn = pygame.image.load(invUrl)
        btn = pygame.transform.scale(btn,(w,h))
        gameDisplay.blit(btn,(x,y))
        if click[0]==1 and action !=None:
            if action=="Play":
                game_loop()
        
            elif action == "Quit":
                pygame.quit()
                quit()  
            elif action == "Resume":
                resume()    
            
        
        
    else:
        pass

def resume():
    global pause 
    pause = False


def paused():
    while pause == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        Homebg = pygame.image.load("Intro.jpg").convert()
        Homebg = pygame.transform.scale(Homebg,(600,700))
        gameDisplay.blit(Homebg,(0,0))
        
        Resumebtn = button("Resume.png","invResume.png",180,380,250,75,"Resume")       
        
        exitbtn = button("exitgame.png","invexitgame.png",180,480,250,75,"Quit")
        
        largetext = pygame.font.SysFont('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Paused", largetext)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
    
def game_intro():
    
    intro = True
    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        Homebg = pygame.image.load("Intro.jpg").convert()
        Homebg = pygame.transform.scale(Homebg,(600,700))
        gameDisplay.blit(Homebg,(0,0))
        
        playbtn = button("playgame.png","invplaygame.png",180,380,250,75,"Play")       
        
        exitbtn = button("exitgame.png","invexitgame.png",180,480,250,75,"Quit")
        
        largetext = pygame.font.SysFont('freesansbold.ttf',80)
        TextSurf, TextRect = text_objects("Welcome", largetext)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
    
    
def game_loop():
    global pause
    pygame.mixer.music.play()
    x = (display_width * 0.45)
    y = (display_height * 0.6)
    
    x_change = 0
    y_change = 0   
    
#Opponent 1
    opp_startx = random.randrange(100,450)
    opp_starty = -700
    opp_speed = 4
    opp_width = 45
    opp_height = 100
    
    

    
    dodged = 0
    bg = pygame.image.load("road.png").convert()
    bg = pygame.transform.scale(bg,(600,700))
    yBG = 0
    
    gameExit = False
    
    while not gameExit:

        
        accel.play()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5    
                    
                    
                
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                                        
                    
                if event.key == pygame.K_UP:
                    y_change = -5
                    
                    
                    
                if event.key == pygame.K_DOWN:
                    y_change = 5
                    
                    accel.stop()
                    carbreak.play()
                    
                if event.key == pygame.K_SPACE:
                    accel.stop()
                    horn.play()
                    accel.play()
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0
            
        x += x_change
        y += y_change
       
        rel_bgY = yBG % bg.get_rect().height
        gameDisplay.blit(bg,(0,rel_bgY-bg.get_rect().height))
        
        if rel_bgY<display_height:
            gameDisplay.blit(bg, (0,rel_bgY))
        
        yBG+=3.5
        #oppcar(oppx,oppy)
        oppcar(opp_startx,opp_starty)
        opp_starty += opp_speed
        
        
        car(x,y)
        opp_dodged(dodged)
        if x>display_width-(3*(car_width)) or x < (2*(car_width)) or y<0 or y>display_height-car_height:
            crash(x,y)
            
        if opp_starty >display_height:
            opp_starty = 0-opp_height
            opp_startx = random.randrange(100,450)
            dodged +=1 
            opp_speed +=0.7
          
        if y < opp_starty+opp_height:
            
            
            if x > opp_startx and x < opp_startx + opp_width and y > opp_starty and y < opp_starty + opp_height or x+car_width > opp_startx and x + car_width < opp_startx+opp_width and y+car_height > opp_starty and y + car_height < opp_starty + opp_height or x > opp_startx  and x < opp_startx + opp_width and y+car_height > opp_starty and  y+car_height < opp_starty + opp_height or x+car_width > opp_startx  and x+car_width < opp_startx + opp_width and y > opp_starty and  y < opp_starty + opp_height :
                crash(x,y)
            
            
        
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()