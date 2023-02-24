import pygame
from button import Button
from button import *
import random
import math
import numpy as np

pygame.init()
pygame.font.init()

#screen
screen_width = 1280
screen_height= 600
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("interstellar")

#FPS
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

#music
pygame.mixer.music.load("audio/music.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

#background
background = pygame.image.load("graphics/bg.png").convert()
background = pygame.transform.scale(background, (screen_width , screen_height))

#font
font = pygame.font.SysFont("font/Pixeltype.ttf", 50)

# Set up the game loop
game = True
score = 0
rocket_launched = False
rocket_velocity = [0, 0]
num_rockets = 3

# Load the rocket image
rocket_image = pygame.image.load("graphics/foguete.png")
rocket_image = pygame.transform.scale(rocket_image, (50, 50))
rocket_rect = rocket_image.get_rect()
rocket_rect.center = (100, screen_height - 200)

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
        screen.blit(background, (0, 0))
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
        screen.blit(background, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONPAGE_TEXT = get_font(100).render("OPTIONS", True, "White")
        OPTIONPAGE_RECT = OPTIONPAGE_TEXT.get_rect(center=(640, 80))
        screen.blit(OPTIONPAGE_TEXT, OPTIONPAGE_RECT)
        OPTIONS_TEXT = get_font(45).render("Para jogar basta mirar com o ponteiro do mouse na direção", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 250))
        OPTIONS_TEXT2 = get_font(45).render("em que deseja lançar o foguete. Em seguida, clique na tela para atirar ", True, "White")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(640, 300))
        OPTIONS_TEXT3 = get_font(45).render("o foguete, e então, TENTAR acertar os aliens inimigos.", True, "White")
        OPTIONS_RECT3 = OPTIONS_TEXT3.get_rect(center=(640, 350))
        OPTIONS_TEXT4 = get_font(45).render("OBS: Não se esqueça que os planetas possuem gravidade...", True, "White")
        OPTIONS_RECT4 = OPTIONS_TEXT4.get_rect(center=(640, 400))
        
        Wever = get_font(20).render("Game made by Alexandre Wever and Sergio Ramella", True, "White")
        Wever_rect = Wever.get_rect(center=(1110, 570))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        screen.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        screen.blit(OPTIONS_TEXT3, OPTIONS_RECT3)
        screen.blit(OPTIONS_TEXT4, OPTIONS_RECT4)
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

        screen.blit(background, (0, 0))

        #write on screen
        game_over = write('GAME OVER', 100, (225, 225, 225)) 
        end = write('PRESS RETURN TO END GAME', 40, (225, 225, 225))
        screen.blit(game_over, (400, 200))
        screen.blit(end, (400, 450))
        pygame.display.update()

        #if keys pressed return to the main menu    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            gameover = False
            pygame.quit()
            return  

#game score screen
def score_screen():
    score_screen = True
    while score_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 

        screen.blit(background, (0, 0))
        score_over = write('CONGRATS YOU WIN!', 100, (225, 225, 225)) 
        end = write('PRESS RETURN TO END GAME', 40, (225, 225, 225))
        screen.blit(score_over, (200, 200))
        screen.blit(end, (400, 450))
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            score_screen = False
            pygame.quit()
            return 



#--------------------------------------------------------------------# 


#-----------------------------Setting the Classes'-----------------------------#

# Set up the planets sprite
class Planets(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("graphics/3.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

planets = pygame.sprite.Group()
#add the planets randomly
planet_x_1 = random.randint(200 , 400)
planet_y_1 = random.randint(100 , 150)
planets.add(Planets(planet_x_1, planet_y_1))
planet_x_2 = random.randint(600 , 800)
planet_y_2 = random.randint(250 , 350)
planets.add(Planets(planet_x_2, planet_y_2))
planet_x_3 = random.randint(900 , 1100)
planet_y_3 = random.randint(400 , 500 )
planets.add(Planets(planet_x_3, planet_y_3))




# Set up the Alien sprite
class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("graphics/alien.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
        

aliens = pygame.sprite.Group()
#add the aliens near the planets

for planet in planets:
    alien_x = planet.rect.center[0] + random.randint(50, 70)
    alien_y = planet.rect.center[1] + random.randint(80, 100)
    aliens.add(Alien(alien_x, alien_y))
    
#function to calculate the gravity between the planets and the aliens
# def gravidade(constante,planeta,alien):
#     direcao_a = np.array([planeta.rect.center[0],planeta.rect.center[1]]) - np.array([alien.rect.center[0],alien.rect.center[1]])
#     distancia = np.linalg.norm(direcao_a)
#     direcao_a = direcao_a/distancia
#     mag_a = constante / distancia**2
#     a_alien = mag_a * direcao_a
#     return a_alien    

# circular movement of the aliens around the planets
radius = 50
angle = 0
#----------------------------GAME LOGIC----------------------------#
main_menu()

while game:
    
    
    # for planet,alien in zip(planets,aliens):
    #     a_alien = gravidade(50000,planet,alien)
    #     vel_alien = vel_alien +  a_alien
    #     alien.move(vel_alien)

    for alien,planet in zip(aliens,planets):
        x = int(radius * math.cos(math.radians(angle))) + planet.rect.center[0] - 20
        y = int(radius * math.sin(math.radians(angle))) + planet.rect.center[1] - 20
        
        alien.move(x, y)

    angle += 1


    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        #make the player choose the angle and power of the rocket, make it like a slingshot
        if event.type == pygame.MOUSEBUTTONDOWN and not rocket_launched:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = (mouse_y - rocket_rect.centery) / 10
            power = (mouse_x - rocket_rect.centerx) / 10
            rocket_velocity = [power, angle]
            rocket_launched = True



    # Update the rocket position and velocity if it has been launched
    if rocket_launched:
        rocket_velocity[1] += 1
        rocket_rect.move_ip(rocket_velocity)
    
    # Detect collisions between the rocket and the aliens
    if rocket_launched:
        for alien in aliens:
            if rocket_rect.colliderect(alien.rect):
                alien.kill()
                score += 10

    

    #respawn the rocket if it goes off the screen
    if rocket_rect.top > screen_height:
        num_rockets -= 1
        if num_rockets == 0:
            game = False
            gameover()

        else:
            rocket_launched = False
            rocket_rect.center = (100, screen_height - 200)
            rocket_velocity = [0, 0]

    #if all the aliens are gone, the player wins and the score screen appears
    if len(aliens) == 0:
        game = False
        score_screen()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False    
    


    # Draw the background, rocket, aliens, and obstacles on the screen
    # Draw the background full image
    screen.blit(background, (0, 0))
    screen.blit(rocket_image, rocket_rect)

    aliens.draw(screen)
    planets.draw(screen)

    # Draw the score on the screen
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw the remaining rockets on the screen
    rocket_text = font.render("Rockets: " + str(num_rockets), True, (255, 255, 255))
    screen.blit(rocket_text, (10, 50))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()



