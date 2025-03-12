from math import sqrt
import turtle


# Initialize the screen and the drawer
s = turtle.Screen()
s.title('Tic-Tac-Toe')
t = turtle.Turtle()

# Game state
centers = [[], []]
n_circles = 0
n_crosses = 0

# Draw the game board
def draw_line(x, y, angle, length=600):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.forward(length)

def draw_board():
    draw_line(-250, 300, -90)
    draw_line(-50, 300, -90)
    draw_line(-450, 100, 0)
    draw_line(-450, -100, 0)

# Draw circles and crosses
def draw_circle():
    s.onclick(None)
    global n_circles
    n_circles += 1
    t.pencolor('blue')
    t.setheading(-90)
    t.forward(75)
    t.setheading(0)
    t.pendown()
    t.circle(75)
    s.onclick(click)

def draw_cross():
    s.onclick(None)
    global n_crosses
    n_crosses += 1
    t.pencolor('red')
    t.setheading(-45)
    t.backward(sqrt(2) * 75)
    t.pendown()
    t.forward(sqrt(2) * 150)
    t.penup()
    t.setheading(90)
    t.forward(150)
    t.setheading(225)
    t.pendown()
    t.forward(sqrt(2) * 150)
    s.onclick(click)

# Handle clicks
def make_move(x, y, x_center, y_center):
    if -450 < x < 150 and -300 < y < 300:
        x_min, x_max = x_center - 100, x_center + 100
        y_min, y_max = y_center - 100, y_center + 100
        center = [x_center, y_center]
        if center not in centers[0] and center not in centers[1] and \
        x_min < x < x_max and y_min < y < y_max:
            t.penup()
            t.goto(center[0], center[1])
            if n_circles == n_crosses:
                draw_circle()
                centers[0].append(center)
            elif n_circles > n_crosses:
                draw_cross()
                centers[1].append(center)

# Check if someone wins the game
def check_win(win=False):
    angles = [-45, 225]
    x_increments = [-100, 100]
    row_centers = [
        [-350, 200], [-350, 0], [-350, -200], [-150, 200], [-150, 0], 
        [-150, -200], [50, 200], [50, 0], [50, -200], 
    ]
    column_centers = [
        [-350, 200], [-150, 200], [50, 200], [-350, 0], [-150, 0], [50, 0], 
        [-350, -200], [-150, -200], [50, -200], 
    ]
    diagonal_centers = [
        [-350, 200], [50, 200], [-150, 0], [50, -200], [-350, -200], 
    ]
    for i in range(2):
        for l in range(3):
            if row_centers[l] in centers[i] and \
            row_centers[l + 3] in centers[i] and \
            row_centers[l + 6] in centers[i]:
                draw_line(row_centers[l][0] - 100, row_centers[l][1], 0)
                win = True
            elif column_centers[l] in centers[i] and \
            column_centers[l + 3] in centers[i] and \
            column_centers[l + 6] in centers[i]:
                draw_line(column_centers[l][0], column_centers[l][1] + 100, -90)
                win = True
        for l in range(2):
            if diagonal_centers[l] in centers[i] and \
            diagonal_centers[2] in centers[i] and \
            diagonal_centers[l + 3] in centers[i]:
                draw_line(diagonal_centers[l][0] + x_increments[l], \
                diagonal_centers[l][1] + 100, angles[l], sqrt(2) * 600)
                win = True
    return win

# Write the results of the game
def last_move():
    if check_win():
        t.penup()
        t.setheading(0)
        t.goto(175, 0)
        if n_circles > n_crosses:
            t.write('PLAYER 1 WINS!', font = ('Arial', 25))
        elif n_circles == n_crosses:
            t.write('PLAYER 2 WINS!', font = ('Arial', 25))
        s.onclick(None)
    elif n_circles + n_crosses == 9:
        t.penup()
        t.setheading(0)
        t.goto(175, 0)
        t.pencolor('black')
        t.write('THE GAME ENDS\nIN A DRAW', font = ('Arial', 25))
        s.onclick(None)

# Keep playing the game until someone wins
def click(x, y):
    grid_centers = [
        [-350, 200], [-150, 200], [50, 200], [-350, 0], [-150, 0], [50, 0], 
        [-350, -200], [-150, -200], [50, -200], 
    ]
    for center in grid_centers:
        make_move(x, y, center[0], center[1])
    last_move()

# Start the game
draw_board()
s.onclick(click)
turtle.done()