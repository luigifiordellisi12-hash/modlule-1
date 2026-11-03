import turtle
screen = turtle.Screen()
screen.bgcolor("midnight blue")
screen.title("Rainbow Flower Spiral")
artist = turtle.Turtle()
artist.speed(0)
artist.pensize(2)
def draw_petal(size, colour):
    artist.color(colour)
    artist.begin_fill()

    artist.circle(size, 90)
    artist.left(90)
    artist.circle(size, 90)

    artist.end_fill()
colours = [
    "hot pink",
    "purple",
    "deepskyblue",
    "turquoise",
    "gold",
    "orange"
]

for i in range(24):
    draw_petal(75, colours[i % len(colours)])
    artist.left(15)
    artist.penup()
artist.goto(0, -20)
artist.pendown()

artist.color("yellow")
artist.begin_fill()
artist.circle(20)
artist.end_fill()
artist.penup()
artist.goto(0, -8)
artist.pendown()

artist.color("white")
artist.begin_fill()
artist.circle(8)
artist.end_fill()
artist.hideturtle()
turtle.done()