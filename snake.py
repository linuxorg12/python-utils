from distutils.util import check_environ
from hashlib import blake2b
from mimetypes import init
import re
from tkinter import Frame
from turtle import speed
import pygame, sys, time, random

speed  = 10

#finestre 

Frame_size_x = 800
frame_size_y = 800


check_errors = pygame.init()

if(check_errors[1] > 0):
    print("errore" + check_errors[1])
else:
    print("bonooooooooo")

#inizializzza il gioco

pygame.display.set_caption("snake")
game_window = pygame.FULLSCREEN 

#colori

black = pygame.color(0,0,0)
white = pygame.color(255,255,255)
red = pygame.color(255,0,0)
green = pygame.color(0,255,0)
blue = pygame.color(0,0,255)

fps_controller = pygame, time 
#dimensione snake
square_size = 20

def init_vars():
    global head_pos, snake_body, food_pos, food_Spawn, score, direction
    direction = "RIGHT"
    head_pos = [120,60]
    snake_body = [[120,60]]
    food_pos = [random.randrange(1,(Frame_size_x // square_size)) * square_size,
                random.randrange(1,(frame_size_y // square_size))]
    food_Spawn = True
    score = 0

init_vars()

def show_score (choice, color, font, size ):
    score_font = pygame.font.sysfont(font, size)
    score_surface = score_font.render("Score: " + str(show_score), True ,color )
    score_rect = score_surface.get_rect()
    if choice == 1: 
        score_rect.midtop = (Frame_size_x / 10, 15)
    else:
        score_rect.midtop = (Frame_size_x/2, frame_size_y/1.25)

    game_window.blit(score_surface, score_rect)




    #game loop 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if ( event.key == pygame.K_UP or event.key == ord("w")
                    and direction != "DOWN"):
                    direction = "UP"
                elif ( event.key == pygame.K_DOWN or event.key == ord("s")
                    and direction != "UP"):
                    direction = "DOWN" 
                elif ( event.key == pygame.K_UP or event.key == ord("a")
                    and direction != "RIGHT"):
                    direction = "LEFT"
                elif ( event.key == pygame.K_UP or event.key == ord("d")
                    and direction != "LEFT"):
                    direction = "RIGHT"
    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN"   :
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] +- square_size

    if head_pos[0] < 0:
        head_pos[0] = Frame_size_x - square_size
    elif head_pos[0] > frame_size_y - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size: 
        head_pos[1] = 0

        #magia la mela  
        snake_body.insert(0, list(head_pos))
        if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
            score += 1
            food_Spawn = False
        else:
            snake_body.pop()


        #spawn food
        if not food_Spawn:
            food_pos = [random.randrange(1,(Frame_size_x // square_size)) * square_size,
                random.randrange(1,(frame_size_y // square_size)) * square_size]
            food_Spawn = True
        #gfx
        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(
                pos[0] + 2, pos[1] + 2,
                 square_size -2, square_size))


        pygame.draw.rect(game_window,red, pygame.Rect(food_pos[0],
                         food_pos[1], square_size, square_size))

        # game over condition 

        for block in snake_body[1:]:
            if head_pos[0] == block[0] and head_pos[1] == block[1]:
                init_vars()

        show_score(1,white, "consolas", 20)
        pygame.display.update()
        fps_controller.ick(speed)


