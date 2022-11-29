import pygame
import os
class Image():

    def __init__(self,model):
        self.model = model
        pygame.font.init()

        self.WIDTH = 1920/2
        self.HEIGHT = 1080/2

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

        ################################-END OF JOINING IMGS-#################################


        ################################-START PLACNIG RECTS-#################################

        self.BUTTON_YES_RECT = self.BUTTON_YES.get_rect()
        self.BUTTON_YES_RECT.topleft = (self.WIDTH*6/10,self.HEIGHT*8/10)

        self.BUTTON_NO_RECT = self.BUTTON_NO.get_rect()
        self.BUTTON_NO_RECT.topleft = (self.WIDTH*4/10,self.HEIGHT*8/10)


        self.BUTTON_EXIT_RECT = self.BUTTON_EXIT.get_rect()
        self.BUTTON_EXIT_RECT.topleft = (self.WIDTH*11/12-self.BUTTON_EXIT_RECT.w/2,self.HEIGHT*11/12-self.BUTTON_EXIT_RECT.h/2)

        self.BUTTON_START_RECT = self.BUTTON_START.get_rect()
        self.BUTTON_START_RECT.topleft = (self.WIDTH/2-self.BUTTON_START_RECT.w/2,self.HEIGHT*5/10)

        self.BUTTON_DIFFICULTY_RECT = self.BUTTON_DIFFICULTY.get_rect()
        self.BUTTON_DIFFICULTY_RECT.topleft = (self.WIDTH/2-self.BUTTON_DIFFICULTY_RECT.w/2,self.HEIGHT*6/10)

        self.BUTTON_SCORE_RECT = self.BUTTON_SCORE.get_rect()
        self.BUTTON_SCORE_RECT.topleft = (self.WIDTH/2-self.BUTTON_SCORE_RECT.w/2,self.HEIGHT*7/10)

        self.BUTTON_BACK_RECT = self.BUTTON_BACK.get_rect()
        self.BUTTON_BACK_RECT.topleft = (self.WIDTH/2-self.BUTTON_BACK_RECT.w/2,self.HEIGHT*8/10)

        ################# DIFICULTYS BUTTONS ####################################

        self.BUTTON_EASY_RECT = self.BUTTON_EASY.get_rect()
        self.BUTTON_EASY_RECT.topleft = (self.WIDTH*1/5+self.BUTTON_EASY_RECT.w/2,self.HEIGHT/2)

        self.BUTTON_MEDIUM_RECT = self.BUTTON_MEDIUM.get_rect()
        self.BUTTON_MEDIUM_RECT.topleft = (self.WIDTH*2/5+self.BUTTON_MEDIUM_RECT.w/2,self.HEIGHT/2)

        self.BUTTON_HARD_RECT = self.BUTTON_HARD.get_rect()
        self.BUTTON_HARD_RECT.topleft = (self.WIDTH*3/5+self.BUTTON_HARD_RECT.w/2,self.HEIGHT/2)

        ############################################################################

        self.SNAKE_HEAD = pygame.transform.rotate(self.SNAKE_HEAD,90)
        self.SNAKE_HEAD.set_colorkey((255,255,255))

        self.font = pygame.font.SysFont("Consolas",20)
        

        self.WINDOW = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption("Snake Game!")
    