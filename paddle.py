import turtle as t

class Paddle(t.Turtle):
    def __init__(self,x):
        super().__init__()
        # Initial position of paddle
        self.x=x
        self.y=0
    def Create_Paddle(self):
        # Using turtle to create paddle
        self.paddle = t.Turtle()
        self.paddle.penup()
        self.paddle.goto(self.x, 0)
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")

    # Paddle moves(up/down)
    def move_up(self):
        self.y += 40
        self.paddle.goto(self.x, self.y)

    def move_down(self):

        self.y -= 40
        self.paddle.goto(self.x, self.y)




