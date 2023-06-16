import graphics
import time
import random
import math

DELAY = 0.025

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600

BALL_RADIUS = 10
BALL_DIAMETER = BALL_RADIUS *2
x_ball = (CANVAS_WIDTH / 2) - BALL_RADIUS
y_ball = (CANVAS_HEIGHT / 2) - BALL_RADIUS

BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH - BRICK_GAP * 9) / 10
BRICK_HEIGHT = 10
x_coor = (CANVAS_WIDTH - (BRICK_WIDTH * 10) - (BRICK_GAP * 9)) / 2

PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15

NUMBER_OF_BRICKS = 0

# Create canvas
canvas = graphics.Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

# Create ball
ball = canvas.create_oval(x_ball, y_ball, x_ball+BALL_DIAMETER, y_ball+BALL_DIAMETER)
canvas.set_color(ball, "purple")

# Create paddle
paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, PADDLE_Y+PADDLE_HEIGHT)

def main():
    brick_colors = ["red", "orange", "yellow", "green", "cyan"]

    # Setup the blocks
    for column in range(10):
        for row in range(10):
            y = row * (BRICK_HEIGHT + BRICK_GAP)
            x = x_coor + column * (BRICK_WIDTH + BRICK_GAP)
            color = brick_colors[row // 2]
            bricks = canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT, color)

    # Animation loop
    change_x = 10
    change_y = random.randint(10, 15)
    while True:
        canvas.move(ball, change_x, change_y)
        #update multiple variables 
        change_x, change_y = bounce(change_x, change_y)
        paddle_track()
        time.sleep(DELAY)
        
        # out of paddle
        bottom_y = canvas.get_top_y(ball) + BALL_DIAMETER
        if bottom_y > CANVAS_HEIGHT:
            print("you lose")
            break   
        
        # check last brick
        if NUMBER_OF_BRICKS == 100:
            print("You won") said 
            break
    ####################################

def bounce(change_x, change_y):
    nonlocal NUMBER_OF_BRICKS  # Add this line

    left_x = canvas.get_left_x(ball)
    top_y = canvas.get_top_y(ball)
    right_x = canvas.get_left_x(ball) + BALL_DIAMETER
    bottom_y = canvas.get_top_y(ball) + BALL_DIAMETER

    colliding_list = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    number_of_elements = len(colliding_list)
    print(colliding_list)

    # wall collision
    if left_x < 0 or right_x > CANVAS_WIDTH:
        change_x = -change_x
        
    # paddle collision
    if "shape_1" in colliding_list:
        change_y = -change_y
    
    # brick collision
    if  number_of_elements > 1 and "shape_1" not in colliding_list:
        # deletes the brick
        canvas.delete(colliding_list[1]) 
        NUMBER_OF_BRICKS +=1
        change_y = -change_y
    
    return change_x, change_y
    
    
    
    ####################################   

def paddle_track():
    mouse_x = canvas.get_mouse_x()
    canvas.moveto(paddle, mouse_x, PADDLE_Y)
    return 

     
if __name__ == '__main__':
    main()
