from cgitb import text
import tkinter as tk
from turtle import left
def game1main():
    import turtle
    import os

    wn = turtle.Screen()
    wn.title("Pong By Abhishek3862")
    wn.bgcolor("green")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Score
    score_a = 0
    score_b = 0

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("brown")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("brown")
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("yellow")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = 2

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    # Functions
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    # Keyboard bindings
    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    # Main game loop
    while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1


        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 350:
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1


        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
def game2main(): #snake
    import turtle

    import time

    import random

    delay = 0.1

    score = 0

    high_score = 0

    # Create screen

    wn = turtle.Screen()

    wn.title("Snake Game by Abhishek3862")

    wn.bgcolor("green")

    wn.setup(width=600, height=600)

    wn.tracer(0)

    # head

    head = turtle.Turtle()

    head.shape("square")

    head.color("black")
    head.penup()

    head.goto(0, 0)

    head.direction = "Stop"

    # food

    food = turtle.Turtle()

    colors = random.choice(['red', 'green', 'blue'])

    shapes = random.choice(['square', 'triangle', 'circle'])

    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()

    food.goto(0, 100)

    pen = turtle.Turtle()

    pen.speed(0)

    pen.shape("square")

    pen.color("white")
    pen.penup()
    pen.hideturtle()

    pen.goto(0, 250)

    pen.write("Score : 0  Highest Score : 0", align="center",

              font=("candara", 24, "bold"))

    # key mappiing

    def group():

        if head.direction != "down":
            head.direction = "up"

    def godown():

        if head.direction != "up":
            head.direction = "down"

    def goleft():

        if head.direction != "right":
            head.direction = "left"

    def goright():

        if head.direction != "left":
            head.direction = "right"

    def move():

        if head.direction == "up":
            y = head.ycor()

            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()

            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()

            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()

            head.setx(x + 20)

    wn.listen()

    wn.onkeypress(group, "w")

    wn.onkeypress(godown, "s")

    wn.onkeypress(goleft, "a")

    wn.onkeypress(goright, "d")

    segments = []

    # main game code

    while True:

        wn.update()

        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:

            time.sleep(1)

            head.goto(0, 0)

            head.direction = "Stop"

            colors = random.choice(['red', 'blue', 'green'])

            shapes = random.choice(['square', 'circle'])

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()

            pen.write("Score : {} Highest Score : {} ".format(

                score, high_score), align="center", font=("candara", 24, "bold"))

        if head.distance(food) < 20:

            x = random.randint(-270, 270)

            y = random.randint(-270, 270)

            food.goto(x, y)

            # Add segment or body to the snakek

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

            pen.write("Score : {} Highest Score : {} ".format(

                score, high_score), align="center", font=("candara", 24, "bold"))

        # for moving the body with head

        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()

            y = segments[index - 1].ycor()

            segments[index].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()

            y = head.ycor()

            segments[0].goto(x, y)

        move()

        for segment in segments:

            if segment.distance(head) < 20:

                time.sleep(1)

                head.goto(0, 0)

                head.direction = "stop"

                colors = random.choice(['red', 'blue', 'green'])

                shapes = random.choice(['square', 'circle'])

                for segment in segments:
                    segment.goto(1000, 1000)

                segment.clear()

                score = 0

                delay = 0.1

                pen.clear()

                pen.write("Score : {} Highest Score : {} ".format(

                    score, high_score), align="center", font=("candara", 24, "bold"))

        time.sleep(delay)

    wn.mainloop()
def game3main(): #rpg game
    #rpggui = Toplevel(gui)
    #rpggui.title("rpg game")
    #rpggui.geometry("380x240")
    #frame = LabelFrame(gui,text="game is running", padx=5 , pady=5)

    print('Welcome to Space Wars - Adventure 1.')

    ans = input('Would you like to play? (Yes or no?): ')
    baseHealth = 100

    if ans.lower() == 'yes':
        print('Welcome aboard. Your base health is 100%.')

        ans = input('What do you want to do? (Attack or stay?)')

        if ans.lower() == 'attack':
            baseHealth -= 25
            print('You shoot the cannons at the enemy. You missed. -25 health.')
        else:
            print('You wait for a better time.')

        ans = input('What is your next move? (Advance or defend?)')

        if ans.lower() == 'advance':
            baseHealth -= 50
            print('You advance on the enemy. -50 health.')
        else:
            baseHealth += 10
            print('You activate the shields. +20 health.')

        ans = input('What should we do? (Attack or flank enemy?)')

        if ans.lower() == 'attack':
            print('You hit! The enemy is weak.')
        else:
            baseHealth -= 25
            print('You flanked the enemy, but got attacked. -25 health.')

        if baseHealth == 0:
            print('You got OOFed. Good game!')
        else:
            ans = input('We have to finish them off no matter what. (Fight or die?)')

        if ans.lower() == 'fight':
            print('You blew up the enemy ship. Good job!')
        else:
            print('You die.')

        print("Your base health was:", str(baseHealth) + '%')
    print('Have a good day.')
    #rpggui.mainloop()
def game4main(): #trivia
    print("hello, welcome to the trivia")
    ans = input("Are you ready to play [yes/no]: ")
    score = 0
    total_q = 3
    if ans.lower() == "yes":
        ans = input("no. of bones in an adult body? ")
        if ans.lower() == "206":
            score += 1
            print("Correct")
        else:
            print("incorrect")

        ans = input("default size of a turtle in python in pixels? ")
        if ans.lower() == "20":
            score += 1
            print("Correct")
        else:
            print("incorrect")

        ans = input("no. of teeth in a adult body ?")
        if ans.lower() == "32":
            score += 1
            print("Correct")
        else:
            print("incorrect")

    print("You have got", score, " question right.")


root = tk.Tk()
root.title('Gaming Arcade')

canvas = tk.Canvas(root, height=500, width=900)
canvas.pack()

background_image = tk.PhotoImage(file='grafic.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bg='#2CA4FF')
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

photo1 = tk.PhotoImage(file='pong.png')
photo2 = tk.PhotoImage(file='snake.png')
photo3 = tk.PhotoImage(file='rpg.png')
photo4 = tk.PhotoImage(file='trivia.png')
button1 = tk.Button(frame ,image=photo1 ,command=game1main)
button1.pack(side='left', fill='both', expand=True)
button2 = tk.Button(frame,image=photo2,command=game2main)
button2.pack(side='left', fill='both', expand=True)
button3 = tk.Button(frame,image=photo3,command=game3main)
button3.pack(side='left', fill='both', expand=True)
button4 = tk.Button(frame,image=photo4,command=game4main)
button4.pack(side='left', fill='both', expand=True)

root.mainloop()