import random
import keyboard
import time
import curses

class Controller_Text():
    def __init__(self,stdscr,model):
        self.model = model
        self.stdscr = stdscr
        self.key = None

    def menuControll(self,view):
        if keyboard.is_pressed("up") and self.model.option>=0:
            time.sleep(0.2)
            self.model.option = self.model.option - 1
            if self.model.option == -1:
                self.model.option = 2

        if keyboard.is_pressed("down") and self.model.option <= 2:
            time.sleep(0.2)
            self.model.option = self.model.option + 1
            if self.model.option == 3:
                self.model.option = 0

    def endMenuControll(self,view):
        if keyboard.is_pressed("up") and self.model.option>=0:
            time.sleep(0.2)
            self.model.option = self.model.option - 1
            if self.model.option == -1:
                self.model.option = 1

        if keyboard.is_pressed("down") and self.model.option <= 1:
            time.sleep(0.2)
            self.model.option = self.model.option + 1
            if self.model.option == 2:
                self.model.option = 0

    def difficultyControll(self,view):
        if keyboard.is_pressed("up") and self.model.option_2>=0:
            time.sleep(0.2)
            self.model.option_2 = self.model.option_2 - 1
            if self.model.option_2 == -1:
                self.model.option_2 = 3
        if keyboard.is_pressed("down") and self.model.option_2 <= 3:
            time.sleep(0.2)
            self.model.option_2 = self.model.option_2 + 1
            if self.model.option_2 == 4:
                self.model.option_2 = 0

    def isSubmitClicked(self):
        if keyboard.is_pressed("enter"):
            time.sleep(0.2)
            return True
        else:
            return False
            

    def inputDirection(self):
        if self.model.key == curses.KEY_DOWN and self.model.lastDirection !="N":
            self.model.direction = "S"

        if self.model.key == curses.KEY_UP and self.model.lastDirection !="S":
            self.model.direction = "N"

        if self.model.key == curses.KEY_LEFT and self.model.lastDirection !="E":
            self.model.direction = "W"

        if self.model.key == curses.KEY_RIGHT and self.model.lastDirection !="W":
            self.model.direction = "E"

    def setSpeed(self):
        if self.model.difficulty == 0:
            self.model.speed = 0.3
        if self.model.difficulty == 1:
            self.model.speed = 0.2
        if self.model.difficulty == 2:
            self.model.speed = 0.1

            
    def addPoint(self):
        if self.model.difficulty == 0:
            self.model.score = self.model.score + 1
        if self.model.difficulty == 1:
            self.model.score = self.model.score + 2
        if self.model.difficulty == 2:
            self.model.score = self.model.score + 3
    
    def saveScore(self):
        file = open("Scores.csv","a")
        file.write(f"\n{self.model.tab},{self.model.score*20},{round(self.model.scoreBoardTime)}")
        file.close()

    def findingFoodCoordinats(self):
        while self.model.findingFoodCoordinats:
            self.model.foodX = random.randint(1, self.model.size-2)
            self.model.foodY = random.randint(1, self.model.size-2)
            if [self.model.foodX,self.model.foodY] not in self.model.bodyCoordinats:
                self.model.findingFoodCoordinats = False
        self.model.findingFoodCoordinats = True

    def checkIfHeadHitBody(self):
        return [self.model.headX, self.model.headY] in self.model.bodyCoordinats
    
    def updateTableMap(self):
        self.model.mapa[self.model.foodX][self.model.foodY]="@"
        for i in self.model.bodyCoordinats:
            self.model.mapa[i[0]][i[1]]="B"
        self.model.mapa[self.model.headX][self.model.headY]="H"
    
    def getUserKeyInput(self):
        try:
            self.model.key = self.stdscr.getch()
        except:
            self.key = None
    
        
        
