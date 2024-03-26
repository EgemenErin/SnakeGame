from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        starting_pos = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_pos:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)


    def up(self):
        self.head.setheading(90)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)

    def down(self):
        self.head.setheading(270)
