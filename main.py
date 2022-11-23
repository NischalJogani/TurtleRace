import random
import turtle
from turtle import Turtle, Screen

race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Turtle Pink/Blue/Purple/Green/Orange/Red/Yellow:      ")


def make_race_lines():
    start_turt = Turtle("turtle")
    finish_turt = Turtle("turtle")
    start_turt.ht()
    finish_turt.ht()
    start_turt.penup()
    start_turt.speed(0)
    finish_turt.penup()
    finish_turt.speed(0)
    start_turt.goto(x=-250, y=170)
    finish_turt.goto(x=250, y=170)
    start_turt.setheading(270)
    finish_turt.setheading(270)
    start_turt.pendown()
    finish_turt.pendown()
    start_turt.forward(340)
    finish_turt.forward(340)


y_positions = [-150, -100, -50, 0, 50, 100, 150]
colors = ["blue", "purple", "green", "yellow", "orange", "red", "DeepPink"]
all_turtles = []


for turtle_index in range(7):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

make_race_lines()

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else:
                print(f"You lost! The {winning_color} turtle won the race.")

    for turtle in all_turtles:
        rand_distance = random.randint(0, 5)
        turtle.forward(rand_distance)

screen.exitonclick()
