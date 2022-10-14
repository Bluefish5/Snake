class View():
    
    def __init__(self,stdscr,model):
        self.model = model
        self.stdscr = stdscr
        self.model.h,self.w = stdscr.getmaxyx()

    def mainMenu(self):
        self.start(60,10)
        self.stdscr.addstr(self.model.h//2,self.w//2-5,f"START")
        self.stdscr.addstr(self.model.h//2+1,self.w//2-5,f"DIFFICULTY")
        self.stdscr.addstr(self.model.h//2+2,self.w//2-5,f"SCORES")
        self.stdscr.refresh()

    def endScreen(self):
        self.stdscr.addstr(self.model.h//2,self.model.w//2-6,f"YOUR SCORE IS:{self.model.score*20} AND THE TIME:{round(self.model.time)}")
        self.stdscr.addstr(self.model.h//2+1,self.model.w//2-6,f"DO YOU WANT TO SAVE YOUR SCORE?:")
        self.stdscr.addstr(self.model.h//2+2,self.model.w//2-6,f"YES")
        self.stdscr.addstr(self.model.h//2+3,self.model.w//2-6,f"NO")
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

    def difficultyMenu(self,difficulty):
        self.stdscr.clear()
        self.stdscr.addstr(self.model.h//2-2,self.w//2-12,f"ACTUAL DIFFICULTY:{self.model.whatIsDifficulty(difficulty)}")
        self.stdscr.addstr(self.model.h//2,self.w//2-6,f"EASY")
        self.stdscr.addstr(self.model.h//2+1,self.w//2-6,f"MEDIUM")
        self.stdscr.addstr(self.model.h//2+2,self.w//2-6,f"HARD")
        self.stdscr.addstr(self.model.h//2+4,self.w//2-6,f"BACK")
        self.stdscr.refresh()

    def legend(self,score,scoreBoardTime,difficulty,direction):
        self.stdscr.addstr(21,self.w//2-10,f"Time:{round(scoreBoardTime)} Score:{score*20}")
        self.stdscr.addstr(20,self.w//2-10,f"direction:{direction}")
        self.stdscr.addstr(22,self.w//2-10,f"difficulty:{self.model.whatIsDifficulty(difficulty)}")
        self.stdscr.refresh()

    def scoreTable(self):
        self.stdscr.addstr(0,0,f"{self.model.df}")
        self.stdscr.addstr(self.model.h//2+2,self.w//2-5,f"BACK<")
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

    def arrowsEndMenu(self,):
        if self.model.option == 0:
                self.stdscr.addstr(self.model.h//2+2,self.model.w//2,f"<")
                self.stdscr.addstr(self.model.h//2+3,self.model.w//2,f" ")
                self.stdscr.refresh()
        if self.model.option == 1:            
                self.stdscr.addstr(self.model.h//2+2,self.model.w//2,f" ")
                self.stdscr.addstr(self.model.h//2+3,self.model.w//2,f"<")
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
    