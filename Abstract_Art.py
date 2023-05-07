import turtle as t

na = t.Turtle()
nb = t.Turtle()
nc = t.Turtle()
win = t.Screen()

win.bgcolor("black")
win.title("Abstract")

x = 70
y = 40
z = 10

na.hideturtle()
na.speed(100)

nb.hideturtle()
nb.speed(100)

nc.hideturtle()
nc.speed(100)

for i in range(65):
    x = x+2
    y = y+2
    z = z+2
    
    na.color("red")
    na.circle(x)
    na.lt(10)
    
    nb.color("blue")
    nb.circle(y)
    nb.lt(10)

    nc.color("yellow")
    nc.circle(z)
    nc.lt(10)

t.done()