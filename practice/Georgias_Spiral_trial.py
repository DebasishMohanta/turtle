import turtle
wn=turtle.Screen()
wn.bgcolor("black")
tina=turtle.Turtle()
tina.shape("turtle")
tina.pensize(2)

def draw_circle(x):
    for i in range(60,120,x):
        tina.speed(0)
        tina.circle(i)

def draw_special(x):
    for _ in range(10):
        draw_circle(x)
        tina.rt(36)

colors=["white","yellow","blue","orange","pink"]
x=10
for color in colors:
    tina.color(color)
    draw_special(x)
    x+=3

turtle.mainloop()
