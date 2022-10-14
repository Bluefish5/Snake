import curses
import time
import random

from curses import wrapper
from curses.textpad import Textbox

from Model import*
from Controller import*
from View import*


def main(stdscr):
    stdscr.nodelay(True)
    curses.curs_set(0)

    model = Model(stdscr)
    view = View(stdscr,model)
    controller = Controller(stdscr,model)
    sample = time.time()

    while True:

        controller.menuControll()

        if controller.isLeftClicked() and model.option == 0:
            break

        if controller.isLeftClicked() and model.option == 1:
            view.difficultyMenu(difficulty)
            while True:
                controller.difficultyControll()
                view.arrowsDifficultyMenu(model.option_2)
                if controller.isLeftClicked() and model.option_2 == 3:
                    stdscr.clear()
                    break
                if controller.isLeftClicked():
                    stdscr.clear()
                    difficulty = model.option_2

        if controller.isLeftClicked() and model.option == 2:
            stdscr.clear()
            while True:
                view.scoreTable()
                if controller.isLeftClicked():
                    stdscr.clear()
                    break
                
        view.mainMenu()
        view.arrowsMainMenu(model.option)
    stdscr.clear()

    controller.setSpeed()
    
    while True:
        new = time.time()
        difference = new - sample
        lastDirection = direction

        x = controller.inputDirection(lastDirection)
        if x != None:
            direction = x
        
        if(difference > model.speed):
            sample = time.time()
            model.mapa[model.headX][model.headY]=" "
            model.mapa[foodX][foodY]=" "

            if model.bodyCoordinats!=[]:
                if not((model.headX == foodX) and (model.headY == foodY)):
                    helper = model.bodyCoordinats.pop(0)
                    model.mapa[helper[0]][helper[1]]=" "
                if((model.headX == foodX) and (model.headY == foodY)):
                    pass
                else:
                    model.bodyCoordinats.append([model.headX,model.headY])
                

            if((headX == foodX) and (model.headY == foodY)):
                while findingFoodCoordinats:
                    foodX = random.randint(1, model.size-2)
                    foodY = random.randint(1, model.size-2)
                    if [foodX,foodY] not in model.bodyCoordinats:
                        findingFoodCoordinats = False
                findingFoodCoordinats = True

                controller.addPoint()
                    
                model.bodyCoordinats.append([ model.headX, model.headY])
                
                model.snakeLen =  model.snakeLen + 1

            if direction == "S" and lastDirection !="N":
                if  model.headY < model.size - 2:
                    model.headY =  model.headY + 1
                    if [model.headX, model.headY] in model.bodyCoordinats:
                        break
                else:
                    break
                    
            if  model.direction == "N" and lastDirection !="S":
                if  model.headY >= 2:
                    model.headY =  model.headY - 1
                    if [model.headX, model.headY] in model.bodyCoordinats:
                        break
                else:
                    break

            if direction == "E" and lastDirection !="W":
                if  model.headX < model.size-2:
                    model.headX = headX + 1
                    if [ model.headX, model.headY] in model.bodyCoordinats:
                        break
                else:
                    break

            if direction == "W" and lastDirection !="E":
                if headX >= 2:
                    headX = headX - 1
                    if [model.headX,model.headY] in model.bodyCoordinats:
                        break
                else:
                    break
            
            model.mapa[model.foodX][foodY]="F"
            for i in model.bodyCoordinats:
                model.mapa[i[0]][i[1]]="B"
            model.mapa[model.headX][model.headY]="H"
            
        for i in range(model.size):
                for j in range(model.size):
                    stdscr.addstr(j,i+model.w//2-model.size//2,str(model.mapa[i][j]))
        scoreBoardTime = time.time() - model.startTime
        view.legend(model.score,scoreBoardTime,difficulty,direction)

    
    model.option = 0
    stdscr.clear()
    while True:
        try:
            key = stdscr.getch()
        except:
            key = None
        
        view.endScreen()
        
        if key == curses.KEY_UP and model.option>=0:
            model.option = model.option - 1
            if model.option == -1:
                model.option = 1
        if key == curses.KEY_DOWN and model.option <= 1:
            model.option = model.option + 1
            if model.option == 2:
                model.option = 0

        view.arrowsEndMenu()

        if key == curses.KEY_LEFT and model.option == 1:
            exit()
        if key == curses.KEY_LEFT and model.option == 0:
            stdscr.clear()

            editwin = curses.newwin(1,16, model.h//2+1,model.w//2)
            stdscr.addstr(model.h//2,model.w//2,f"INSERT YOUR NAME:")
            stdscr.refresh()
            box = Textbox(editwin)
            box.edit()
            model.tab = box.gather()

            file = open("Scores.csv","a")
            file.write(f"\n{model.tab},{model.score*20},{round(time)}")
            file.close()
            stdscr.refresh()
            exit()

if __name__ == '__main__':
    wrapper(main)