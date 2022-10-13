import curses
import re
import time
import random
import pandas
from curses import wrapper
from curses.textpad import Textbox
class model():
    pass
class View():
    
    def __init__(self,stdscr):
        self.stdscr = stdscr
        self.h,self.w = stdscr.getmaxyx()

    def mainMenu(self):
        self.start(60,10)
        self.stdscr.addstr(self.h//2,self.w//2-5,f"START")
        self.stdscr.addstr(self.h//2+1,self.w//2-5,f"DIFFICULTY")
        self.stdscr.addstr(self.h//2+2,self.w//2-5,f"SCORES")
        self.stdscr.refresh()

    def start(self,x,y):
        self.stdscr.addstr(y,x,"""
                        _______ __   _ _______ _     _ _______       ______ _______ _______ _______
                        |______ | \  | |_____| |____/  |______      |  ____ |_____| |  |  | |______
                        ______| |  \_| |     | |    \_ |______      |_____| |     | |  |  | |______
        """)
        self.stdscr.refresh()

    def difficultyMenu(self,difficulty):
        self.stdscr.addstr(self.h//2-2,self.w//2-12,f"ACTUAL DIFFICULTY:{whatIsDifficulty(difficulty)}")
        self.stdscr.addstr(self.h//2,self.w//2-6,f"EASY")
        self.stdscr.addstr(self.h//2+1,self.w//2-6,f"MEDIUM")
        self.stdscr.addstr(self.h//2+2,self.w//2-6,f"HARD")
        self.stdscr.addstr(self.h//2+4,self.w//2-6,f"BACK")
        self.stdscr.refresh()

    def legend(self,score,scoreBoardTime,difficulty,direction):
        self.stdscr.addstr(21,self.w//2-10,f"Time:{round(scoreBoardTime)} Score:{score*20}")
        self.stdscr.addstr(20,self.w//2-10,f"direction:{direction}")
        self.stdscr.addstr(22,self.w//2-10,f"difficulty:{whatIsDifficulty(difficulty)}")
        self.stdscr.refresh()

    def scoreTable(self):
        self.stdscr.addstr(0,0,f"{readScores()}")
        self.stdscr.addstr(self.h//2+2,self.w//2-5,f"BACK<")
        self.stdscr.refresh()
    def arrowsMainMenu(self,option):
        if option == 0:
            self.stdscr.addstr(self.h//2,self.w//2,f"<")
            self.stdscr.addstr(self.h//2+1,self.w//2+5,f" ")
            self.stdscr.addstr(self.h//2+2,self.w//2+1,f" ")
        if option == 1:
            self.stdscr.addstr(self.h//2,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+1,self.w//2+5,f"<")
            self.stdscr.addstr(self.h//2+2,self.w//2+1,f" ")
        if option == 2:
            self.stdscr.addstr(self.h//2,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+1,self.w//2+5,f" ")
            self.stdscr.addstr(self.h//2+2,self.w//2+1,f"<")
        self.stdscr.refresh()

    def arrowsDifficultyMenu(self,option):
        if option == 0:
            self.stdscr.addstr(self.h//2,self.w//2,f"<")
            self.stdscr.addstr(self.h//2+1,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+2,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+4,self.w//2,f" ")
        if option == 1:
            self.stdscr.addstr(self.h//2,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+1,self.w//2,f"<")
            self.stdscr.addstr(self.h//2+2,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+4,self.w//2,f" ")
        if option == 2:
            self.stdscr.addstr(self.h//2,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+1,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+2,self.w//2,f"<")
            self.stdscr.addstr(self.h//2+4,self.w//2,f" ")
        if option == 3:
            self.stdscr.addstr(self.h//2,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+1,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+2,self.w//2,f" ")
            self.stdscr.addstr(self.h//2+4,self.w//2,f"<")
        self.stdscr.refresh()


        
def setSpeed(difficulty):
    if difficulty == 0:
        return 0.3
    if difficulty == 1:
        return 0.2
    if difficulty == 2:
        return 0.1

def readScores():
    df =pandas.read_csv("Scores.csv")
    df= df.sort_values(by=["SCORE"], ascending=False)
    return df.head(10)

def whatIsDifficulty(number):
    if number == 0:
        return "EASY"
    if number == 1:
        return "MEDIUM"
    if number == 2:
        return "HARD"


def gameOver(stdscr,score,time):
    tab=""
    stdscr.clear()
    option = 0
    h,w = stdscr.getmaxyx()
    stdscr.addstr(10,0,"""
                             ______ _______ _______ _______       _____  _    _ _______  ______
                            |  ____ |_____| |  |  | |______      |     |  \  /  |______ |_____/
                            |_____| |     | |  |  | |______      |_____|   \/   |______ |    \_
                                                                                                    
    """)
    stdscr.refresh()
    while True:
        try:
            key = stdscr.getch()
        except:
            key = None
        stdscr.addstr(h//2,w//2-6,f"YOUR SCORE IS:{score*20} AND THE TIME:{round(time)}")
        stdscr.addstr(h//2+1,w//2-6,f"DO YOU WANT TO SAVE YOUR SCORE?:")
        stdscr.addstr(h//2+2,w//2-6,f"YES")
        stdscr.addstr(h//2+3,w//2-6,f"NO")
        
        if key == curses.KEY_UP and option>=0:
            option = option - 1
            if option == -1:
                option = 1
        if key == curses.KEY_DOWN and option <= 1:
            option = option + 1
            if option == 2:
                option = 0
        if option == 0:
                stdscr.addstr(h//2+2,w//2,f"<")
                stdscr.addstr(h//2+3,w//2,f" ")
                stdscr.refresh()
        if option == 1:            
                stdscr.addstr(h//2+2,w//2,f" ")
                stdscr.addstr(h//2+3,w//2,f"<")
                stdscr.refresh()
        if key == curses.KEY_LEFT and option == 1:
            exit()
        if key == curses.KEY_LEFT and option == 0:
            stdscr.clear()

            editwin = curses.newwin(1,16, h//2+1,w//2)
            stdscr.addstr(h//2,w//2,f"INSERT YOUR NAME:")
            stdscr.refresh()
            box = Textbox(editwin)
            box.edit()
            tab = box.gather()

            file = open("Scores.csv","a")
            file.write(f"\n{tab},{score*20},{round(time)}")
            file.close()
            stdscr.refresh()
            exit()
            
                

def createMap(size):
    array = [[" " for i in range(size)] for j in range(size)]
    return array

def main(stdscr):
    stdscr.nodelay(True)
    curses.curs_set(0)
    view = View(stdscr)
    
    difficulty=0
    option = 0
    option_2 = 0
    score = 0
    startTime=time.time()
    findingFoodCoordinats = True
    h,w = stdscr.getmaxyx()
    size = 20
    center = int(size / 2)
    headX = center
    headY = center
    foodX = random.randint(1, size-2)
    foodY = random.randint(1, size-2)
    bodyCoordinats=[]
    snakeLen = 0
    lastDirection = "E"
    direction = "E"
    mapa = createMap(size)
    mapa[headX][headY]="H"
    for i in range(size):
        if i == 0 or i == size-1:
            for k in range(size):
                mapa[i][k]="#"
        mapa[i][0]="#"
        mapa[i][size-1]="#"
    sample = time.time()
    stdscr.clear()

    while True:
        try:
            key = stdscr.getch()
        except:
            key = None

        if key == curses.KEY_UP and option>=0:
            option = option - 1
            if option == -1:
                option = 2
        if key == curses.KEY_DOWN and option <= 2:
            option = option + 1
            if option == 3:
                option = 0
        if key == curses.KEY_LEFT and option == 0:
            break
        if key == curses.KEY_LEFT and option == 2:
            stdscr.clear()
            while True:
                try:
                    key = stdscr.getch()
                except:
                    key = None
                view.scoreTable()
                if key == curses.KEY_LEFT:
                    stdscr.clear()
                    break
        if key == curses.KEY_LEFT and option == 1:
            stdscr.clear()
            while True:
                try:
                    key = stdscr.getch()
                except:
                    key = None

                view.difficultyMenu(difficulty)

                if key == curses.KEY_UP and option_2>=0:
                    option_2 = option_2 - 1
                    if option_2 == -1:
                        option_2 = 2
                if key == curses.KEY_DOWN and option_2 <= 3:
                    option_2 = option_2 + 1
                    if option_2 == 4:
                        option_2 = 0

                view.arrowsDifficultyMenu(option_2)
                if key == curses.KEY_LEFT and option_2 == 3:
                    stdscr.clear()
                    break
                if key == curses.KEY_LEFT:
                    stdscr.clear()
                    difficulty = option_2
        view.mainMenu()
        view.arrowsMainMenu(option)
    stdscr.clear()

    speed = setSpeed(difficulty)
    
    while True:
        new = time.time()
        difference = new - sample
        try:
            key = stdscr.getch()
        except:
            key = None

        lastDirection = direction

        if key == curses.KEY_DOWN and lastDirection !="N":
            direction = "S"
        if key == curses.KEY_UP and lastDirection !="S":
            direction = "N"
        if key == curses.KEY_LEFT and lastDirection !="E":
            direction = "W"
        if key == curses.KEY_RIGHT and lastDirection !="W":
            direction = "E"

        if(difference > speed):
            sample = time.time()
            mapa[headX][headY]=" "
            mapa[foodX][foodY]=" "

            if bodyCoordinats!=[]:
                if not((headX == foodX) and (headY == foodY)):
                    helper = bodyCoordinats.pop(0)
                    mapa[helper[0]][helper[1]]=" "
                if((headX == foodX) and (headY == foodY)):
                    pass
                else:
                    bodyCoordinats.append([headX,headY])
                

            if((headX == foodX) and (headY == foodY)):
                while findingFoodCoordinats:
                    foodX = random.randint(1, size-2)
                    foodY = random.randint(1, size-2)
                    if [foodX,foodY] not in bodyCoordinats:
                        findingFoodCoordinats = False
                findingFoodCoordinats = True

                if difficulty == 0:
                    score = score + 1
                if difficulty == 1:
                    score = score + 2
                if difficulty == 2:
                    score = score + 3
                    
                bodyCoordinats.append([headX,headY])
                
                snakeLen = snakeLen + 1

            if direction == "S" and lastDirection !="N":
                if headY < size - 2:
                    headY = headY + 1
                    if [headX,headY] in bodyCoordinats:
                        gameOver(stdscr,score,scoreBoardTime)
                else:
                    gameOver(stdscr,score,scoreBoardTime)
                    
            if direction == "N" and lastDirection !="S":
                if headY >= 2:
                    headY = headY - 1
                    if [headX,headY] in bodyCoordinats:
                        gameOver(stdscr,score,scoreBoardTime)
                else:
                    gameOver(stdscr,score,scoreBoardTime)

            if direction == "E" and lastDirection !="W":
                if headX < size-2:
                    headX = headX + 1
                    if [headX,headY] in bodyCoordinats:
                        gameOver(stdscr,score,scoreBoardTime)
                else:
                    gameOver(stdscr,score,scoreBoardTime)

            if direction == "W" and lastDirection !="E":
                if headX >= 2:
                    headX = headX - 1
                    if [headX,headY] in bodyCoordinats:
                        gameOver(stdscr,score,scoreBoardTime)
                else:
                    gameOver(stdscr,score,scoreBoardTime)
            
            mapa[foodX][foodY]="F"
            for i in bodyCoordinats:
                mapa[i[0]][i[1]]="B"
            mapa[headX][headY]="H"
            
        for i in range(size):
                for j in range(size):
                    stdscr.addstr(j,i+w//2-size//2,str(mapa[i][j]))
        scoreBoardTime = time.time() - startTime
        view.legend(score,scoreBoardTime,difficulty,direction)
wrapper(main)