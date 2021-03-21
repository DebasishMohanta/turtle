import turtle

def make_circle(turtle,color,size,x,y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(size)
    turtle.end_fill()

tina=turtle.Turtle()
tina.shape("turtle")

make_circle(tina,"green",100,50,0)
make_circle(tina,"blue",100,0,0)
make_circle(tina,"yellow",100,-50,0)

tina.penup()
tina.color("black")
tina.goto(0,-50)
tina.write("Let's Learn Python!",align="center",font=(None,20,"bold"))
tina.goto(0,-80)

turtle.mainloop()
