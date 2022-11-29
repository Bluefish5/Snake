import time
from curses import wrapper
from Model import*
from Controller import*
from View import*
from View_Text import *
from Controller_Text import *


def main(stdscr):
    run = True
    while run:
        if stdscr == "GRAPHIC":
            model = Model(stdscr,15)
            view = View(model)
            controller = Controller(model)
        else:
            model = Model(stdscr,30)
            view = View_Text(stdscr,model)
            controller = Controller_Text(stdscr,model)

        view.clearView()
        while run:
            view.mainMenu(controller)
            controller.menuControll(view)
            if controller.isSubmitClicked():
                if model.option == 0:
                        view.clearView()
                        break
                if model.option == 1:
                    view.clearView()
                    while run:
                        view.difficultyMenu()
                        controller.difficultyControll(view)
                        if controller.isSubmitClicked():
                            if model.option_2 == 3:
                                view.clearView()
                                break
                            model.difficulty = model.option_2
                if  model.option == 2:
                    view.clearView()
                    while True:
                        view.scoreTable()
                        if controller.isSubmitClicked():
                            view.clearView()
                            break
                
        controller.setSpeed()
        model.startTime = time.time()
        model.sample = time.time()
        view.clearView()
        view.doBackGraound()
        while run:
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

        view.clearView()
        while run:
            view.endScreen()
            controller.endMenuControll(view)
            if controller.isSubmitClicked():
                if model.option == 1:
                    time.sleep(0.5)
                    break
                    
                if model.option == 0:
                    view.clearView()
                    view.insertName()
                    time.sleep(0.5)
                    controller.saveScore()
                    break
            
                

if __name__ == '__main__':
    os.system('cls')
    print("Jeżeli chcesz włączyć Snake Graphic wpisz: 0,\njeżeli chcesz włączyć Snake Text wpisz: 1.\n")
    x = int(input("co chcesz wybrać:"))
    if x:
        wrapper(main)           
    else:
        main("GRAPHIC")
        