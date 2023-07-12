import turtle
import time
import random

def moveTurtle():
    gotoRandomLocation(murtle)
    turtle.onscreenclick(getLocation)

def startGame(): #turtle'ı hareket ettirmek için moveTurtle() fonksiyonunu çağıracak ve 5 saniyelik süre için countdown() fonksiyonu başlayacak.
    moveTurtle()
    countdown(5)

def drawTimer(timerText):
    turtle.clear()
    turtle.penup()
    turtle.color("#563958")
    turtle.hideturtle() #t'yı yazan turtle'ı saklamak için
    turtle.goto(0, 200)  # metinin konumunu ayarlamak için (x= 0, y= 200)
    turtle.write(timerText, align="center", font=("Arial", 23, "bold"))

def drawGameOver():
    turtle.clear()
    turtle.penup()
    turtle.color("#563958")
    turtle.goto(0, 200)
    turtle.write("Game Over", align="center", font=("Arial", 23, "bold"))

def countdown(t):
    while t >= 0:
        if t > 0:
            mins, secs = divmod(t, 60) #divmod t'yı 60'a böler ve bölümü dakika kalanı saniye olarak gösterir.
            timerText = '{:02d}:{:02d}'.format(mins, secs) #format yöntemi ile dakika ve saniyeyi "MM:SS" olarak gösteririz.
            drawTimer(timerText)
        else:
            turtle.onscreenclick(None) #süre bitince tıklamaları devre dışı bırak.
            drawGameOver() #süre bitince ekrana game over yaz.
        time.sleep(1)
        t -= 1
        if t >= 0:
            moveTurtle()


def refreshScore(): #skoru güncellemek ve yazdırmak için kullanılır.
    turtle.clear()
    turtle.penup()
    turtle.color("#563958")
    turtle.hideturtle()
    turtle.goto(0, 250)
    turtle.write("Your Score = {}".format(score), align="center", font=("Arial", 23, "bold"))

def getLocation(x,y):
    xTurtle, yTurtle= murtle.position()
    if abs(x-xTurtle)<= 20 and abs(y- yTurtle)<= 20:
        global score
        score += 1
        refreshScore()

def gotoRandomLocation(murtle):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    murtle.hideturtle()
    murtle.goto(x, y)
    murtle.showturtle()

if __name__ == '__main__':
    turtleScreen = turtle.Screen()
    turtleScreen.bgcolor("#BBAF9C")
    turtleScreen.title("Catch The Turtle")
    turtleScreen.setup(800, 700)  # turtle ekranının büyüklüğü

    murtle = turtle.Turtle()
    murtle.color("#35585F")
    murtle.shape("turtle")
    murtle.penup()

    score = 0

    startGame()
    refreshScore() #skoru yazdırır
    turtle.mainloop()
