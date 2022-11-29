import curses
from curses.textpad import Textbox
class View_Text():
    
    def __init__(self,stdscr,model):
        stdscr.nodelay(True)
        curses.curs_set(0)
        stdscr.clear()
        self.stdscr = stdscr
        self.model = model
        
        curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
        curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
        curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_BLACK)
        curses.init_pair(4,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
        curses.init_pair(5,curses.COLOR_CYAN,curses.COLOR_BLACK)
        curses.init_pair(6,curses.COLOR_RED,curses.COLOR_RED)
        curses.init_pair(7,curses.COLOR_MAGENTA,curses.COLOR_MAGENTA)
        curses.init_pair(8,curses.COLOR_CYAN,curses.COLOR_CYAN)
        curses.init_pair(9,curses.COLOR_RED,curses.COLOR_CYAN)

        self.GREEN=curses.color_pair(1)
        self.RED=curses.color_pair(2)
        self.YELLOW=curses.color_pair(3)
        self.MAGENTA=curses.color_pair(4)
        self.CYAN=curses.color_pair(5)
        self.BODY_COLOR=curses.color_pair(6)
        self.WALL_MAGENTA=curses.color_pair(7)
        self.WALL_CYAN=curses.color_pair(8)
        self.FOOD=curses.color_pair(9)


    def mainMenu(self,controller):
        
        self.start(60,10)
        self.stdscr.addstr(self.model.h//2,self.model.w//2-5,f"START",self.YELLOW)
        self.stdscr.addstr(self.model.h//2+1,self.model.w//2-5,f"DIFFICULTY",self.MAGENTA)
        self.stdscr.addstr(self.model.h//2+2,self.model.w//2-5,f"SCORES",self.RED)
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
        self.stdscr.addstr(self.model.h//2,self.model.w//2-6,f"YOUR SCORE IS:{self.model.score*20} AND THE TIME:{round(self.model.scoreBoardTime)}",self.MAGENTA)
        self.stdscr.addstr(self.model.h//2+1,self.model.w//2-6,f"DO YOU WANT TO SAVE YOUR SCORE?:",self.YELLOW)
        self.stdscr.addstr(self.model.h//2+2,self.model.w//2-6,f"YES",self.GREEN)
        self.stdscr.addstr(self.model.h//2+3,self.model.w//2-6,f"NO",self.RED)
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
        """,self.GREEN)
        self.stdscr.refresh()
    def end(self,x,y):
        self.stdscr.addstr(y,x,"""
                             ______ _______ _______ _______       _____  _    _ _______  ______
                            |  ____ |_____| |  |  | |______      |     |  \  /  |______ |_____/
                            |_____| |     | |  |  | |______      |_____|   \/   |______ |    \_
                                                                                                    
    """,self.CYAN)

    def difficultyMenu(self):
        
        if self.model.difficulty == 0:
            diff = "EASY  "
        if self.model.difficulty == 1:
            diff = "MEDIUM"
        if self.model.difficulty == 2:
            diff = "HARD  "
        self.stdscr.addstr(self.model.h//2-2,self.model.w//2-12,f"ACTUAL DIFFICULTY:{diff}",self.MAGENTA)
        self.stdscr.addstr(self.model.h//2,self.model.w//2-6,f"EASY  ",self.GREEN)
        self.stdscr.addstr(self.model.h//2+1,self.model.w//2-6,f"MEDIUM",self.YELLOW)
        self.stdscr.addstr(self.model.h//2+2,self.model.w//2-6,f"HARD  ",self.RED)
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
        self.stdscr.addstr(21,80,f"Time:{round(self.model.scoreBoardTime)} Score:{self.model.score*20}",self.YELLOW)
        self.stdscr.addstr(20,80,f"direction:{self.model.direction}",self.CYAN)
        self.stdscr.addstr(22,80,f"difficulty:{diff}", self.MAGENTA)
        self.stdscr.refresh()

    def scoreTable(self):
        self.stdscr.addstr(0,0,f"{self.model.df}",self.MAGENTA)
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

                if str(self.model.mapa[i][j]) == "@":
                    self.stdscr.addstr(j,i+self.model.w//2-self.model.size//2,str(self.model.mapa[i][j]),self.FOOD)
                elif str(self.model.mapa[i][j]) == "H":
                    self.stdscr.addstr(j,i+self.model.w//2-self.model.size//2,str(self.model.mapa[i][j]),self.BODY_COLOR)  
                elif str(self.model.mapa[i][j]) == "B":
                    self.stdscr.addstr(j,i+self.model.w//2-self.model.size//2,str(self.model.mapa[i][j]),self.BODY_COLOR)
                elif str(self.model.mapa[i][j]) == "#":
                    self.stdscr.addstr(j,i+self.model.w//2-self.model.size//2,str(self.model.mapa[i][j]),self.WALL_MAGENTA)     
                else:
                    self.stdscr.addstr(j,i+self.model.w//2-self.model.size//2,str(self.model.mapa[i][j]),self.WALL_CYAN)
    def insertName(self):
        
        curses.flushinp()
        self.insertNameText()
        self.insertNameBox()

    def clearView(self):
        self.stdscr.clear()
    def doBackGraound(self):
        pass

        
        