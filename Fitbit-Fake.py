import random
from turtle import *
import time

COLOR = (0.2039215686, 0.3409803922, 0.5921568627)
TARGET = (0, 0.7, 0.99218)

screen = Screen()
screen.tracer(False)

WIDTH, HEIGHT = 700, 500

deltas = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]

turtle = Turtle()
turtle.color(COLOR)

turtle.penup()
turtle.goto(-WIDTH/2, HEIGHT/2)
turtle.pendown()

direction = 1

for distance, y in enumerate(range(HEIGHT//2, -HEIGHT//2, -1)):

    turtle.forward(WIDTH * direction)
    turtle.color([COLOR[i] + delta * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)

    direction *= -1

screen.tracer(True)


penup()
color("white", "white")
setup(width=700, height=500, startx=None, starty=None)
penup()

penup()
goto(-330,225)
pendown()
begin_fill()
signal = input(str("(max 5)(as int)what signal strenth = "))
circle(10, extent=None, steps=None)
penup()
if signal == "1":
    end_fill()
forward(25)
pendown()
circle(10, extent=None, steps=None)
penup()
if signal == "2":
    end_fill()
forward(25)
pendown()
circle(10, extent=None, steps=None)
penup()
if signal == "3":
    end_fill()
forward(25)
pendown()
circle(10, extent=None, steps=None)
penup()
if signal == "4":
    end_fill()
forward(25)
pendown()
circle(10, extent=None, steps=None)
penup()
end_fill()
        

forward(25)
right(90)
forward(2)
left(90)
pendown()
mobileCarr = input("what is your moblie carrier = ").upper()
write(mobileCarr, font=("Arial", 13 ,"normal"))

penup()
goto(230, 225)
pendown()
batper = input("battery percentage = ")
write(batper + "%", font=("Arial", 13 ,"normal"))
penup()
goto(275, 228)
#drawing battery outline
pendown()
forward(35)
left(90)
forward(5)
right(90)
forward(2)
left(90)
forward(5)
left(90)
forward(2)
right(90)
forward(5)
left(90)
forward(35)
left(90)
forward(15)
#drawing percentage
batPerIn = (int(batper)/35)* 12.25
begin_fill()
left(90)
forward(int(batPerIn))
left(90)
forward(15)
left(90)
forward(int(batPerIn))
left(90)
forward(15)
end_fill()
penup()
    
goto(-330, 190)

color("lightblue", "lightblue")
begin_fill()
left(135)
pendown()
forward(25)
right(90)
forward(5)
right(90)
forward(20)
left(90)
forward(20)
right(90)
forward(5)
right(90)
forward(25)
end_fill()
penup()

goto(-300, 172)
write("Heart Rate", font=("Arial", 20 ,"normal"))
color("white", "white")

goto(-65, 170)
day = input("what is the day of the week = ")
write(day, font=("Arial", 20 ,"normal"))

goto(-110, 119)
color("pink", "pink")
write("♥", font=("Arial", 20 ,"normal"))
goto(-85, 122)
color("white", "white")
write("Beats Per Minute", font=("Arial", 15 ,"normal"))

goto(-330, 50)
write("175", font=("Arial", 13 ,"normal"))
right(45)
forward(10)
right(90)
forward(40)
pendown()
forward(610)
penup()

goto(-330, -75)
write("125", font=("Arial", 13 ,"normal"))
left(90)
forward(10)
right(90)
forward(40)
pendown()
forward(610)
penup()

goto(-330, -200)
write("50", font=("Arial", 13 ,"normal"))
left(90)
forward(10)
right(90)
forward(40)
pendown()
forward(610)
penup()

goto(-250, -230)
workoutStartHour = input("What hour did you start your workout? = ")
workoutStartMin = input("How many minutes of the hour did you start your workout? = ")
write(workoutStartHour+":"+workoutStartMin, font=("Arial", 13 ,"normal"))

goto(250, -230)
workoutEndHour = input("What hour did you end your workout? = ")
workoutEndMin = input("How many minutes of the hour did you end your workout? = ")
write(workoutEndHour+":"+workoutEndMin, font=("Arial", 13 ,"normal"))

#making line
yPoints = [-160, -155, -140, -155, -130, -110, -120, -80, -100, -50, -60, -20, 0, 10, -20, 15, 5, 20, 0, 30, 10, 40, 20, 26, 10, 45, -30, -25,-10, -32, 10, 0, 20, 15, 30, 25, 40, 45, 30, 40, 20, 45, 15, 20, 10, 25, 20, 35, 30 ,45, 40 ,30, 35, 20, -30, -50, -40, -10, 10, 20, 5, 20, 15, 30 ,45, 35, 50, 40 ,49, 55, 40, 50, 45, 30, 40, 20, 25, 25, 10, 0, 7, 10, 15, 10, 15, 10, 5, 0 , -10, 5, -15 - 30, -20, -40, -50, -40, -100, -130, -120, -150, -140, -160, -150, -160, -140, -160, -150, -160, -140, -160]

color("red", "black")
penup()
pensize(6)
curX = -250
curY = 250
xStep = 5
goto(-250, -160)
print("plotting...") 

for i in yPoints:    
    pendown()
    curY = i
    randNum = random.randint(-5, 10)
    randY = i + randNum
    print(curX, ",",  randY)
    goto(curX, randY)
    curX  = curX + xStep
    time.sleep(0.25)

penup()
goto(-1000, 1000)

done()
