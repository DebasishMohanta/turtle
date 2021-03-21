import turtle
tina=turtle.Turtle()
tina.shape("turtle")

colors=["white","yellow","blue","pink"]
def give_color():
    for color in colors:
        tina.color(color)
        draw_circle()
def draw_circle():
    for i in range(60,120,10):
        tina.speed(0)
        tina.circle(i)
def draw_special():
    angle=360/10
    for _ in range(10):
        tina.rt(angle)
    draw_circle()

turtle.mainloop()
