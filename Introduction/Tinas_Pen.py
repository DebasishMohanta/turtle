import turtle
tina=turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.goto(0,100)
tina.write("I don't draw when my pen is up!")
tina.goto(0,50)
tina.pendown()
tina.color("green")
tina.write("I do draw when my pen is up!")
tina.goto(-50,50)

turtle.mainloop()
