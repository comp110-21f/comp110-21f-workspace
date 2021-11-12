import sys
import pygame as py
from vector import Vector
from gm import GameManager
from enemy import Enemy
import pygame_gui
py.init()

# Window
size = width, height = 640, 480

# RGBA constants
green = 12, 152 ,54 ,0
color = 100, 50, 20, 10

FRAMES = 60
# Makes Screen
screen = py.display.set_mode(size)

# Game clock
clock = py.time.Clock()

#Keeps game loop running
playing = True

#Handles GUI
manager = pygame_gui.UIManager((width, height))


#UI Elements for GUI
health = pygame_gui.elements.UILabel(relative_rect=py.Rect((420, 40), (200, 50)),
                text='Health: ' + str("TODO"),
                manager=manager) 

# Game Loop
while playing:
    # Games internal clock, sets number of frames run per second
    clock.tick(FRAMES)

    # Tracks player interaction
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()
        # Places fighter if game manager agrees
        if event.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
  

    screen.fill(green)



    #GUI Updates
    health.set_text("Health: " + "TODO")
    manager.process_events(event)
    manager.update(20)
    manager.draw_ui(screen)

    #Flips all the updates from the loop onto screen
    py.display.update()