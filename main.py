from pygame import *
import time

# Set windows 
init()
win = display.set_mode((972,486))
display.set_caption("My Game")

# Set Background 
bg = image.load("splash.jpg")
bg = transform.scale(bg , (972,486))
win.blit(bg,(0,0))
display.update()

while True:
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN or e.type == QUIT:
            import py
            quit()



