import pygame
from button import Button
from button import *

pygame.init()
pygame.font.init()

#screen
x= 1280
y= 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("interstellar")

#FPS
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

#music
pygame.mixer.music.load("audio/music.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

#background
bg = pygame.image.load("graphics/bg.png").convert()
bg = pygame.transform.scale(bg, (x, y))

#font
font = pygame.font.SysFont("font/Pixeltype.ttf", 50)\

#loading loops
game = True

#----------------------functions----------------------#

#Font for menu
def get_font(size):
    return pygame.font.SysFont("font/Pixeltype.ttf", size)


 # writing on the screen the options      
def write(msg, size, color):
    font = pygame.font.SysFont("font/Pixeltype.ttf", size, True, False)
    message = f'{msg}'
    new_text = font.render(message, True, color)
    return new_text

#used an old code(from my last pygame) and adapt it for the main menu part
def main_menu():
    menu = True
    while menu:
        screen.blit(bg, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("INTERSTELLAR", True, "White")
        MENU_RECT = MENU_TEXT.get_rect(center=(650, 80))
        PLAY_BUTTON = Button(image=None, pos=(640, 250),text_input="PLAY", font=get_font(75), base_color="White", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 350),text_input="OPTIONS", font=get_font(75), base_color="White", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(640, 450),text_input="QUIT", font=get_font(75), base_color="White", hovering_color="Red")
        screen.blit(MENU_TEXT, MENU_RECT)
        Wever = get_font(20).render("Game made by Alexandre Wever and Sergio Ramella", True, "White")
        Wever_rect = Wever.get_rect(center=(1110, 570))
        screen.blit(Wever, Wever_rect)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    menu = False

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
        pygame.display.update()

#used an old code(from my last pygame) and adapt it for the option part
def options():
    option = True
    while option:
        screen.blit(bg, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONPAGE_TEXT = get_font(100).render("OPTIONS", True, "White")
        OPTIONPAGE_RECT = OPTIONPAGE_TEXT.get_rect(center=(640, 80))
        screen.blit(OPTIONPAGE_TEXT, OPTIONPAGE_RECT)
        OPTIONS_TEXT = get_font(45).render("ESCREVER AQUI", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 250))
        OPTIONS_TEXT2 = get_font(45).render("ESCREVER AQUI", True, "White")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 300))
        Wever = get_font(20).render("Game made by Alexandre Wever and Sergio Ramella", True, "White")
        Wever_rect = Wever.get_rect(center=(1110, 570))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        screen.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        screen.blit(Wever, Wever_rect)
        OPTIONS_BACK = Button(image=None, pos=(640, 460),text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    option = False
        pygame.display.update()

#Gameover Screen
def gameover():
    gameover = True
    while gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 

        screen.blit(bg, (0, 0))

        #write on screen
        score_board = write(f'Score: {points}', 50, (255, 255, 255))
        game_over = write('GAME OVER', 100, (225, 225, 225)) 
        end = write('PRESS RETURN TO END GAME', 40, (225, 225, 225))
        screen.blit(game_over, (400, 200))
        screen.blit(score_board, (560, 300))
        screen.blit(end, (400, 450))
        pygame.display.update()

        #if keys pressed return to the main menu    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            gameover = False
            pygame.quit()
            return  
#--------------------------------------------------------------------# 

#----------------------------GAME LOGIC----------------------------#
main_menu()

#while game:




