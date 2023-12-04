
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.speed(1)  # Set the drawing speed

# Function to draw a water faucet


def draw_faucet():
    pen.penup()
    pen.goto(-20, -100)
    pen.pendown()
    pen.color("gray")
    pen.goto(20, -100)
    pen.goto(0, 0)
    pen.goto(-10, 0)
    pen.goto(-10, -100)
    pen.hideturtle()

# Function to draw a bucket


def draw_bucket():
    pen.penup()
    pen.goto(40, -100)
    pen.pendown()
    pen.color("blue")
    pen.goto(90, -100)
    pen.goto(90, -50)
    pen.goto(40, -50)
    pen.goto(40, -100)
    pen.hideturtle()


# Main drawing
draw_faucet()
draw_bucket()

# Add a message
pen.penup()
pen.goto(-100, 50)
pen.pendown()
pen.color("black")
pen.write("Save Water", font=("Arial", 16, "bold"))

# Close the drawing window on click
screen.exitonclick()
