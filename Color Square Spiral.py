





import turtle

turtle_pen = turtle.Pen()

window = turtle.Screen()



window.bgcolor("black")




window.title("Tristan's Cool Square Spiral")
COLORS = ["red", "yellow", "blue", "green"]
turtle_pen = turtle.Pen()

















for counter in range(100):
    color = COLORS[counter % 4]

    
    turtle_pen.pencolor(color)


    turtle_pen.forward(counter)
    turtle_pen.backward(counter)
    turtle_pen.left(145)