# part -1 Set up window

import turtle,time,random
delay=0.1
wd=turtle.Screen()
wd.title("snake Xmania")
wd.bgcolor("blue")
wd.setup(width=600,height=600)
wd.tracer(0)

# part -2 Create Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.goto(0,0)
head.penup()
head.direction="stop"

# part -3 set up food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('white')
food.penup()
food.goto(random.randint(-280,280),random.randint(-280,280))

# part -6 Score
score=0
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(160,250)
pen.shape('square')
pen.write(f"SCORE : {score}",align='center',font=('timesnewroman',24,'bold'))



def up():
    if head.direction!='down':
        head.direction="up"
def down():
    if head.direction!='up':
        head.direction="down"
def right():
    if head.direction!='left':
        head.direction="right"
def left():
    if head.direction!='right':
        head.direction="left"
wd.listen()
wd.onkeypress(up,'Up')
wd.onkeypress(down,'Down')
wd.onkeypress(right,'Right')
wd.onkeypress(left,'Left')
body=[]
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
        
pen.hideturtle()
while True:
    wd.update()
    pen.hideturtle()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()<-290 or head.ycor()>290:
        time.sleep(2)
        head.direction="stop"
        head.goto(0,0)
        for i in body:
            i.goto(1000,1000) # go to out of window
        body.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write(f"SCORE : {score}",align='center',font=('timesnewroman',24,'bold'))
    
    if head.distance(food)<20:
        food.goto(random.randint(-290,280),random.randint(-290,290))
        new_body=turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("grey")
        new_body.penup()
        # part -4 Grow the body
        body.append(new_body)
        score+=1
        delay-=0.01
        pen.clear()
        pen.write(f"SCORE : {score}",align='center',font=('timesnewroman',24,'bold'))

    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
        
    move()
    for i in body:
        # part -5 Collision part
        if i.distance(head)<20:
            time.sleep(2)
            head.direction='stop'
            head.goto(0,0)
            for i in body:
                i.goto(1000,1000) # go to out of window
            body.clear()
            score=0
            delay=0.1
            pen.clear()
            pen.write(f"SCORE : {score}",align='center',font=('timesnewroman',24,'bold'))
    time.sleep(delay)
    

wd.mainloop()
