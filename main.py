from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter your color: ")

# adding finish line
finish = Turtle()
finish.hideturtle()
finish.penup()
finish.speed(8)
finish.goto(230,250)
finish.right(90)
finish.pendown()
finish.forward(500)

color = ['red', 'blue', 'green', 'purple', 'orange']
position = [-60, -30, 0, 30, 60]
all_turtles = []
for turtle_index in range(5):
    turtle_new = Turtle()
    turtle_new.shape('turtle')
    turtle_new.color(color[turtle_index])
    turtle_new.penup()
    turtle_new.speed(8)
    turtle_new.goto(-230, position[turtle_index])
    turtle_new.pendown()
    all_turtles.append(turtle_new)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            turtle_won = turtle.pencolor()
            if turtle_won == user_bet:
                print(f"You won! The winning turtle is {turtle_won}")
            else:
                print(f"You won! The winning turtle is {turtle_won}")
        turtle.penup()
        turtle.forward(random.randint(0, 10))
        turtle.pendown()
screen.exitonclick()
