import random
import time
import pandas

class Model():
    def __init__(self,stdscr):
        self.stdscr = stdscr
        self.difficulty=0
        self.option = 0
        self.option_2 = 0
        self.score = 0
        self.startTime=time.time()
        self.findingFoodCoordinats = True
        self.h,self.w = stdscr.getmaxyx()
        self.size = 20
        self.center = int(self.size / 2)
        self.headX = self.center
        self.headY = self.center
        self.foodX = random.randint(1, self.size-2)
        self.foodY = random.randint(1,self.size-2)
        self.bodyCoordinats=[]
        self.snakeLen = 0
        self.lastDirection = "E"
        self.direction = "E"
        self.mapa = [[" " for i in range(self.size)] for j in range(self.size)]
        self.mapa[self.headX][self.headY]="H"
        self.tab="" 
        self.df = pandas.read_csv("Scores.csv").sort_values(by=["SCORE"], ascending=False).head(10)
        self.createBorderOfMap()
        

    def whatIsDifficulty(self):
        if self.difficulty == 0:
            return "EASY"
        if self.difficulty == 1:
            return "MEDIUM"
        if self.difficulty == 2:
            return "HARD"

    def createBorderOfMap(self):
        for i in range(self.size):
            if i == 0 or i == self.size-1:
                for k in range(self.size):
                    self.mapa[i][k]="#"
            self.mapa[i][0]="#"
            self.mapa[i][self.size-1]="#"