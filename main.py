import turtle

#Create Screen
sc = turtle.Screen()
sc.title("Tim's Pong Game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

#Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

#Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

#Ball Size
hit_ball = turtle.Turtle()
hit_ball.speed(500)
hit_ball.shape("square")
hit_ball.color("red")
hit_ball.penup()
hit_ball.goto(0,0)
hit_ball.dx = 5
hit_ball.dy = -5

#Scoreboard
left_score = 0
right_score = 0

#Display the Score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("red")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left Player: 0       Right Player: 0", align="center", font=("Courier", 24, "normal"))

#Function to Move the Paddles
def paddle_Left_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

def paddle_Right_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)

def paddle_Left_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

def paddle_Right_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)

#Keyboard Bindings
sc.listen()
sc.onkeypress(paddle_Left_up, "w")
sc.onkeypress(paddle_Left_down, "s")
sc.onkeypress(paddle_Right_up, "Up")
sc.onkeypress(paddle_Right_down, "Down")

#The Game Itself
while True:
    sc.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    #Check the borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0 ,0)
        hit_ball.dy *= -1
        left_score += 1
        sketch.clear()
        sketch.write("Left Player: {}       Right Player: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0 ,0)
        hit_ball.dy *= -1
        right_score += 1
        sketch.clear()
        sketch.write("Left Player: {}       Right Player: {}".format(left_score, right_score), align="center", font=("Courier", 24, "normal"))

    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 40 and hit_ball.ycor() > right_pad.ycor() -40):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 40 and hit_ball.ycor() > left_pad.ycor() - 40):
        hit_ball.setx(-360)
        hit_ball.dx *= -1
