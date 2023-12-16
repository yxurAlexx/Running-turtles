import turtle
import time
import random
class Player:
    balance = 200
    bet = 0
    TargetTurtle = 0
    def __init__(self, name):
        self.name = name
T = turtle.Turtle()
T.speed(100)
T.shape("turtle")
T.up()
T.goto(-360, 320)
T.down()
def drawField():
    for i in range(12):
        for i in range(2):
            T.forward(700)
            T.right(90)
            T.forward(50)
            T.right(90)
        T.right(90)
        T.forward(50)
        T.left(90)

turtles = []
turtlesDist = []
colors = ['cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'brown', 'orange', 'silver', 'black', 'navy', 'teal',  'aquamarine',  'green yellow', 'lime',  'olive drab',  'dark khaki']
def generateTurtles():
    turtles.clear()
    for i in range(12):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(random.choice(colors))
        t.up()
        t.goto(-370, 295-50*i)
        t.write("№: " +str(i+1))
        turtles.append(t)
        turtlesDist.append(0)
def startGame():
    player.TargetTurtle = input("Какая черепаха победит: ")
    while True:
        bet = input("Введите ставку: ")
        if bet.isdigit():
            player.bet = int(bet)
            if player.bet > player.balance:
                player.bet = player.balance
            player.balance -= player.bet
            break
        else: print("Неверная ставка")
    if player.TargetTurtle == startRun():
        winMoney = player.bet *3
        player.balance += winMoney
        player.bet = 0
        print("Вы угадали.Вы выиграли: ", winMoney)
    else: print("Вы не угадали")
def startRun():
    while True:
        for i in range(len(turtles)):
            dist = random.randint(1, 5)
            turtles[i].forward(dist)
            turtlesDist[i] += dist
            if turtlesDist[i]> 700: return str(i+1)

player = Player(input("What is your name: "))
drawField()
generateTurtles()
startGame()


turtle.done()