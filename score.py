import turtle as t
class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        # Initial scores at the start
        self.l_score=0
        self.r_score=0
        # Updating side that gains point
        self.update_sides()

    # Adding point on left paddle
    def add_point_left(self):
        self.l_score+=1
        self.clear()
        self.update_sides()

    # updating sides each round
    def update_sides(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(200,200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    # Adding point for right paddle
    def add_point_right(self):
        self.r_score+=1
        self.clear()
        self.update_sides()





