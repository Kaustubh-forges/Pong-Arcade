import turtle as t
class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        # initial ball velocities( movement along x and y)
        self.dx=0
        self.dy=0
    def create_ball(self):
        # using turtle to create ball object
        self.ball = t.Turtle()
        self.ball.penup()
        self.speed = self.ball.speed()

        self.ball.shapesize(stretch_wid=1, stretch_len=1)
        self.ball.shape("circle")
        self.ball.color("white")

        # Setting velocity after ball spawns
        self.dx=10
        self.dy=10
    def move_ball(self):
        # Updating ball's position based on current velocity
        new_x=self.ball.xcor()+self.dx
        new_y=self.ball.ycor()+self.dy
        self.ball.goto(new_x,new_y)

    # Inverting ball direction after collision with walls(top/bottom)
    def bounce_top_right(self):
        self.dy*=-1

    def bounce_top_left(self):

        self.dy*=-1

    def bounce_bottom_right(self):

        self.dy*=-1
    def bounce_bottom_left(self):

        self.dy*=-1

    # Resetting ball after point loss
    def after_losing_point(self):
        self.ball.goto(0,0)
        self.dx*=-1

    # Ball collides with paddle and inverts direction
    def ball_paddle_collision(self):
        self.dx*=-1






