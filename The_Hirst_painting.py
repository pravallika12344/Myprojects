import turtle as tk
import random
tim=tk.Turtle()
tk.colormode(255)
no_of_dots=100
tim.penup()
tim.speed("fastest")
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

color_list=[(150,75,49),(223,201,135),(172,154,48),(52,93,124),(18,86,90),(81,148,129),(148,17,20),(14,70,64),(30,68,100),(107,127,153),(174,94,97),(176,192,209)]
for i in range(1,no_of_dots+1):
    tim.dot(10,random.choice(color_list))
    tim.forward(50)
    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)                  



screen=tk.Screen()
screen.exitonclick()