import turtle
import time
import random

# set up screen
from typing import Any, Union

window = turtle.Screen()
window.title("Snake")
window.bgcolor("green")
window.setup(width=700, height=700)
segments = []

# draw borders
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(4)
for s in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
window.tracer(0)

# score
score = 0
high_score = 0
scorePen = turtle.Turtle()
scorePen.speed(0)
scorePen.shape("square")
scorePen.color("white")
scorePen.penup()
scorePen.hideturtle()
scorePen.goto(0, 310)
scorePen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# fruit

fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("red")
fruit.penup()
fruit.goto(0, 100)


# functions

def moveUp():
    if head.direction != "down":
        head.direction = "up"


def moveDown():
    if head.direction != "up":
        head.direction = "down"


def moveLeft():
    if head.direction != "right":
        head.direction = "left"


def moveRight():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def addSegment():
    newSeg = turtle.Turtle()
    newSeg.speed(0)
    newSeg.shape("square")
    newSeg.color("grey")
    newSeg.penup()
    segments.append(newSeg)


def moveSegments():
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    # move the first seg to head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


def borderCollision():
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for i in segments:
            i.goto(1000, 1000)
        segments.clear()
        return True
    else:
        return False


def fruitCollision():
    if head.distance(fruit) < 20:
        # spawn fruit
        x = random.randint(-285, 285)
        y = random.randint(-285, 285)
        fruit.goto(x, y)
        addSegment()
        # Increase the score
        return True
    else:
        return False


# keyboard controls
window.listen()
window.onkeypress(moveUp, "w")
window.onkeypress(moveDown, "s")
window.onkeypress(moveLeft, "a")
window.onkeypress(moveRight, "d")

# main loop
while True:
    window.update()

    if fruitCollision():
        score += 10
        if score > high_score:
            high_score = score
        scorePen.clear()
        scorePen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if borderCollision():
        score = 0
        scorePen.clear()
        scorePen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # body collision
    for x in segments:
        if x.distance(head) < 20:
            x = True
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for i in segments:
                i.goto(1000, 1000)
            segments.clear()
            score = 0
            scorePen.clear()
            scorePen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    moveSegments()
    move()

    time.sleep(0.09)

window.mainloop()
