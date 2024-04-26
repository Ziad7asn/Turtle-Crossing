from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.goto(-245,260)
        self.write(f"Level: {self.score}",align="center",font=FONT)

    
    def add_point(self):
        self.score += 1
        self.update_scoreboard()
    
    def stop(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)