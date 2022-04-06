import turtle

wn = turtle.Screen()
wn.title('Pong by Lemons122')
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.shapesize(stretch_len=0.5, stretch_wid=7)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_len=0.5, stretch_wid=7)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.shapesize(stretch_len=0.75, stretch_wid=0.75)
ball.dx = 0.05
ball.dy = 0.05


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    print(y)
    if y >= 230:
        paddle_a.sety(y)
    else:
        y += 10
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    print(y)
    if y <= -220:
        paddle_a.sety(y)
    else:
        y -= 10
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    print(y)
    if y >= 230:
        paddle_b.sety(y)
    else:
        y += 10
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    print(y)
    if y <= -220:
        paddle_b.sety(y)
    else:
        y -= 10
        paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Keeps it from closing/Main game
while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() > 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 20) or (ball.xcor() < -340 and ball.xcor() <-350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):

        ball.dx *= -1
