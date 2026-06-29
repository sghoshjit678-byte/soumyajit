import random
import time
import turtle

from pygame import mixer

# 1. Audio Setup with Safety Catch
mixer.init()
try:
    mixer.music.load("happy-birthday-song.mp3")  # Ensure this file exists!
    mixer.music.play()
except Exception:
    print("Music file not found, continuing without audio.")

# Sets background
bg = turtle.Screen()
bg.bgcolor("black")

# Bottom Line 1
turtle.penup()
turtle.goto(-170, -180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160, -150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150, -120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)
bg.bgcolor("lightgreen")

# Cake
turtle.penup()
turtle.goto(-100, -100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()
bg.bgcolor("lightblue")

# Candles
turtle.penup()
turtle.goto(-90, 0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-60, 0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(-30, 0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(0, 0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)
turtle.penup()
turtle.goto(30, 0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
bg.bgcolor("orange")

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40, -50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

bg.bgcolor("red")

# 2. FIXED: Dedicated Text Turtle for Animation
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.color("yellow")

# Initial text display
text_turtle.goto(0, 50)
text_turtle.write(
    arg="Happy Birthday CodeWithRandom!",
    align="center",
    font=("jokerman", 20, "normal"),
)
time.sleep(1.5)

# Bouncing Animation (alters Y position up and down)
y_positions = [50, 70, 50, 70, 50, 70, 50]

for pos in y_positions:
    text_turtle.clear()  # Only clears what text_turtle drew!
    text_turtle.goto(0, pos)
    text_turtle.write(
        arg="Happy Birthday CodeWithRandom!",
        align="center",
        font=("jokerman", 20, "normal"),
    )
    time.sleep(0.3)

turtle.done()