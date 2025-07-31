# Pong Arcade Project

#------------------------

# Modules implemented
import turtle as t
import  time
import paddle
import ball
import score

# Screen setup and aesthetics
screen=t.Screen()
screen.title("Pong")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

# Creating ball object + Use of class "Ball"
ball=ball.Ball()
ball.create_ball()

# Creating scorecard + Use of class "Score"
score=score.Score()

# Creating paddle + Paddle placement near walls using class "Paddle"
paddle_right=paddle.Paddle(350)
paddle_left=paddle.Paddle(-350)
paddle_right.Create_Paddle()
paddle_left.Create_Paddle()

# Gameplay controls + Detection of user clicks using method "onkey()"
screen.onkey(fun=paddle_right.move_up, key="Up")
screen.onkey(fun=paddle_left.move_up, key="w")
screen.onkey(fun=paddle_left.move_down, key="s")
screen.onkey(fun=paddle_right.move_down, key="Down")

# Debug leftover: checking turtle's default speed (not used in gameplay)....because why not
speed = ball.ball.speed()
print(speed)

# Constants
speed=0.1


game_on=True

# Big bad loop which acts as the backbone
while game_on:
    time.sleep(speed) # Slowing loop down and managing ball speed
    screen.update() # Manually making the screen re-draw everything after one full loop
    ball.move_ball() # Making the ball move
  # Bounce off of the top and bottom walls
    if ball.ball.xcor() >= 0 and ball.ball.ycor() >280:
        ball.bounce_top_right()
    if ball.ball.xcor()<=0 and ball.ball.ycor()>280:
         ball.bounce_top_left()
    if ball.ball.xcor()>=0 and ball.ball.ycor()<-280:
         ball.bounce_bottom_right()
    if ball.ball.xcor()<=0 and ball.ball.ycor()<-280:
         ball.bounce_bottom_left()

    # Paddle collision detection( along with sending the ball back) + increasing the speed of the ball after every detection
    if ball.ball.distance(paddle_right.paddle)<50 and ball.ball.xcor()>330 or ball.ball.distance(paddle_left.paddle)<50 and ball.ball.xcor()<-330:
        ball.ball_paddle_collision()
        speed*=0.9

    # Detecting win and distributing point to the winner + Adjusting speed of the ball for new round
    if ball.ball.xcor()>380:
        ball.after_losing_point()
        score.add_point_left()
        speed=0.1
    if ball.ball.xcor()<-380:
        ball.after_losing_point()
        score.add_point_right()
        speed=0.1

    # Detecting end of game + Recording and presenting the winner
    if score.l_score==5 or score.r_score==5:
        game_on=False
        screen.clear()
        screen.bgcolor("light grey")
        screen.title("Game Over!")
        game_over=t.Turtle()
        game_over.penup()
        game_over.goto(x=0,y=-70)
        game_over.hideturtle()
        if score.l_score==5:
            game_over.write(f"Left side wins!\nFinal scores are:-\nLeft side:{score.l_score}\nRight side:{score.r_score}",align="center", font=("Consolas", 50, "normal"))
        elif score.r_score==5:
            game_over.write(
                f"Right side wins!\nFinal scores are:-\nLeft side:{score.l_score}\nRight side:{score.r_score}",
                align="center", font=("Consolas", 50, "normal"))


screen.exitonclick()