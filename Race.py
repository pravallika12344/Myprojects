import turtle as tk
import random
screen=tk.Screen()
screen.listen()
screen.setup(width=500,height=400)
is_race_on=False
colours=["red","green","blue","orange","yellow"]
all_turtles=[]
user_bet=screen.textinput(title="make your bet",prompt="which turtle would you think will win? Choose a colour")
for i in range(len(colours)):

    tik=tk.Turtle(shape="turtle")
    tik.color(colours[i])
    tik.penup()
    tik.goto(x=-230,y=-100+i*50)
    all_turtles.append(tik)

if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
       if turtle.xcor()>230:
           is_race_on=False
           winning_color=turtle.pencolor()
           if winning_color==user_bet:
               print(f"You've won! {winning_color} turtle is the winner")
           else:
               print(f"You've lost! {winning_color} turtle is the winner")
               
       random_distance=random.randint(0,10)
       turtle.forward(random_distance)
screen.exitonclick()