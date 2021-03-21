import turtle
tina=turtle.Turtle()
tina.shape('turtle')

tina.penup()
tina.goto(-60,175)

x,y=tina.pos()
print(x,y)

tina.forward(100)
x,y=tina.pos()
print(x,y)

turtle.mainloop()
