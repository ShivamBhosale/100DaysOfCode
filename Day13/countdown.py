import turtle
import time

width = 600
height = 500
S=turtle.Screen()
S.setup(width,height)
S.bgcolor("lightgreen")
S.title("New Year Countdown")

countdown = 10

pen=turtle.Pen()
pen.hideturtle()

for timer in range(countdown, -1 ,-1):
    pen.clear()
    pen.write(timer, align="center", font=(None,80))
    time.sleep(2)

pen.clear()
pen.color("red")
pen.write("Happy New Year 2021",align="center", font=(None,80))