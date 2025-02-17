from math import sqrt

import turtle


#Create the screen and the drawer
s = turtle.Screen()
s.title('Tic-Tac-Toe')
t = turtle.Turtle()

#Draw the game board
def draw_line(x, y, angle=0):
    t.penup()
    t.goto(x, y)
    t.right(angle)
    t.pendown()
    t.forward(600)

draw_line(-250, 300, 90)
draw_line(-50, 300)
draw_line(-450, 100, -90)
draw_line(-450, -100)

#Create circles and crosses
n_circles = 0
n_crosses = 0

def draw_circle():    
    t.right(90)
    t.forward(75)
    t.left(90)
    t.pendown()
    t.circle(75)

    global n_circles
    n_circles += 1


def draw_cross():
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

    global n_crosses
    n_crosses += 1


#Draw circles or crosses when you click on the board
circle_centers = []
cross_centers = []

def make_move(x, y, x_min, x_max, y_min, y_max):
    if -450 < x < 150 and -300 < y < 300:
        global circle_centers, cross_centers
        center = [(x_min + x_max) / 2, (y_min + y_max) / 2]

        if center not in circle_centers and center not in cross_centers and \
            x_min < x < x_max and y_min < y < y_max:
            t.penup()
            t.goto(center[0], center[1])

            if n_circles == n_crosses:
                draw_circle()
                circle_centers.append(center)
            elif n_circles > n_crosses:
                draw_cross()
                cross_centers.append(center)


def win_move():
    row_centers = [[[-350, 200], [-150, 200], [50, 200]], 
                   [[-350, 0], [-150, 0], [50, 0]], 
                   [[-350, -200], [-150, -200], [50, -200]]]
    
    column_centers = [[[-350, 200], [-350, 0], [-350, -200]], 
                      [[-150, 200], [-150, 0], [-150, -200]], 
                      [[50, 200], [50, 0], [50, -200]]]
    
    diagonal_centers = [[[-350, 200], [-150, 0], [50, -200]], 
                        [[50, 200], [-150, 0], [-350, -200]]]


    for i in range(3):
        if row_centers[i] in circle_centers:
            t.penup()
            t.goto(-450, row_centers[i[1]])
            t.pendown()
            t.heading(0)
            t.forward(600)
            turtle.done()

    for i in range(3):
        if column_centers[i] in circle_centers:
            t.penup()
            t.goto(column_centers[i[0]], 300)
            t.pendown()
            t.heading(-90)
            t.forward(600)
            turtle.done()

    for i in range(2):
        if diagonal_centers[i] in circle_centers:
            t.penup()
            t.goto(diagonal_centers[i[0]] - 100, 300)
            if diagonal_centers[i[0]] == -350:
                t.heading(-45)
            elif diagonal_centers[i[0]] == 50:
                t.heading(225)
            t.pendown()
            t.forward(sqrt(2) * 600)
            turtle.done()


def click(x, y):
    make_move(x, y, -450, -250, 100, 300)
    make_move(x, y, -250, -50, 100, 300)
    make_move(x, y, -50, 150, 100, 300)
    make_move(x, y, -450, -250, -100, 100)
    make_move(x, y, -250, -50, -100, 100)
    make_move(x, y, -50, 150, -100, 100)
    make_move(x, y, -450, -250, -300, -100)
    make_move(x, y, -250, -50, -300, -100)
    make_move(x, y, -50, 150, -300, -100)
    win_move()


s.onclick(click)
turtle.done()