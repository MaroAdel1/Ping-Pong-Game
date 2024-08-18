import turtle

wind = turtle.Screen() # intialize screen
wind.title('Ping Pong') # set the title of the window
wind.bgpic("rGCS02.png")  # set background color of the window 
wind.setup(width=800, height=600) # set the width and height of the window 
wind.tracer(0) # stops the window from updating automatically

# madrb1
madrb1 = turtle.Turtle()
madrb1.speed(0)
madrb1.shape('square')
madrb1.color('blue')
madrb1.penup()
madrb1.goto(-350,0)
madrb1.shapesize(stretch_wid=5, stretch_len=1)

# madrb2
madrb2 = turtle.Turtle()
madrb2.speed(0)
madrb2.shape('square')
madrb2.color('red')
madrb2.penup()
madrb2.goto(350,0)
madrb2.shapesize(stretch_wid=5, stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.19
ball.dy = 0.19

# Score:
score1 = 0
score2 = 0

score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0,260)
score.write('Player_1: 0    Player_2: 0', align='center', font=('Courier', 24, 'normal'))

# functions:
def madrb1_up():
    y = madrb1.ycor()
    y += 20
    madrb1.sety(y)

def madrb1_down():
    y = madrb1.ycor()
    y -= 20
    madrb1.sety(y)

def madrb2_up():
    y = madrb2.ycor()
    y += 20
    madrb2.sety(y)

def madrb2_down():
    y = madrb2.ycor()
    y -= 20
    madrb2.sety(y)

# keyboard bindings
wind.listen()

wind.onkeypress(madrb1_up, 'w')

wind.onkeypress(madrb1_down, 's')

wind.onkeypress(madrb2_up, 'Up')

wind.onkeypress(madrb2_down, 'Down')




# Main game loop
while True:
    wind.update() # updates the screen everytime the loop run
    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write('Player_1: {}    Player_2: {}'.format(score1, score2), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write('Player_1: {}    Player_2: {}'.format(score1, score2), align='center', font=('Courier', 24, 'normal'))

    # Ball collision

    if (ball.xcor()> 340 and ball.xcor() <350) and (ball.ycor() < madrb2.ycor() + 40 and ball.ycor() > madrb2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrb1.ycor() + 40 and ball.ycor() > madrb1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1