import turtle

turtle.shape("turtle")
turtle.speed(1)

for side_length in range(50,100,10):
    for i in range(4):
        print(side_length)
        turtle.forward(side_length)
        turtle.left(90)

turtle.exitonclick()
