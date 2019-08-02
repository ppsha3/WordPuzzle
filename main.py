import pygame


def hover(start_button):

    button_rect = pygame.draw.rect(gameDisplay, light_grey, (start_button[0], start_button[1], start_button[2], start_button[3]), 2)
		
    return True


def center_text(button_rect, text_rect):

    mid_point_x = button_rect[0] + (button_rect[2]/2)
    mid_point_y = button_rect[1] + (button_rect[3]/2)

    text_location = (mid_point_x - (text_rect[2]/2), mid_point_y - (text_rect[3]/2))

    return list(map(int, text_location))


def create_button(text, button_location, button_size, bg_colour = None):

    global game_font

    button_rect = pygame.draw.rect(gameDisplay, grey, (button_location[0], button_location[1], button_size[0], button_size[1]), 2)

    text_surf = game_font.render(text, True, black)
    text_rect = text_surf.get_rect()
    text_location = center_text(button_rect, text_rect)
	
    gameDisplay.blit(text_surf, text_location)

    return button_rect
	

def load_image(image_name):
	
    image_surf = pygame.image.load(image_name)
##    image_rect = image_surf.get_rect()

    return image_surf

	
def play_music(file_name):

    music = pygame.mixer.music

    music.load(file_name)
    music.play(-1)
    music.set_volume(0.25)
	
	
def game_intro():

    global wel_animation, puzz_animation

    play_music('music/intro_music.mp3')        

    wel_surf = load_image('images/welcome_image.jpg')
    puzz_surf = load_image('images/WordPuzzle.jpg')

    wel_animation = animate(direction = 'top', speed = 10)

    intro = True

    while intro:
	
        gameDisplay.fill(white)

        display_image(wel_surf, (200, 115), wel_animation)
        display_image(puzz_surf, (225, 235))

        start_button = create_button('Start', (350, 385), (100, 50))

        handle_event(start_button)   
        
        pygame.display.update()
        clock.tick(10)
		
    return True


def create_input_box(len_text, location):

    x_location = location[0] + len_text[2] 
    y_location = location[1] - 5

    button_rect = pygame.draw.rect(gameDisplay, grey, (x_location, y_location, 50, 25), 2)

    return button_rect


def handle_event():

    global input_box, start_button

    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            if input_box.collidepoint(mouse_position):
                hover(input_box)
            if start_button.collidepoint(mouse_position):
                hover(start_button)
								   
        if event.type == pygame.MOUSEBUTTONUP:
            if input_box.collidepoint(mouse_position):
##                take_input()
##                started = True
            if start_button.collidepoint(mouse_position):
                intro = False       


def create_text(text, text_location, font_size, direction = None):

    game_font = pygame.font.Font(None, font_size)

    text_surf = game_font.render(text, True, black)
    text_rect = text_surf.get_rect()

    if direction == None:
        gameDisplay.blit(text_surf, text_location)
    else:
        animate(direction, text_surf, text_location, 15)

    return text_rect


def animate(direction, speed, rect, destination):

    animation = dict()

    if direction == 'top':
        animation["x_coo"] = destination[0]
        animation["y_coo"] = 0

##    if direction == 'top':
##        animation["x_coo"] = destination[0] - int(rect[3]/2)
##        animation["y_coo"] = 0
##
##    if direction == 'top':
##        animation["x_coo"] = destination[0] - int(rect[3]/2)
##        animation["y_coo"] = 0
##
##    if direction == 'top':
##        animation["x_coo"] = destination[0] - int(rect[3]/2)
##        animation["y_coo"] = 0
        
    animation["speed"] = speed
    animation["destination"] = destination
    animation["done"] = False


def display_image(obj_surf):
    
    global animation

    if animation["done"]:
        gameDisplay.blit(obj_surf, (animation["x_coo"], animation["y_coo"]))
        animation["y_coo"] = animation["y_coo"] + animation["speed"]
        if animation["destination"] == (animation["x_coo"], animation["y_coo"]):
            animation["done"] = True
    else:
        gameDisplay.blit(obj_surf, animation["destination"])
        
    return True
	 
	 
def check_input():
	pass


def start_game():

#   pygame.mixer.fadeout(2)

    started = False
    
    current_point = (400, 0)

##    play_music('music/game_music.mp3')

    while not started:

        gameDisplay.fill(white)

        ok_text = create_text('OK!', (385, 50), 30, 'top')
        set_len_text = create_text('Set the length of the word  ',(250,100), 30)
        input_box = create_input_box(set_len_text, (250,100))

        handle_event()			
			
        pygame.display.update()
        clock.tick(10)
	
    return True


pygame.init()

display_width = 800
display_height = 600
game_font = pygame.font.Font(None, 30)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('WordPuzzle')

black = (75,75,75)
white = (255,255,255)
grey = (150,150,200)
light_grey = (75,75,100)

clock = pygame.time.Clock()

game_intro()
start_game()
#play()
