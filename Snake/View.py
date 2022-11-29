import pygame
import os
from Image import*
class View():
    
    def __init__(self,model):
        self.model = model
        self.image = Image(model)
        self.actualHeadDirection = "E"
        self.mapWitdhStart = (self.image.WIDTH-(self.model.size * 30))/2
        self.mapHeightStart = (self.image.HEIGHT-(self.model.size * 30))/2
        
    def clearView(self):
        pygame.display.update()

    def mainMenu(self,controller):
        self.checkIfClosed()
        self.image.WINDOW.blit(self.image.MAIN_MENU_IMG,(0,0))
        pos = pygame.mouse.get_pos()
        if (self.image.BUTTON_START_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_START_HOVER,(self.image.BUTTON_START_RECT.x,self.image.BUTTON_START_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_START,(self.image.BUTTON_START_RECT.x,self.image.BUTTON_START_RECT.y))
        
        if (self.image.BUTTON_DIFFICULTY_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_DIFFICULTY_HOVER,(self.image.BUTTON_DIFFICULTY_RECT.x,self.image.BUTTON_DIFFICULTY_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_DIFFICULTY,(self.image.BUTTON_DIFFICULTY_RECT.x,self.image.BUTTON_DIFFICULTY_RECT.y))

        if (self.image.BUTTON_SCORE_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_SCORE_HOVER,(self.image.BUTTON_SCORE_RECT.x,self.image.BUTTON_SCORE_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_SCORE,(self.image.BUTTON_SCORE_RECT.x,self.image.BUTTON_SCORE_RECT.y))
        pygame.display.update()

    def endScreen(self):
        self.checkIfClosed()
        self.image.WINDOW.blit(self.image.GAME_OVER,(0,0))
        pos = pygame.mouse.get_pos()
        

        TEXT = self.image.font.render(f"YOUR SCORE IS:{self.model.score*20} AND THE TIME:{round(self.model.scoreBoardTime)}",0,(0,0,0))
        self.image.WINDOW.blit(TEXT,(self.image.HEIGHT*6/10,self.image.HEIGHT/2+2))
        TEXT = self.image.font.render(f"DO YOU WANT TO SAVE YOUR SCORE?:",0,(0,0,0))
        self.image.WINDOW.blit(TEXT,(self.image.HEIGHT*6/10,self.image.HEIGHT/2+30+2))

        TEXT = self.image.font.render(f"YOUR SCORE IS:{self.model.score*20} AND THE TIME:{round(self.model.scoreBoardTime)}",0,(50,50,255))
        self.image.WINDOW.blit(TEXT,(self.image.HEIGHT*6/10+1,self.image.HEIGHT/2+2+1))
        TEXT = self.image.font.render(f"DO YOU WANT TO SAVE YOUR SCORE?:",0,(50,50,255))
        self.image.WINDOW.blit(TEXT,(self.image.HEIGHT*6/10+1,self.image.HEIGHT/2+30+2+1))



        if (self.image.BUTTON_YES_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_YES_HOVER,(self.image.BUTTON_YES_RECT.x,self.image.BUTTON_YES_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_YES,(self.image.BUTTON_YES_RECT.x,self.image.BUTTON_YES_RECT.y))

        if (self.image.BUTTON_NO_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_NO_HOVER,(self.image.BUTTON_NO_RECT.x,self.image.BUTTON_NO_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_NO,(self.image.BUTTON_NO_RECT.x,self.image.BUTTON_NO_RECT.y))

        pygame.display.update()

    def difficultyMenu(self):
        self.checkIfClosed()
        self.image.WINDOW.blit(self.image.MAIN,(0,0))
        pos = pygame.mouse.get_pos()

        if self.model.difficulty == 0:
            self.image.WINDOW.blit(self.image.MENU_DIFFICULTY_EASY,(0,0))
        if self.model.difficulty == 1:
            self.image.WINDOW.blit(self.image.MENU_DIFFICULTY_MEDIUM,(0,0))
        if self.model.difficulty == 2:
            self.image.WINDOW.blit(self.image.MENU_DIFFICULTY_HARD,(0,0))
        
        if (self.image.BUTTON_EASY_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_EASY_HOVER,(self.image.BUTTON_EASY_RECT.x,self.image.BUTTON_EASY_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_EASY,(self.image.BUTTON_EASY_RECT.x,self.image.BUTTON_EASY_RECT.y))
        
        if (self.image.BUTTON_MEDIUM_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_MEDIUM_HOVER,(self.image.BUTTON_MEDIUM_RECT.x,self.image.BUTTON_MEDIUM_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_MEDIUM,(self.image.BUTTON_MEDIUM_RECT.x,self.image.BUTTON_MEDIUM_RECT.y))
        
        if (self.image.BUTTON_HARD_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_HARD_HOVER,(self.image.BUTTON_HARD_RECT.x,self.image.BUTTON_HARD_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_HARD,(self.image.BUTTON_HARD_RECT.x,self.image.BUTTON_HARD_RECT.y))

        if (self.image.BUTTON_BACK_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_BACK_HOVER,(self.image.BUTTON_BACK_RECT.x,self.image.BUTTON_BACK_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_BACK,(self.image.BUTTON_BACK_RECT.x,self.image.BUTTON_BACK_RECT.y))

        

        pygame.display.update()
        

    def legend(self):
        if self.model.difficulty == 0:
            diff = "EASY  "
        if self.model.difficulty == 1:
            diff = "MEDIUM"
        if self.model.difficulty == 2:
            diff = "HARD  "

        TEXT = self.image.font.render(f"Time:{round(self.model.scoreBoardTime)} Score:{self.model.score*20}",0,(0,0,0))
        self.image.WINDOW.blit(TEXT,(self.image.WIDTH*3/4,300))
        
        TEXT = self.image.font.render(f"direction:{self.model.direction}",0,(0,0,0))
        self.image.WINDOW.blit(TEXT,(self.image.WIDTH*3/4,250))
        
        
        TEXT = self.image.font.render(f"difficulty:{diff}",0,(0,0,0))
        self.image.WINDOW.blit(TEXT,(self.image.WIDTH*3/4,200))

        pygame.display.update()
        
        

    def scoreTable(self):
        self.checkIfClosed()
        self.image.WINDOW.blit(self.image.MAIN,(0,0))
        pos = pygame.mouse.get_pos()
        
        
        x = self.model.df.split("\n")
        for i in range(len(x)):
            TEXT = self.image.font.render(x[i],0,(0,0,0))
            self.image.WINDOW.blit(TEXT,(self.image.WIDTH*4/10,i*20+self.image.HEIGHT*1/10))
            TEXT = self.image.font.render(x[i],0,(50,50,255))
            self.image.WINDOW.blit(TEXT,(self.image.WIDTH*4/10+1,i*20+self.image.HEIGHT*1/10+1))

        if (self.image.BUTTON_BACK_RECT.collidepoint(pos)):
            self.image.WINDOW.blit(self.image.BUTTON_BACK_HOVER,(self.image.BUTTON_BACK_RECT.x,self.image.BUTTON_BACK_RECT.y))
        else:
            self.image.WINDOW.blit(self.image.BUTTON_BACK,(self.image.BUTTON_BACK_RECT.x,self.image.BUTTON_BACK_RECT.y))

        pygame.display.update()

    def insertName(self):
        run = True
        while run:
            self.image.WINDOW.blit(self.image.MAIN,(0,0))

            TEXT = self.image.font.render(f"Insert Your Name:",0,(0,0,0))
            self.image.WINDOW.blit(TEXT,(self.image.WIDTH/2-10,self.image.HEIGHT/2-20+2))

            TEXT = self.image.font.render(f"Insert Your Name:",0,(50,50,255))
            self.image.WINDOW.blit(TEXT,(self.image.WIDTH/2-10+1,self.image.HEIGHT/2-20+2+1))

            textSurface = self.image.font.render(self.model.userText,True,(255,255,255))
            self.image.WINDOW.blit(textSurface,(self.image.WIDTH/2-10,self.image.HEIGHT/2))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.model.userText = self.model.userText[:-1]
                    elif event.key == pygame.K_RETURN:
                        run = False
                    else:
                        self.model.userText+= event.unicode
            pygame.display.update()
       
    def updateMap(self):
        self.checkIfClosed()
        pygame.draw.rect(self.image.WINDOW,(255,255,255),(self.image.WIDTH*7/10,self.image.HEIGHT*3/10,250,200))

        if self.model.direction == "N":
            if self.actualHeadDirection == "E":
                self.image.SNAKE_HEAD = pygame.transform.rotate(self.image.SNAKE_HEAD,90)
                self.image.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "N"

            if self.actualHeadDirection == "W":
                self.image.SNAKE_HEAD = pygame.transform.rotate(self.image.SNAKE_HEAD,-90)
                self.image.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "N"

        if self.model.direction == "E":
            if self.actualHeadDirection == "N":
                self.image.SNAKE_HEAD = pygame.transform.rotate(self.image.SNAKE_HEAD,-90)
                self.image.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "E"

            if self.actualHeadDirection == "S":
                self.image.SNAKE_HEAD = pygame.transform.rotate(self.image.SNAKE_HEAD,90)
                self.image.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "E"

        if self.model.direction == "S":
            if self.actualHeadDirection == "W":
                self.image.SNAKE_HEAD = pygame.transform.rotate(self.image.SNAKE_HEAD,90)
                self.image.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "S"

            if self.actualHeadDirection == "E":
                self.image.SNAKE_HEAD = pygame.transform.rotate(self.image.SNAKE_HEAD,-90)
                self.image.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "S"

        if self.model.direction == "W":
            if self.actualHeadDirection == "N":
                self.image.SNAKE_HEAD = pygame.transform.rotate(self.image.SNAKE_HEAD,90)
                self.image.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "W"

            if self.actualHeadDirection == "S":
                self.image.SNAKE_HEAD = pygame.transform.rotate(self.image.SNAKE_HEAD,-90)
                self.image.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "W"
            
        for i in range(self.model.size):
            for j in range(self.model.size):
                if str(self.model.mapa[i][j]) == "@":
                    self.image.WINDOW.blit(self.image.GRASS,(self.mapWitdhStart+i*30,self.mapHeightStart+j*30))
                    self.image.WINDOW.blit(self.image.SNAKE_FOOD,(self.mapWitdhStart+i*30,self.mapHeightStart+j*30))
                elif str(self.model.mapa[i][j]) == "H":
                    self.image.WINDOW.blit(self.image.GRASS,(self.mapWitdhStart+i*30,self.mapHeightStart+j*30))
                    self.image.WINDOW.blit(self.image.SNAKE_HEAD,(self.mapWitdhStart+i*30,self.mapHeightStart+j*30))
                elif str(self.model.mapa[i][j]) == "B":
                    self.image.WINDOW.blit(self.image.GRASS,(self.mapWitdhStart+i*30,self.mapHeightStart+j*30))
                    self.image.WINDOW.blit(self.image.SNAKE_BODY,(self.mapWitdhStart+i*30,self.mapHeightStart+j*30))
                elif str(self.model.mapa[i][j]) == "#":
                    self.image.WINDOW.blit(self.image.WALL,(self.mapWitdhStart+i*30,self.mapHeightStart+j*30))
                else:
                    self.image.WINDOW.blit(self.image.GRASS,(self.mapWitdhStart+i*30,self.mapHeightStart+j*30))
    
    def checkIfClosed(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    def doBackGraound(self):
        self.image.WINDOW.blit(self.image.MAIN,(0,0))