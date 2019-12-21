



import turtle

window = turtle.Screen()


window.bgcolor("black")




window.title("Tristan's Cool Square Spiral")

turtle_pen = turtle.Pen()








turtle_pen.pencolor("#1288e3")









for counter in range(100):


    turtle_pen.forward(counter)
    turtle_pen.backward(counter)
    turtle_pen.left(145)