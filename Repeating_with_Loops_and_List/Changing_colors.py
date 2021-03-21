import turtle
tina=turtle.Turtle()
tina.shape("turtle")

colors=["red","orange","yellow","green","blue","purple","black"]

for color in colors:
    angle=360/len(colors)
    tina.color(color)
    tina.circle(40)
    tina.circle(20)
    tina.rt(angle)
    tina.forward(30)

turtle.mainloop()
