import turtle as t  
import random

#initial settings
landscape=t.Turtle()
tree=t.Turtle()
star=t.Turtle()
present=t.Turtle()
snowman=t.Turtle()
hat=t.Turtle()
#hide turtle, leaving the lines
landscape.hideturtle()
tree.hideturtle()
star.hideturtle()
present.hideturtle()
snowman.hideturtle()
hat.hideturtle()

wn=t.Screen()
t.bgcolor("grey")
#screen size 
wn.setup(1000,600)

# background
def drawLandscape():
    landscape.pencolor("blue")
    landscape.shape("circle")
    landscape.goto(-500,0)
    landscape.goto(500,0)

# tree
def drawTree():
    #stump
    tree.fillcolor("brown")
    #begin fill -> https://holypython.com/python-turtle-tutorial/turtle-fill/
    tree.begin_fill()
    tree.pencolor("brown")
    tree.goto(-30,0)
    tree.goto(-30,40)
    tree.goto(30,40)
    tree.goto(30,0)
    tree.goto(0,0)
    tree.end_fill()
    #pines left side 
    tree.penup()
    tree.pencolor("green")
    tree.goto(-30,40)
    tree.pendown()
    tree.fillcolor("green")
    tree.begin_fill()
    tree.goto(-90,40)
    tree.goto(-60,80)
    tree.goto(-70,80)
    tree.goto(-40,120)
    tree.goto(-50,120)
    tree.goto(0,180)

    #pines right side
    tree.goto(0,180)
    tree.goto(50,120)
    tree.goto(40,120)
    tree.goto(70,80)
    tree.goto(60,80)
    tree.goto(90,40)
    tree.goto(0,40)
    tree.end_fill()
    tree.penup()

    # tree ornaments 
    tree.fillcolor("red")
    tree.pencolor("red")
    # min and max y values go up to spread out ornaments
    minOrnament=40
    maxOrnament=60
    # make 6 ornaments
    for i in range(6):
        tree.goto(random.randint(-25,25),random.randint(minOrnament,maxOrnament))
        tree.pendown()
        tree.begin_fill()
        tree.circle(7)
        tree.end_fill()
        tree.penup()
        # increase the y values
        minOrnament+=17
        maxOrnament+=17

#star 
def drawStar():
    star.penup()
    star.fillcolor("yellow")
    star.begin_fill()
    star.pencolor("yellow")
    star.goto(0,180)
    star.pendown()
    star.goto(-20,170)
    star.goto(-10,190)
    star.goto(-20,200)
    star.goto(-5,210)
    star.goto(0,220)
    star.goto(5,210)
    star.goto(20,200)
    star.goto(10,190)
    star.goto(20,170)
    star.goto(0,180)
    star.end_fill()
    star.penup

#present
def drawPresent():
    present.penup()
    present.fillcolor("red")
    present.begin_fill()
    present.pencolor("green")
    present.goto(200,0)
    present.pendown
    present.goto(200,50)
    present.goto(250,50)
    present.goto(250,0)
    present.goto(200,0)
    present.end_fill()
    present.penup()
    # wrappers
    present.pencolor("green")
    present.pensize(4)
    present.goto(200,25)
    present.pendown()
    present.goto(250,25)
    present.penup()
    present.goto(225,50)
    present.pendown()
    present.goto(225,0)
    present.penup()

#snowman
def drawSnowman():
    snowman.penup()
    snowman.goto(-300,0)
    snowman.pencolor("white")
    snowman.fillcolor("white")
    snowman.begin_fill()
    snowman.pendown()
    snowman.circle(50)
    snowman.goto(-300,100)
    snowman.circle(35)
    snowman.goto(-300,170)
    snowman.circle(20)
    snowman.penup()
    snowman.end_fill()

#text
def drawText():
    writer=t.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(-100,-200)
    writer.color('black')
    writer.pendown()
    writer.write("Happy Holidays",font=("Verdanan",20,"normal"))
    writer.penup()

'''
# image
image=t.Turtle
wn.addshape('Christmas-clip-art-free-images-graphics-clipartcow.png')
image.shape('Christmas-clip-art-free-images-graphics-clipartcow.png')
'''


# hat
def drawHat():
    hat.goto(-300,-100)
    hat.pencolor('red')
    hat.fillcolor('red')
    hat.begin_fill()
    for i in range(3):
        hat.fd(50)
        hat.right(120)
    hat.end_fill()

# snow
def snow(numberOfFlakes,colorOfSnow,farLeft,farRight,upper,lower,speed,variation,ground):
    snowFlakes=[]
    for i in range(100):
        s=t.Turtle(shape='circle')
        s.color(colorOfSnow)
        s.speed(0)
        s.penup()
        s.goto(random.randint(farLeft,farRight),random.randint(lower,upper))   #r -> random module 
        snowFlakes.append(s)

    # running code 
    while True:
        for s in snowFlakes:
            newX=s.xcor()+random.randint(-variation,variation)
            newY=s.ycor()+random.randint(-speed,0)
            s.goto(newX,newY)
            if s.ycor()<-ground:
                s.stamp()
                s.sety(random.randint(lower,upper))
                



# call functions            
drawLandscape()
drawTree()
drawStar()
drawPresent()
drawSnowman()
drawText()
drawHat()
snow(50,"white",-(wn.window_width()/2),(wn.window_width()/2),425,320,30,5,300)
wn.mainloop()