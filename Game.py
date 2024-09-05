import pygame
from pygame.locals import *
from time import *
import datetime

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

pygame.init()
screen = pygame.display.set_mode((800, 580), pygame.RESIZABLE, pygame.NOFRAME)
logo = pygame.image.load(".\\img\\Arc.svg").convert_alpha() # ---
icon = pygame.image.load(".\\clock.ico").convert_alpha()
pygame.display.set_caption("Arc Browser ver 1.0")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True


screen.fill("white")

forward = 0
backward = 0

while running:
    
    height = screen.get_height()
    width = screen.get_width()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)
            screen.fill("white")
    
    # --- draw logo on top left corner
    logo_size_w = width*0.1
    DEFAULT_IMAGE_SIZE = (logo_size_w, logo_size_w * 0.83)
    logo = pygame.transform.scale(logo, DEFAULT_IMAGE_SIZE)
    screen.blit(logo, (0, 0))
    
    # pygame.draw.circle(screen, (255, 111, 97), (width/2 + forward, height/2), 25)
    
    pygame.display.flip()
    pygame.time.wait(10)
    screen.fill("white")

    clock.tick(60)
    
pygame.quit()