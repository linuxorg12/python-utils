import pygame

check_errors = pygame.init()

if(check_errors[1] > 0):
    print("errore" + check_errors[1])
else:
    print("bonooooooooo")