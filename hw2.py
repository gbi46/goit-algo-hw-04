import turtle

def koch_curve(t, length, depth):
    """
    Draws a single Koch curve using recursion.

    :param t: turtle object used for drawing
    :param length: length of the current line segment
    :param depth: recursion depth (0 means straight line)
    """
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)

def koch_snowflake(t, length, depth):
    """
    Draws the full Koch snowflake (3 Koch curves forming a triangle).

    :param t: turtle object used for drawing
    :param length: length of each side of the initial triangle
    :param depth: recursion depth
    """
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)

def main():
    # Ask the user for recursion depth
    try:
        depth = int(input("Enter recursion depth (e.g. 0-6): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Set up the drawing screen
    screen = turtle.Screen()
    screen.title("Koch Snowflake")

    # Create the turtle
    t = turtle.Turtle()
    t.speed(0)  # fastest drawing speed

    # Position turtle so the snowflake is centered
    size = 300
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Draw the snowflake
    koch_snowflake(t, size, depth)

    # Keep the window open until user closes it
    screen.mainloop()

if __name__ == "__main__":
    main()
