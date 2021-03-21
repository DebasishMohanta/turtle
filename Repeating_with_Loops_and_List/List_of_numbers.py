import turtle
tina=turtle.Turtle()
tina.shape("turtle")

number_list=list(range(1,11))

tina.color("green")
for num in number_list:
    tina.forward(num*10)
    tina.lt(60)

turtle.mainloop()
