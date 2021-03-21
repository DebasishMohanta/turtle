import turtle
tina=turtle.Turtle()
tina.shape('turtle')
tina.color('purple')

def triangle():
    tina.forward(100)
    tina.lt(120)
    tina.forward(100)
    tina.lt(120)
    tina.forward(100)
    tina.lt(120)

triangle()

turtle.mainloop()
