import pygame
import math
from pygame import mixer

# initialize the game
pygame.init()

# FPS 
FPS = 60
fpsclock = pygame.time.Clock()

# create the screen
screen_length = 600
screen_width = 300
screen = pygame.display.set_mode((screen_length,screen_width))

# background, title and icon
background = pygame.image.load("background.jpg")
title = pygame.display.set_caption("dinasour game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# add dinasor
dinosaurImg = pygame.image.load("dinosaur.png")
dinosaurX = 10
dinosaurY = 220
dinosaurY_change = 0.1

def dinosaur(x,y):
    screen.blit(dinosaurImg,(x,y))

# dinasour jumps over the tree
jump = False

# add tree
treeImg = pygame.image.load("tree.png")
treeX = 530
treeY = 230
treeX_change = 0.1

def tree(x,y):
    screen.blit(treeImg,(x,y))

# change background
backgroundX = 0
backgroundY = 0
background_change = 0.1

def background_screen1(x,y):
    screen.blit(background,(x,y))
def background_screen2(x,y):
    screen.blit(background,(x+600,y))

# check collision
def isCollision(dinosaurX,dinosaurY,treeX,treeY):
    distance = math.sqrt(math.pow(dinosaurX-treeX,2)+math.pow(dinosaurY-treeY,2))
    if distance < 27:
        return True
    else:
        return False

# game over
over_font = pygame.font.Font("freesansbold.ttf",60)

def game_over():
    text1 = over_font.render("GAME OVER", True, (150,150,255))
    screen.blit(text1,(106,120))

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (150,150,255))
    screen.blit(score,(x,y))

# game loop
running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if dinosaurY == 220:
                    jump = True
                    jump_sound = mixer.Sound('tick.wav')
                    jump_sound.play()

    background_screen1(backgroundX,backgroundY)
    background_screen2(backgroundX,backgroundY)
    backgroundX -= background_change
    if backgroundX <=0:
        backgroundX = 0
        backgroundX -= background_change

    dinosaur(dinosaurX,dinosaurY)
    if 220>=dinosaurY>= 140:
        if jump == True:
            dinosaurY -= dinosaurY_change

    else:
        jump = False
    if dinosaurY < 220:
        if jump == False:
            dinosaurY += dinosaurY_change

    tree(treeX,treeY)
    treeX -= treeX_change

    if treeX <= -20:
        treeX = 600
        score_value += 1

    collision = isCollision(dinosaurX,dinosaurY,treeX,treeY)
    if collision:
        background_change = 0
        treeX_change = 0
        game_over()
        jump = False

    show_score(textX,textY)
    fpsclock.tick()
    pygame.display.flip()

pygame.quit()