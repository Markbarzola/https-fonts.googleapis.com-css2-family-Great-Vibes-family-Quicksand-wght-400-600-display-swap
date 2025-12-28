import turtle

t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("white")

# Cabeza
t.penup()
t.goto(0, -100)
t.pendown()
t.color("pink")
t.begin_fill()
t.circle(100)  # círculo para la cabeza
t.end_fill()

# Orejas
t.penup()
t.goto(-70, 50)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(70, 50)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()

# Ojos
t.penup()
t.goto(-40, -20)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(40, -20)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Nariz
t.penup()
t.goto(0, -40)
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(8)
t.end_fill()

# Moño (lado izquierdo)
t.penup()
t.goto(-80, 80)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-110, 80)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-95, 100)
t.pendown()
t.begin_fill()
t.circle(15)
t.end_fill()

t.hideturtle()
turtle.done()