import sys, pygame
import curses
from curses.textpad import Textbox
class View():
    
    def __init__(self,stdscr,model):
        self.stdscr = stdscr
        self.model = model
        pygame.init()

    def mainMenu(self):
        self.start(60,10)
        self.stdscr.addstr(self.model.h//2,self.model.w//2-5,f"START")
        self.stdscr.addstr(self.model.h//2+1,self.model.w//2-5,f"DIFFICULTY")
        self.stdscr.addstr(self.model.h//2+2,self.model.w//2-5,f"SCORES")
        if self.model.option == 0:
            self.stdscr.addstr(self.model.h//2,self.model.w//2,f"<")
            self.stdscr.addstr(self.model.h//2+1,self.model.w//2+5,f" ")
            self.stdscr.addstr(self.model.h//2+2,self.model.w//2+1,f" ")
        if self.model.option == 1:
            self.stdscr.addstr(self.model.h//2,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+1,self.model.w//2+5,f"<")
            self.stdscr.addstr(self.model.h//2+2,self.model.w//2+1,f" ")
        if self.model.option == 2:
            self.stdscr.addstr(self.model.h//2,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+1,self.model.w//2+5,f" ")
            self.stdscr.addstr(self.model.h//2+2,self.model.w//2+1,f"<")
        self.stdscr.refresh()

    def endScreen(self):
        self.end(60,10)
        self.stdscr.addstr(self.model.h//2,self.model.w//2-6,f"YOUR SCORE IS:{self.model.score*20} AND THE TIME:{round(self.model.scoreBoardTime)}")
        self.stdscr.addstr(self.model.h//2+1,self.model.w//2-6,f"DO YOU WANT TO SAVE YOUR SCORE?:")
        self.stdscr.addstr(self.model.h//2+2,self.model.w//2-6,f"YES")
        self.stdscr.addstr(self.model.h//2+3,self.model.w//2-6,f"NO")
        if self.model.option == 0:
                self.stdscr.addstr(self.model.h//2+2,self.model.w//2,f"<")
                self.stdscr.addstr(self.model.h//2+3,self.model.w//2,f" ")
        if self.model.option == 1:            
                self.stdscr.addstr(self.model.h//2+2,self.model.w//2,f" ")
                self.stdscr.addstr(self.model.h//2+3,self.model.w//2,f"<")
        self.stdscr.refresh()


    def start(self,x,y):
        self.stdscr.addstr(y,x,"""
                        _______ __   _ _______ _     _ _______       ______ _______ _______ _______
                        |______ | \  | |_____| |____/  |______      |  ____ |_____| |  |  | |______
                        ______| |  \_| |     | |    \_ |______      |_____| |     | |  |  | |______
        """)
        self.stdscr.refresh()
    def end(self,x,y):
        self.stdscr.addstr(y,x,"""
                             ______ _______ _______ _______       _____  _    _ _______  ______
                            |  ____ |_____| |  |  | |______      |     |  \  /  |______ |_____/
                            |_____| |     | |  |  | |______      |_____|   \/   |______ |    \_
                                                                                                    
    """)

    def difficultyMenu(self):
        if self.model.difficulty == 0:
            diff = "EASY  "
        if self.model.difficulty == 1:
            diff = "MEDIUM"
        if self.model.difficulty == 2:
            diff = "HARD  "
        self.stdscr.addstr(self.model.h//2-2,self.model.w//2-12,f"ACTUAL DIFFICULTY:{diff}")
        self.stdscr.addstr(self.model.h//2,self.model.w//2-6,f"EASY  ")
        self.stdscr.addstr(self.model.h//2+1,self.model.w//2-6,f"MEDIUM")
        self.stdscr.addstr(self.model.h//2+2,self.model.w//2-6,f"HARD  ")
        self.stdscr.addstr(self.model.h//2+4,self.model.w//2-6,f"BACK  ")
        if self.model.option_2 == 0:
            self.stdscr.addstr(self.model.h//2,self.model.w//2,f"<")
            self.stdscr.addstr(self.model.h//2+1,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+2,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+4,self.model.w//2,f" ")
        if self.model.option_2 == 1:
            self.stdscr.addstr(self.model.h//2,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+1,self.model.w//2,f"<")
            self.stdscr.addstr(self.model.h//2+2,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+4,self.model.w//2,f" ")
        if self.model.option_2 == 2:
            self.stdscr.addstr(self.model.h//2,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+1,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+2,self.model.w//2,f"<")
            self.stdscr.addstr(self.model.h//2+4,self.model.w//2,f" ")
        if self.model.option_2 == 3:
            self.stdscr.addstr(self.model.h//2,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+1,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+2,self.model.w//2,f" ")
            self.stdscr.addstr(self.model.h//2+4,self.model.w//2,f"<")
        self.stdscr.refresh()

    def legend(self):
        if self.model.difficulty == 0:
            diff = "EASY  "
        if self.model.difficulty == 1:
            diff = "MEDIUM"
        if self.model.difficulty == 2:
            diff = "HARD  "
        self.stdscr.addstr(21,self.model.w//2-10,f"Time:{round(self.model.scoreBoardTime)} Score:{self.model.score*20}")
        self.stdscr.addstr(20,self.model.w//2-10,f"direction:{self.model.direction}")
        self.stdscr.addstr(22,self.model.w//2-10,f"difficulty:{diff}")
        self.stdscr.refresh()

    def scoreTable(self):
        self.stdscr.addstr(0,0,f"{self.model.df}")
        self.stdscr.addstr(self.model.h//2+2,self.model.w//2-5,f"BACK<")
        self.stdscr.refresh()

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
        for i in range(self.model.size):
            for j in range(self.model.size):
                self.stdscr.addstr(j,i+self.model.w//2-self.model.size//2,str(self.model.mapa[i][j]))
        