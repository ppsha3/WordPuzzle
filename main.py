import pygame


def create_text(text, text_location, font_size, bg_colour = None):

    game_font = pygame.font.Font(None, font_size)

    if bg_colour == None:
        text_surf = game_font.render(text, True, black)
    else:
        text_surf = game_font.render(text, True, black, grey)

    text_rect = text_surf.get_rect()
    
    gameDisplay.blit(text_surf, text_location)

    return text_rect
    

def hover(start_button):

    button_rect = pygame.draw.rect(gameDisplay, light_grey, (start_button[0], start_button[1], start_button[2], start_button[3]), 2)
        
    return True


def center_text(button_rect, text_rect):

    mid_point_x = button_rect[0] + (button_rect[2]/2)
    mid_point_y = button_rect[1] + (button_rect[3]/2)

    text_location = (mid_point_x - (text_rect[2]/2), mid_point_y - (text_rect[3]/2))

    return list(map(int, text_location))


def create_button(text, button_location, button_size, bg_colour = None):

    game_font = pygame.font.Font(None, 30)

    if bg_colour == None:
        text_surf = game_font.render(text, True, black)
    else:
        text_surf = game_font.render(text, True, black, grey)

    text_rect = text_surf.get_rect()
    
    button_rect = pygame.draw.rect(gameDisplay, grey, (button_location[0], button_location[1], button_size[0], button_size[1]), 2)
    
    text_location = center_text(button_rect, text_rect)
    
    gameDisplay.blit(text_surf, text_location)
    
    return button_rect
    

def display_image(image_name, image_location = None):
    
    image_surf = pygame.image.load(image_name)
    image_rect = image_surf.get_rect()

    if image_location == None:
        image_location = ((display_width/2) - (image_rect[2]/2), (display_height/2) - (image_rect[3]/2))

    gameDisplay.blit(image_surf, image_location)

    
def play_music(file_name):

    music = pygame.mixer.music

    music.load(file_name)
    music.play(-1)
    music.set_volume(0.25)
    
    
def game_intro():

        intro = True

##        play_music('music/intro_music.mp3')        
        while intro:
    
                gameDisplay.fill(white)
        
                display_image('images/welcome_image.jpg', (200, 115))
                display_image('images/WordPuzzle.jpg', (225, 235))
                start_button = create_button('Start', (350, 385), (100, 50))
                
                for event in pygame.event.get():
                    print(event)

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                        
                    mouse_position = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONUP:
                        if start_button.collidepoint(mouse_position):
                            intro = False

                    if event.type == pygame.MOUSEMOTION:
                        if start_button.collidepoint(mouse_position):
                            hover(start_button)            
                    
                
                pygame.display.update()

                clock.tick(10)
        
        return True


def input_box(input_rect, location):

    x_location = location[0] + input_rect[2]
    y_location = location[1] + input_rect[3]

    button_rect = pygame.draw.rect(gameDisplay, grey, (x_location, y_location, 50, 25), 2)

def check_input():
    pass


def start_game():

    pygame.mixer.fadeout(2)
	
    started = False

##    play_music('music/game_music.mp3')
    
    while started == False:

            gameDisplay.fill(white)
    
            ok_text = create_text('OK!', (385, 50), 30)
            input_rect = create_text('Set the length of the word ', (250,100), 30)
            input_box(input_rect, (250,100))

            for event in pygame.event.get():
                print(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

##                mouse_position = pygame.mouse.get_pos()
##                if event.type == pygame.MOUSEBUTTONUP:
##                    if input_box.collidepoint(mouse_position):
##                        check_input()
##                        started = True
##
##                if event.type == pygame.MOUSEMOTION:
##                    if start_button.collidepoint(mouse_position):
##                        hover(start_button)            
                
            
            pygame.display.update()

            clock.tick(10)
    
    return True


pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('WordPuzzle')

black = (75,75,75)
white = (255,255,255)
grey = (150,150,200)
light_grey = (75,75,100)

clock = pygame.time.Clock()

game_intro()
start_game()
play()
