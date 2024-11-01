import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Decorated Jack-O-Lantern")

# Set up the turtle for the pumpkin
pumpkin = turtle.Turtle()
pumpkin.speed(3)

# Draw a filled circle
def draw_circle(t, radius, color, x=0, y=0):
    t.penup()
    t.goto(x, y-radius)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw a triangle
def draw_triangle(t, x, y, length, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()

# Draw the pumpkin stem
def draw_stem(t):
    t.penup()
    t.goto(-20, 140)
    t.pendown()
    t.color("dark green")
    t.fillcolor("green")
    t.begin_fill()
    t.goto(20, 140)
    t.goto(10, 180)
    t.goto(-10, 180)
    t.goto(-20, 140)
    t.end_fill()

# Draw leaves for decoration
def draw_leaf(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("dark green")
    t.fillcolor("green")
    t.begin_fill()
    t.circle(10, 180)
    t.left(90)
    t.circle(10, 180)
    t.end_fill()
    t.setheading(0)

# Draw pumpkin body
draw_circle(pumpkin, 150, "orange")

# Draw stem
draw_stem(pumpkin)

# Draw leaves around the stem
draw_leaf(pumpkin, -30, 160)
draw_leaf(pumpkin, 30, 160)

# Eyes
draw_triangle(pumpkin, -50, 50, 40, "black")
draw_triangle(pumpkin, 10, 50, 40, "black")

# Nose
draw_triangle(pumpkin, -20, 20, 30, "black")

# Draw a wavy mouth
pumpkin.penup()
pumpkin.goto(-60, -40)
pumpkin.setheading(-30)
pumpkin.color("black")
pumpkin.width(2)
pumpkin.pendown()
for _ in range(4):
    pumpkin.forward(20)
    pumpkin.left(60)
    pumpkin.forward(20)
    pumpkin.right(60)

# Draw a couple of square teeth for extra detail
pumpkin.penup()
pumpkin.goto(-40, -30)
pumpkin.setheading(0)
pumpkin.color("black")
pumpkin.pendown()
pumpkin.begin_fill()
pumpkin.goto(-20, -10)
pumpkin.goto(-40, -10)
pumpkin.goto(-40, -30)
pumpkin.end_fill()

pumpkin.penup()
pumpkin.goto(10, -30)
pumpkin.pendown()
pumpkin.begin_fill()
pumpkin.goto(20, -10)
pumpkin.goto(0, -10)
pumpkin.goto(10, -30)
pumpkin.end_fill()

# Hide the turtle
pumpkin.hideturtle()

# Keep the window open until clicked
turtle.done()
