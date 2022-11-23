import time
from curses import wrapper
from Model import*
from Controller import*
from View import*
import pygame


def main():
    run = True
    while run:
        model = Model()
        view = View(model)
        controller = Controller(model)
        while run:
            controller.checkIfClosed()
            view.mainMenu()
            pos = pygame.mouse.get_pos()
            
            if (view.BUTTON_EXIT_RECT.collidepoint(pos)):
                 if pygame.mouse.get_pressed()[0]==1:
                    pygame.quit()

            if (view.BUTTON_START_RECT.collidepoint(pos)):
                if pygame.mouse.get_pressed()[0]==1:
                    break
            
            if (view.BUTTON_DIFFICULTY_RECT.collidepoint(pos)):
                if pygame.mouse.get_pressed()[0]==1:
                    while True:
                        controller.checkIfClosed()
                        view.difficultyMenu()
                        pos = pygame.mouse.get_pos()
                        if (view.BUTTON_EASY_RECT.collidepoint(pos)):
                            if pygame.mouse.get_pressed()[0]==1:
                                model.difficulty = 0
                        if (view.BUTTON_MEDIUM_RECT.collidepoint(pos)):
                            if pygame.mouse.get_pressed()[0]==1:
                                model.difficulty = 1
                        if (view.BUTTON_HARD_RECT.collidepoint(pos)):
                            if pygame.mouse.get_pressed()[0]==1:
                                model.difficulty = 2
                        if (view.BUTTON_BACK_RECT.collidepoint(pos)):
                            if pygame.mouse.get_pressed()[0]==1:
                                break

            if (view.BUTTON_SCORE_RECT.collidepoint(pos)):
                if pygame.mouse.get_pressed()[0]==1:
                    while True:
                        controller.checkIfClosed()
                        view.scoreTable()
                        pos = pygame.mouse.get_pos()
                        if (view.BUTTON_BACK_RECT.collidepoint(pos)):
                            if pygame.mouse.get_pressed()[0]==1:
                                break 

        view.WINDOW.fill((255,255,255))
        pygame.display.update()
        controller.setSpeed()
        model.startTime = time.time()
        model.sample = time.time()

        while run:
            controller.checkIfClosed()
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

        while run:
            pos = pygame.mouse.get_pos()
            controller.checkIfClosed()
            view.endScreen()
            
            if (view.BUTTON_NO_RECT.collidepoint(pos)):
                if pygame.mouse.get_pressed()[0]==1:
                    break

            if (view.BUTTON_YES_RECT.collidepoint(pos)):
                if pygame.mouse.get_pressed()[0]==1:
                    view.insertName()
                    controller.saveScore()
                    break
                

if __name__ == '__main__':
    main()