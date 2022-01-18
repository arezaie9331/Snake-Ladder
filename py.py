from os import read
import pygame,sys
import random
import time as t
from pygame import *
from functions import *

clock = pygame.time.Clock()

# Temp vals 
turn = 1
player1_pos = 1
player2_pos = 1
randi=0
end_bool = True

# set colors 
red = (255,0,0)
# green = (0,255,0)
# blue = (0,0,255)
aqua = (0,255,255)
white = (255,255,255)
black = (0,0,0)
gray = (150,150,255)

# Set windows 
pygame.init()
win = display.set_mode((600,750))
display.set_caption("My Game")

# display.set_icon()

# Set Background 
bg = image.load("back.png")
bg = transform.scale(bg , (600,600))

# set texts 
P_name_font = font.Font(None,40)
P_turn_font = font.Font(None,30)
rand_font = font.Font(None,100)
player_1_name = P_name_font.render("Player 1",True,black)
player_2_name = P_name_font.render("Player 2",True,black)
player_1_turn = P_turn_font.render("Your turn.",True,black)
player_2_turn = P_turn_font.render("Your turn.",True,black)

# circles
player1_x = 20
player2_x = 45
player1_y = 563
player2_y = 585

# Functions
def nish(now_home):
    _ , last = is_nish(now_home)
    x,y = return_x_y(last)
    return x , y

def nardeboon(now_home):
    _ , last = is_nardeboon(now_home)
    x , y = return_x_y(last)
    return x , y

def Go():
    global turn
    global randi
    global end_bool
    # Player 1 turn
    if (turn==1):
        global player1_pos
        global player1_x
        global player1_y
        # Get the random num beetwin 1 and 6
        randi = random.randint(1,6)
        # Check Can player go or not
        if player1_pos+randi<=100:
            # Check the last of game
            if player1_pos+randi==100:
                end_bool = False                
            # Going on number in a for
            for m in range(randi):
                player1_pos+=1
                player1_x , player1_y = return_x_y(player1_pos)
                # Set the statics
                player1_y -= 40
                player1_x +=20
                # Show the player position
                draw.circle(win,aqua,(player1_x,player1_y),15)
                display.update()
                time.wait(100)             
            # Check the Nardeboon
            nardeboon_t,last_n = is_nardeboon(player1_pos)
            if nardeboon_t:
                player1_x , player1_y = nardeboon(player1_pos)
                # Set the statics
                player1_x += 20
                player1_y -=40
                player1_pos = last_n
                draw.circle(win,aqua,(player1_x,player1_y),15)
                display.update()
            # Check the 6 and awards
            if randi != 6:
                # Change turn
                turn = 0
                # Check the nish
                nish_t , last = is_nish(player1_pos)
                if nish_t:
                    player1_x , player1_y = nish(player1_pos)
                    player1_x += 20
                    player1_y -=40
                    player1_pos = last
                    draw.circle(win,aqua,(player1_x,player1_y),15)
                    display.update()
        elif randi!=6 :
            # Change turn
            turn = 0  
    # Player 2 turn
    else:
        global player2_pos
        global player2_x
        global player2_y
        # Get the random num beetwin 1 and 6
        randi = random.randint(1,6)
        # Check Can player go or not
        if player2_pos+randi<=100:
            # Check the last of game
            if player2_pos+randi==100:
                end_bool = False
            # Going on number in a for
            for m in range(randi):
                player2_pos+=1
                player2_x , player2_y = return_x_y(player2_pos)
                # Set the statics
                player2_y -= 20
                player2_x +=45
                # Show the player position
                draw.circle(win,red,(player2_x,player2_y),15)
                display.update()
                time.wait(100)
            # Check the Nardeboon
            nardeboon_t,last_n = is_nardeboon(player2_pos)
            if nardeboon_t:
                player2_x , player2_y = nardeboon(player2_pos)
                # Set the statics
                player2_x += 45
                player2_y -=20
                player2_pos = last_n
                draw.circle(win,red,(player2_x,player2_y),15)
                display.update()
            # Check the 6 and awards
            if randi != 6:
                # Change turn
                turn = 1
                # Check the nish
                nish_t , last = is_nish(player2_pos)
                if nish_t:
                    player2_x , player2_y = nish(player2_pos)
                    player2_x += 45
                    player2_y -=20
                    player2_pos = last
                    draw.circle(win,red,(player2_x,player2_y),15)
                    display.update()
        elif randi!=6 :
            # Change turn
            turn = 1 

# Main Loop
while end_bool:
    # Show BackGrounds
    win.fill(gray)
    win.blit(bg,(0,0))
    # Show texts
    player_1_score = P_name_font.render(f"{player1_pos}",True,black)
    player_2_score = P_name_font.render(f"{player2_pos}",True,black)
    player_rand = rand_font.render(f"{randi}",True,black)
    win.blit(player_1_name,(50,720))
    win.blit(player_2_name,(450,720))
    win.blit(player_1_score,(90,670))
    win.blit(player_2_score,(490,670))
    win.blit(player_rand,(275,670))
    # Show the turn texts
    if (turn==1):
        win.blit(player_1_turn,(55,610))
    else:
        win.blit(player_2_turn,(455,610))
    # Show first position of players
    draw.circle(win,aqua,(player1_x,player1_y),15)
    draw.circle(win,(255,0,0),(player2_x,player2_y),15)
    # Event Handeling
    for e in event.get():
        # Set the Exit Key
        if e.type == QUIT:
            quit();
            sys.exit()
        # Set the click for doing jobs
        if e.type == MOUSEBUTTONDOWN:
            Go()
    #Display and positions Updating  
    display.update()

# End Of Game
while True:
    win.fill(gray)
    if player1_pos == 100 :
        player_win = rand_font.render("Player 1 wins!",True,black)
    else:
        player_win = rand_font.render("Player 2 wins!",True,black)
    win.blit(player_win,(0,0))
    display.update()
    for e in event.get():        
        if e.type == QUIT:
            quit();
            sys.exit()
        if e.type == MOUSEBUTTONDOWN:
            quit();
            sys.exit()