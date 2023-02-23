import pygame
from button import Button
from button import *
import random


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
bird_launched = False
bird_velocity = [0, 0]
num_birds = 3

# Load the bird image
bird_image = pygame.image.load("graphics/foguete.png")
bird_image = pygame.transform.scale(bird_image, (50, 50))
bird_rect = bird_image.get_rect()
bird_rect.center = (100, screen_height - 200)

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
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("graphics/3.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

planets = pygame.sprite.Group()
#add the planets randomly
for i in range(3):
    x = random.randint(500, 1000)
    y = random.randint(100, 600)
    planets.add(Planets(x, y))

# Set up the pig sprite
class Pig(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("graphics/alien.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

pigs = pygame.sprite.Group()
#add the pigs randomly
for i in range(3):
    x = random.randint(500, 1000)
    y = random.randint(100, 600)
    pigs.add(Pig(x, y))
    


#----------------------------GAME LOGIC----------------------------#
main_menu()

while game:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        #make the player choose the angle and power of the bird, make it like a slingshot
        if event.type == pygame.MOUSEBUTTONDOWN and not bird_launched:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = (mouse_y - bird_rect.centery) / 10
            power = (mouse_x - bird_rect.centerx) / 10
            bird_velocity = [power, angle]
            bird_launched = True



    # Update the bird position and velocity if it has been launched
    if bird_launched:
        bird_velocity[1] += 1
        bird_rect.move_ip(bird_velocity)
    
    # Detect collisions between the bird and the pigs
    if bird_launched:
        for pig in pigs:
            if bird_rect.colliderect(pig.rect):
                pig.kill()
                score += 10

    

    #respawn the bird if it goes off the screen
    if bird_rect.top > screen_height:
        num_birds -= 1
        if num_birds == 0:
            game = False
            gameover()

        else:
            bird_launched = False
            bird_rect.center = (100, screen_height - 200)
            bird_velocity = [0, 0]

    #if all the pigs are gone, the player wins and the score screen appears
    if len(pigs) == 0:
        game = False
        score_screen()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

    #add the pigs arround the planets and make it move on circles
    for pig in pigs:
        pig.rect.x -= 1
        pig.rect.y += 1
        if pig.rect.x < 0:
            pig.rect.x = 1000
        if pig.rect.y > 600:
            pig.rect.y = 0


        
            
    # Draw the background, bird, pigs, and obstacles on the screen
    # Draw the background full image
    screen.blit(background, (0, 0))
    screen.blit(bird_image, bird_rect)
    pigs.draw(screen)
    planets.draw(screen)

    # Draw the score on the screen
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw the remaining birds on the screen
    bird_text = font.render("Rockets: " + str(num_birds), True, (255, 255, 255))
    screen.blit(bird_text, (10, 50))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()



