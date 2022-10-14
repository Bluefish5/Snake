import curses

class Controller():
    def __init__(self,stdscr,model):
        self.model = model
        self.stdscr = stdscr
        self.key = None

    def menuControll(self):
        try:
            key = self.stdscr.getch()
        except:
            key = None

        if key == curses.KEY_UP and self.model.option>=0:
            self.model.option = self.model.option - 1
            if self.model.option == -1:
                self.model.option = 2
        if key == curses.KEY_DOWN and self.model.option <= 2:
            self.model.option = self.model.option + 1
            if self.model.option == 3:
                self.model.option = 0

    def difficultyControll(self):
        try:
            key = self.stdscr.getch()
        except:
            key = None
        if key == curses.KEY_UP and self.model.option_2>=0:
            self.model.option_2 = self.model.option_2 - 1
            if self.model.option_2 == -1:
                self.model.option_2 = 2
        if key == curses.KEY_DOWN and self.model.option_2 <= 3:
            self.model.option_2 = self.model.option_2 + 1
            if self.model.option_2 == 4:
                self.model.option_2 = 0

    def isLeftClicked(self):
        try:
            self.key = self.stdscr.getch()
        except:
            self.key = None

        if self.key == curses.KEY_LEFT:
            return True
        else:
            return False

    def inputDirection(self,lastDirection):
        try:
            self.key = self.stdscr.getch()
        except:
            self.key = None

        if self.key == curses.KEY_DOWN and lastDirection !="N":
            self.model.direction = "S"
        if self.key == curses.KEY_UP and lastDirection !="S":
            self.model.direction = "N"
        if self.key == curses.KEY_LEFT and lastDirection !="E":
            self.model.direction = "W"
        if self.key == curses.KEY_RIGHT and lastDirection !="W":
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