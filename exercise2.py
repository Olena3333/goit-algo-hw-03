import turtle

def koch_curve(t : turtle.Turtle, order : int, size : float):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order : int, size=450):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    try:
        lvl = int(input("Enter the recursion level for the snowflake: "))
        draw_koch_snowflake(lvl)
    except ValueError:
        print("You should enter Integer number")