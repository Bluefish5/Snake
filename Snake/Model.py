import random
import time
import pandas

class Model():
    def __init__(self,stdscr,size):
        self.stdscr = stdscr
        self.scoreBoardTime = None
        self.new = None
        self.sample = None
        self.key = None
        self.startTime = None

        self.difficulty=0
        self.option = 0
        self.option_2 = 0
        self.score = 0
        self.snakeLen = 0
        self.size = size

        self.userText="" 
        self.lastDirection = "E"
        self.direction = "E"

        self.findingFoodCoordinats = True

        self.bodyCoordinats=[]

        self.center = int(self.size / 2)
        self.headX = self.center
        self.headY = self.center
        self.foodX = random.randint(1, self.size-2)
        self.foodY = random.randint(1,self.size-2)
        
        self.mapa = [[" " for i in range(self.size)] for j in range(self.size)]
        self.mapa[self.headX][self.headY]="H"
        if size == 30:
            self.h,self.w = stdscr.getmaxyx()
        
        self.df = pandas.read_csv("Scores.csv").sort_values(by=["SCORE"], ascending=False).head(10)
        self.df = self.df.to_string(index=False)
        self.createBorderOfMap()
        
    def createBorderOfMap(self):
        for i in range(self.size):
            if i == 0 or i == self.size-1:
                for k in range(self.size):
                    self.mapa[i][k]="#"
            self.mapa[i][0]="#"
            self.mapa[i][self.size-1]="#"