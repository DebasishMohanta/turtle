import turtle
tina=turtle.Turtle()
tina.shape("turtle")

colors=["black","blue","purple","green"]

tina.lt(90)

for color in colors:
    tina.forward(20)
    tina.color(color)
    tina.write("What color am I now?")


turtle.mainloop()
