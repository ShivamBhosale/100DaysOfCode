import turtle
import time

width = 600
height = 600
S=turtle.Screen()
S.setup(width,height)
S.bgcolor("Black")
S.title("New Year Countdown 2021")

countdown = 10

pen=turtle.Pen()
pen.hideturtle()

for timer in range(countdown, -1 ,-1):
    pen.clear()
    pen.color("yellow")
    pen.write(timer, align="center", font=(None,80))
    time.sleep(1)

pen.clear()
pen.color("red")
pen.write("Happy New Year 2021!!", align="center", font=(None,50))
turtle.done()