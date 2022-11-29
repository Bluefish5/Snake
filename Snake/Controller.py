import random
import pygame
import time

class Controller():
    def __init__(self,model):
        self.model = model
        self.key = None    

    def inputDirection(self):
        if self.model.key[pygame.K_DOWN] and self.model.lastDirection !="N":
            self.model.direction = "S"

        if self.model.key[pygame.K_UP] and self.model.lastDirection !="S":
            self.model.direction = "N"

        if self.model.key[pygame.K_LEFT] and self.model.lastDirection !="E":
            self.model.direction = "W"

        if self.model.key[pygame.K_RIGHT] and self.model.lastDirection !="W":
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
        file.write(f"\n{self.model.userText},{self.model.score*20},{round(self.model.scoreBoardTime)}")
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
            self.model.key = pygame.key.get_pressed()
        except:
            self.model.key = None

    
                
    def menuControll(self,view):
        pos = pygame.mouse.get_pos()
        if (view.image.BUTTON_START_RECT.collidepoint(pos)):
            self.model.option = 0
        elif (view.image.BUTTON_DIFFICULTY_RECT.collidepoint(pos)):
            self.model.option = 1
        elif (view.image.BUTTON_SCORE_RECT.collidepoint(pos)):
            self.model.option = 2
        else:
            self.model.option = -1

    def isSubmitClicked(self):
        if pygame.mouse.get_pressed()[0]==1:
            time.sleep(0.2)
            return True
        else:
            return False

    def difficultyControll(self,view):
        pos = pygame.mouse.get_pos()
        if (view.image.BUTTON_EASY_RECT.collidepoint(pos)):
            if pygame.mouse.get_pressed()[0]==1:
                self.model.option_2 = 0
        if (view.image.BUTTON_MEDIUM_RECT.collidepoint(pos)):
            if pygame.mouse.get_pressed()[0]==1:
                self.model.option_2 = 1
        if (view.image.BUTTON_HARD_RECT.collidepoint(pos)):
            if pygame.mouse.get_pressed()[0]==1:
                self.model.option_2 = 2
        if (view.image.BUTTON_BACK_RECT.collidepoint(pos)):
            if pygame.mouse.get_pressed()[0]==1:
                self.model.option_2 = 3

    def endMenuControll(self,view):
        pos = pygame.mouse.get_pos()
        if (view.image.BUTTON_NO_RECT.collidepoint(pos)):
                if pygame.mouse.get_pressed()[0]==1:
                   self.model.option = 1

        if (view.image.BUTTON_YES_RECT.collidepoint(pos)):
            if pygame.mouse.get_pressed()[0]==1:
                self.model.option = 0