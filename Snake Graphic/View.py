import curses
from curses.textpad import Textbox
import pygame
import os
class View():
    
    def __init__(self,model):
        pygame.font.init()
        self.model = model
        
        self.WIDTH = 1920/2
        self.HEIGHT = 1080/2

        self.font = pygame.font.SysFont("GOST Common",20)

        self.WINDOW = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("Snake Game!")

        self.GRASS = pygame.image.load(os.path.join('img','grass.png'))

        self.MENU_DIFFICULTY_EASY = pygame.image.load(os.path.join('img','menu_difficulty_easy.png'))
        self.MENU_DIFFICULTY_EASY = pygame.transform.scale(self.MENU_DIFFICULTY_EASY,(self.WIDTH,self.HEIGHT))

        self.MENU_DIFFICULTY_MEDIUM = pygame.image.load(os.path.join('img','menu_difficulty_medium.png'))
        self.MENU_DIFFICULTY_MEDIUM = pygame.transform.scale(self.MENU_DIFFICULTY_MEDIUM,(self.WIDTH,self.HEIGHT))

        self.MENU_DIFFICULTY_HARD = pygame.image.load(os.path.join('img','menu_difficulty_hard.png'))
        self.MENU_DIFFICULTY_HARD = pygame.transform.scale(self.MENU_DIFFICULTY_HARD,(self.WIDTH,self.HEIGHT))

        self.MAIN_MENU_IMG = pygame.image.load(os.path.join('img','main_menu.png'))
        self.MAIN_MENU_IMG = pygame.transform.scale(self.MAIN_MENU_IMG,(self.WIDTH,self.HEIGHT))

        self.MAIN_SCORE = pygame.image.load(os.path.join("img","main_score.png"))
        self.MAIN_SCORE = pygame.transform.scale(self.MAIN_SCORE,(self.WIDTH,self.HEIGHT))

        self.GAME_OVER = pygame.image.load(os.path.join("img","game_over.png"))
        self.GAME_OVER = pygame.transform.scale(self.GAME_OVER,(self.WIDTH,self.HEIGHT))

        self.MAIN = pygame.image.load(os.path.join("img","main.png"))
        self.MAIN = pygame.transform.scale(self.MAIN,(self.WIDTH,self.HEIGHT))

        self.BUTTON_YES = pygame.image.load(os.path.join('img','button_yes.png'))
        self.BUTTON_YES.set_colorkey((255,255,255))

        self.BUTTON_YES_HOVER = pygame.image.load(os.path.join('img','button_yes_hover.png'))
        self.BUTTON_YES_HOVER.set_colorkey((255,255,255))

        self.BUTTON_NO = pygame.image.load(os.path.join('img','button_no.png'))
        self.BUTTON_NO.set_colorkey((255,255,255))

        self.BUTTON_NO_HOVER = pygame.image.load(os.path.join('img','button_no_hover.png'))
        self.BUTTON_NO_HOVER.set_colorkey((255,255,255))

        self.BUTTON_EXIT = pygame.image.load(os.path.join('img','button_exit.png'))
        self.BUTTON_EXIT.set_colorkey((255,255,255))

        self.BUTTON_EXIT_HOVER = pygame.image.load(os.path.join('img','button_exit_hover.png'))
        self.BUTTON_EXIT_HOVER.set_colorkey((255,255,255))

        self.BUTTON_START = pygame.image.load(os.path.join('img','button_start.png'))
        self.BUTTON_START.set_colorkey((255,255,255))

        self.BUTTON_START_HOVER = pygame.image.load(os.path.join('img','button_start_hover.png'))
        self.BUTTON_START_HOVER.set_colorkey((255,255,255))

        self.BUTTON_SCORE = pygame.image.load(os.path.join('img','button_score.png'))
        self.BUTTON_SCORE.set_colorkey((255,255,255))

        self.BUTTON_SCORE_HOVER = pygame.image.load(os.path.join('img','button_score_hover.png'))
        self.BUTTON_SCORE_HOVER.set_colorkey((255,255,255))

        self.BUTTON_DIFFICULTY = pygame.image.load(os.path.join('img','button_difficulty.png'))
        self.BUTTON_DIFFICULTY.set_colorkey((255,255,255))

        self.BUTTON_DIFFICULTY_HOVER = pygame.image.load(os.path.join('img','button_difficulty_hover.png'))
        self.BUTTON_DIFFICULTY_HOVER.set_colorkey((255,255,255))

        self.BUTTON_EASY = pygame.image.load(os.path.join('img','button_easy.png'))
        self.BUTTON_EASY.set_colorkey((255,255,255))

        self.BUTTON_EASY_HOVER = pygame.image.load(os.path.join('img','button_easy_hover.png'))
        self.BUTTON_EASY_HOVER.set_colorkey((255,255,255))

        self.BUTTON_MEDIUM = pygame.image.load(os.path.join('img','button_medium.png'))
        self.BUTTON_MEDIUM.set_colorkey((255,255,255))

        self.BUTTON_MEDIUM_HOVER = pygame.image.load(os.path.join('img','button_medium_hover.png'))
        self.BUTTON_MEDIUM_HOVER.set_colorkey((255,255,255))

        self.BUTTON_HARD = pygame.image.load(os.path.join('img','button_hard.png'))
        self.BUTTON_HARD.set_colorkey((255,255,255))

        self.BUTTON_HARD_HOVER = pygame.image.load(os.path.join('img','button_hard_hover.png'))
        self.BUTTON_HARD_HOVER.set_colorkey((255,255,255))

        self.BUTTON_BACK = pygame.image.load(os.path.join('img','button_back.png'))
        self.BUTTON_BACK.set_colorkey((255,255,255))

        self.BUTTON_BACK_HOVER = pygame.image.load(os.path.join('img','button_back_hover.png'))
        self.BUTTON_BACK_HOVER.set_colorkey((255,255,255))

        self.WALL = pygame.image.load(os.path.join('img','wall.png'))
        self.WALL = pygame.transform.scale(self.WALL,(30,30))
        self.WALL.set_colorkey((255,255,255))

        self.SNAKE_HEAD = pygame.image.load(os.path.join('img','snake_head.png'))
        self.SNAKE_HEAD = pygame.transform.scale(self.SNAKE_HEAD,(30,30))
        self.SNAKE_HEAD.set_colorkey((255,255,255))

        self.SNAKE_FOOD = pygame.image.load(os.path.join('img','snake_food.png'))
        self.SNAKE_FOOD = pygame.transform.scale(self.SNAKE_FOOD,(30,30))
        self.SNAKE_FOOD.set_colorkey((255,255,255))

        self.SNAKE_BODY = pygame.image.load(os.path.join('img','snake_body.png'))
        self.SNAKE_BODY = pygame.transform.scale(self.SNAKE_BODY,(30,30))
        self.SNAKE_BODY.set_colorkey((255,255,255))

        self.BUTTON_YES_RECT = self.BUTTON_YES.get_rect()
        self.BUTTON_YES_RECT.topleft = (self.WIDTH/2,self.HEIGHT/2)

        self.BUTTON_NO_RECT = self.BUTTON_NO.get_rect()
        self.BUTTON_NO_RECT.topleft = (self.WIDTH/2+150,self.HEIGHT/2)


        self.BUTTON_EXIT_RECT = self.BUTTON_EXIT.get_rect()
        self.BUTTON_EXIT_RECT.topleft = (self.WIDTH/2,self.HEIGHT-50)

        self.BUTTON_START_RECT = self.BUTTON_START.get_rect()
        self.BUTTON_START_RECT.topleft = (self.WIDTH/2,250)

        self.BUTTON_DIFFICULTY_RECT = self.BUTTON_DIFFICULTY.get_rect()
        self.BUTTON_DIFFICULTY_RECT.topleft = (self.WIDTH/2,320)

        self.BUTTON_SCORE_RECT = self.BUTTON_SCORE.get_rect()
        self.BUTTON_SCORE_RECT.topleft = (self.WIDTH/2,390)

        self.BUTTON_EASY_RECT = self.BUTTON_EASY.get_rect()
        self.BUTTON_EASY_RECT.topleft = (self.WIDTH/2-250,self.HEIGHT/2)

        self.BUTTON_MEDIUM_RECT = self.BUTTON_MEDIUM.get_rect()
        self.BUTTON_MEDIUM_RECT.topleft = (self.WIDTH/2,self.HEIGHT/2)

        self.BUTTON_HARD_RECT = self.BUTTON_HARD.get_rect()
        self.BUTTON_HARD_RECT.topleft = (self.WIDTH/2+200,self.HEIGHT/2)

        self.BUTTON_BACK_RECT = self.BUTTON_BACK.get_rect()
        self.BUTTON_BACK_RECT.topleft = (self.WIDTH/6,410)

        self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,90)
        self.SNAKE_HEAD.set_colorkey((255,255,255))
        self.actualHeadDirection = "E"

    def mainMenu(self):
        self.WINDOW.blit(self.MAIN_MENU_IMG,(0,0))
        pos = pygame.mouse.get_pos()
        if (self.BUTTON_START_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_START_HOVER,(self.BUTTON_START_RECT.x,self.BUTTON_START_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_START,(self.BUTTON_START_RECT.x,self.BUTTON_START_RECT.y))
        
        if (self.BUTTON_DIFFICULTY_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_DIFFICULTY_HOVER,(self.BUTTON_DIFFICULTY_RECT.x,self.BUTTON_DIFFICULTY_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_DIFFICULTY,(self.BUTTON_DIFFICULTY_RECT.x,self.BUTTON_DIFFICULTY_RECT.y))

        if (self.BUTTON_SCORE_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_SCORE_HOVER,(self.BUTTON_SCORE_RECT.x,self.BUTTON_SCORE_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_SCORE,(self.BUTTON_SCORE_RECT.x,self.BUTTON_SCORE_RECT.y))
        
        if (self.BUTTON_EXIT_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_EXIT_HOVER,(self.BUTTON_EXIT_RECT.x,self.BUTTON_EXIT_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_EXIT,(self.BUTTON_EXIT_RECT.x,self.BUTTON_EXIT_RECT.y))
        pygame.display.update()

    def endScreen(self):
        self.WINDOW.blit(self.GAME_OVER,(0,0))
        pos = pygame.mouse.get_pos()
        
        TEXT = self.font.render(f"YOUR SCORE IS:{self.model.score*20} AND THE TIME:{round(self.model.scoreBoardTime)}",0,(0,0,0))
        self.WINDOW.blit(TEXT,(100,self.HEIGHT/2))
        TEXT = self.font.render(f"DO YOU WANT TO SAVE YOUR SCORE?:",0,(0,0,0))
        self.WINDOW.blit(TEXT,(100,self.HEIGHT/2+30))

        if (self.BUTTON_YES_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_YES_HOVER,(self.BUTTON_YES_RECT.x,self.BUTTON_YES_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_YES,(self.BUTTON_YES_RECT.x,self.BUTTON_YES_RECT.y))

        if (self.BUTTON_NO_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_NO_HOVER,(self.BUTTON_NO_RECT.x,self.BUTTON_NO_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_NO,(self.BUTTON_NO_RECT.x,self.BUTTON_NO_RECT.y))

        pygame.display.update()

    def difficultyMenu(self):
        self.WINDOW.blit(self.MAIN,(0,0))
        pos = pygame.mouse.get_pos()

        if self.model.difficulty == 0:
            self.WINDOW.blit(self.MENU_DIFFICULTY_EASY,(0,0))
        if self.model.difficulty == 1:
            self.WINDOW.blit(self.MENU_DIFFICULTY_MEDIUM,(0,0))
        if self.model.difficulty == 2:
            self.WINDOW.blit(self.MENU_DIFFICULTY_HARD,(0,0))
        
        if (self.BUTTON_EASY_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_EASY_HOVER,(self.BUTTON_EASY_RECT.x,self.BUTTON_EASY_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_EASY,(self.BUTTON_EASY_RECT.x,self.BUTTON_EASY_RECT.y))
        
        if (self.BUTTON_MEDIUM_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_MEDIUM_HOVER,(self.BUTTON_MEDIUM_RECT.x,self.BUTTON_MEDIUM_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_MEDIUM,(self.BUTTON_MEDIUM_RECT.x,self.BUTTON_MEDIUM_RECT.y))
        
        if (self.BUTTON_HARD_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_HARD_HOVER,(self.BUTTON_HARD_RECT.x,self.BUTTON_HARD_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_HARD,(self.BUTTON_HARD_RECT.x,self.BUTTON_HARD_RECT.y))

        if (self.BUTTON_BACK_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_BACK_HOVER,(self.BUTTON_BACK_RECT.x,self.BUTTON_BACK_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_BACK,(self.BUTTON_BACK_RECT.x,self.BUTTON_BACK_RECT.y))

        

        pygame.display.update()
        

    def legend(self):
        if self.model.difficulty == 0:
            diff = "EASY  "
        if self.model.difficulty == 1:
            diff = "MEDIUM"
        if self.model.difficulty == 2:
            diff = "HARD  "

        TEXT = self.font.render(f"Time:{round(self.model.scoreBoardTime)} Score:{self.model.score*20}",0,(0,0,0))
        self.WINDOW.blit(TEXT,(400,300))
        
        TEXT = self.font.render(f"direction:{self.model.direction}",0,(0,0,0))
        self.WINDOW.blit(TEXT,(400,250))
        
        
        TEXT = self.font.render(f"difficulty:{diff}",0,(0,0,0))
        self.WINDOW.blit(TEXT,(400,200))
        
        

    def scoreTable(self):
        self.WINDOW.blit(self.MAIN_SCORE,(0,0))
        pos = pygame.mouse.get_pos()
        
        font = pygame.font.SysFont("GOST Common",20)
        x = self.model.df.split("\n")
        for i in range(len(x)):
            if i == 0:
                continue
            TEXT = font.render(x[i],0,(0,0,0))
            self.WINDOW.blit(TEXT,(self.WIDTH/2-100,100+i*20))

        if (self.BUTTON_BACK_RECT.collidepoint(pos)):
            self.WINDOW.blit(self.BUTTON_BACK_HOVER,(self.BUTTON_BACK_RECT.x,self.BUTTON_BACK_RECT.y))
        else:
            self.WINDOW.blit(self.BUTTON_BACK,(self.BUTTON_BACK_RECT.x,self.BUTTON_BACK_RECT.y))

        pygame.display.update()

    def insertNameText(self):
        self.stdscr.addstr(self.model.h//2,self.model.w//2,f"INSERT YOUR NAME:")
        self.stdscr.refresh()

    def insertNameBox(self):
        editwin = curses.newwin(1,16, self.model.h//2+1,self.model.w//2)
        box = Textbox(editwin)
        box.edit()
        self.model.tab = box.gather()
        self.stdscr.refresh()
        
    def updateMap(self):
        self.WINDOW.blit(self.MAIN,(0,0))

        if self.model.direction == "N":
            if self.actualHeadDirection == "E":
                self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,90)
                self.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "N"

            if self.actualHeadDirection == "W":
                self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,-90)
                self.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "N"

        if self.model.direction == "E":
            if self.actualHeadDirection == "N":
                self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,-90)
                self.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "E"

            if self.actualHeadDirection == "S":
                self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,90)
                self.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "E"

        if self.model.direction == "S":
            if self.actualHeadDirection == "W":
                self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,90)
                self.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "S"

            if self.actualHeadDirection == "E":
                self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,-90)
                self.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "S"

        if self.model.direction == "W":
            if self.actualHeadDirection == "N":
                self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,90)
                self.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "W"

            if self.actualHeadDirection == "S":
                self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,-90)
                self.SNAKE_HEAD.set_colorkey((255,255,255))
                self.actualHeadDirection = "W"
            
        for i in range(self.model.size):
            for j in range(self.model.size):
                if str(self.model.mapa[i][j]) == "@":
                    self.WINDOW.blit(self.GRASS,(200+i*30,j*30))
                    self.WINDOW.blit(self.SNAKE_FOOD,(200+i*30,j*30))
                elif str(self.model.mapa[i][j]) == "H":
                    self.WINDOW.blit(self.GRASS,(200+i*30,j*30))
                    self.WINDOW.blit(self.SNAKE_HEAD,(200+i*30,j*30))
                elif str(self.model.mapa[i][j]) == "B":
                    self.WINDOW.blit(self.GRASS,(200+i*30,j*30))
                    self.WINDOW.blit(self.SNAKE_BODY,(200+i*30,j*30))
                elif str(self.model.mapa[i][j]) == "#":
                    self.WINDOW.blit(self.WALL,(200+i*30,j*30))
                else:
                    self.WINDOW.blit(self.GRASS,(200+i*30,j*30))
        pygame.display.update()