import turtle 
import time
import random
delay = 0.25
score = 0
high_score = 0
#setup the screen
wdo = turtle.Screen()
wdo.title("Priya's snake game")
wdo.bgcolor("gray")
wdo.setup(700,700)
wdo.tracer(0)
#snake head
head = turtle.Turtle()
head.shape("square")
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction="Stop"
#food in the game
food = turtle.Turtle()
colors = random.choice(['red','green' ,'blue'])
shapes = random.choice(['square','triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score: 0 High Score : 0", align="center", font = ("candara", 24, "bold"))
#assigning key directions
def go_up():
    if head.direction!="down":
        head.direction="up"

def go_down():
    if head.direction!="up":
        head.direction = "down"


def go_right():
    if head.direction!="left":
        head.direction ="right"

def go_left():
    if head.direction!="right":
        head.direction = "left"


def move():
    if head.direction == "up":
        y = head.ycor()# y cordinate of the head
        head.sety(y+20)


    if head.direction == "down":
        y = head.ycor()# y cordinate of the head
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor() #x cordinate of the head
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor() #x cordinate of the head
        head.setx(x-20)
#keyboard bindings
wdo.listen()
wdo.onkeypress(go_up,"Up")
wdo.onkeypress(go_down,"Down")
wdo.onkeypress(go_right,"Right")
wdo.onkeypress(go_left,"Left")
segments =[]
#main gameplay
while True:
    wdo.update()    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(['red','green' ,'blue'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score:{}".format( score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        #Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score:{} High Score: {}".format(score,high_score), align = "center", font = ("candara", 24, "bold"))

    #check for head collisions with body segments

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            colors = random.choice(['red','green' ,'blue'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.25
            pen.clear()
            pen.write("Score:{} High Score: {}".format(score,high_score), align = "center", font = ("candara", 24, "bold"))
    time.sleep(delay)
wdo.mainloop()
