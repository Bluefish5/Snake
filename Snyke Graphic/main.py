import curses
import time

from curses import wrapper

from Model import*
from Controller import*
from View import*


def main(stdscr):
    stdscr.nodelay(True)
    curses.curs_set(0)
    while True:
        stdscr.clear()
        model = Model(stdscr)
        view = View(stdscr,model)
        controller = Controller(stdscr,model)
        while True:
            view.mainMenu()
            controller.getUserKeyInput()
            controller.menuControll()

            if controller.isLeftClicked():
                if model.option == 0:
                    break
                if model.option == 1:
                    stdscr.clear()
                    while True:
                        view.difficultyMenu()
                        controller.getUserKeyInput()
                        controller.difficultyControll()
                        if controller.isLeftClicked():
                            if model.option_2 == 3:
                                stdscr.clear()
                                break
                            model.difficulty = model.option_2
                            stdscr.refresh() 

                if  model.option == 2:
                    stdscr.clear()
                    while True:
                        view.scoreTable()
                        controller.getUserKeyInput()
                        if controller.isLeftClicked():
                            stdscr.clear()
                            break  

        stdscr.clear()
        controller.setSpeed()
        model.startTime = time.time()
        model.sample = time.time()

        while True:
            model.new = time.time()
            model.difference = model.new - model.sample
            model.lastDirection = model.direction
            controller.getUserKeyInput()
            controller.inputDirection()
            
            if(model.difference > model.speed):
                model.sample = time.time()
                model.mapa[model.headX][model.headY]=" "
                model.mapa[model.foodX][model.foodY]=" "

                if model.bodyCoordinats!=[]:
                    if not((model.headX == model.foodX) and (model.headY == model.foodY)):
                        helper = model.bodyCoordinats.pop(0)
                        model.mapa[helper[0]][helper[1]]=" "
                    if((model.headX == model.foodX) and (model.headY == model.foodY)):
                        pass
                    else:
                        model.bodyCoordinats.append([model.headX,model.headY])
                    
                if((model.headX == model.foodX) and (model.headY == model.foodY)):
                    controller.findingFoodCoordinats()
                    controller.addPoint()
                    model.bodyCoordinats.append([ model.headX, model.headY])
                    model.snakeLen =  model.snakeLen + 1

                if model.direction == "S" and model.lastDirection !="N":
                    if  model.headY < model.size - 2:
                        model.headY =  model.headY + 1
                        if controller.checkIfHeadHitBody():
                            break
                    else:
                        break
                        
                if  model.direction == "N" and model.lastDirection !="S":
                    if  model.headY >= 2:
                        model.headY =  model.headY - 1
                        if controller.checkIfHeadHitBody():
                            break
                    else:
                        break

                if model.direction == "E" and model.lastDirection !="W":
                    if  model.headX < model.size-2:
                        model.headX = model.headX + 1
                        if controller.checkIfHeadHitBody():
                            break
                    else:
                        break

                if model.direction == "W" and model.lastDirection !="E":
                    if model.headX >= 2:
                        model.headX = model.headX - 1
                        if controller.checkIfHeadHitBody():
                            break
                    else:
                        break
                controller.updateTableMap()
                
            model.scoreBoardTime = time.time() - model.startTime

            view.updateMap()
            view.legend()

        model.option = 0
        stdscr.clear()
        while True:
            view.endScreen()
            controller.getUserKeyInput()
            controller.endMenuControll()

            if controller.isLeftClicked():
                if model.option == 1:
                    break
                if model.option == 0:
                    stdscr.clear()
                    view.insertNameText()
                    view.insertNameBox()
                    controller.saveScore()
                    break
                

if __name__ == '__main__':
    #os.system("start cmd /k python main.py")
    wrapper(main)