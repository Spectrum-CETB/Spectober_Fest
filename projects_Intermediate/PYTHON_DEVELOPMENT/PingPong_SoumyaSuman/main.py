# PING PONG BY SOUMYA SUMAN

import turtle

win= turtle.Screen()
win.title("Ping Pong by Soumya")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

score_a=0
score_b=0

#paddle a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=0.5
ball.dy=0.5

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
#function
def paddle_a_up():
	y=paddle_a.ycor()
	y+=20
	paddle_a.sety(y)
def paddle_a_down():
	y=paddle_a.ycor()
	y-=20
	paddle_a.sety(y)
def paddle_b_up():
	y=paddle_b.ycor()
	y+=20
	paddle_b.sety(y)
def paddle_b_down():
	y=paddle_b.ycor()
	y-=20
	paddle_b.sety(y)


#keyboard binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_a_up,"W")
win.onkeypress(paddle_a_down,"S")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")

#main game loop
while True:
	win.update()
	
	#move the ball
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)
	
	# Border checking

    # Top and bottom
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
	elif ball.ycor() <-290:
		ball.sety(-290)
		ball.dy *= -1
	#left and right
	if ball.xcor() > 350:
		score_a += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		ball.goto(0,0)
		ball.dx *= -1
	elif ball.xcor() <-350:
		score_b += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
		ball.goto(0,0)
		ball.dx *= -1
		
	#paddle-ball collision
	if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
		ball.dx *= -1 
	elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
		ball.dx *= -1
    
