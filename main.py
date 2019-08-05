import pygame


class animation():

    def setStartPoint(self):

        current_point = [None, None]
    
        if self.anim[0] == 'top':
            current_point[0] = self.destination[0]
            current_point[1] = 0

        if self.anim[0] == 'bottom':
            current_point[0] = self.destination[0]
            current_point[1] = display_height            
            
        return current_point


    def __init__(self, surface, destination, anim = None, speed = None):
    
        self.surface = surface
        self.destination = destination
        
        if anim == None:
            self.anim_prog = False
        else:
            self.anim = anim
            self.anim_prog = anim
            self.current_point = self.setStartPoint()

        self.speed = speed if speed != None
            
			
    def updateProgress(self):
	
		if self.anim[0] == 'top' and self.current_point > self.destination:
			if type(self.anim_prog) == str
				self.anim_prog = ''
		
		
    def getNextPoint(self):
        
        if self.anim_prog[0] == 'top' or self.anim[1] == 'bottom_reverse':
            self.current_point[1] = self.current_point[1] + self.speed

        if self.anim[0] == 'bottom' or self.anim[1] == 'top_reverse':
             self.current_point[1] = self.current_point[1] - self.speed:
		
		if self.anim[1] == 'vanish':
             self.current_point[1] = self.current_point[1] - self.speed

		self.updateProgress()

        return self.current_point
		

    def getSize(self):

        return self.surface.get_size()
    


class Button():

    def setText(self, text):

        self.text = text
        self.txt_surf = game_font.render(self.text, True, black)

        txt_width, txt_height = self.txt_surf.get_size()
        mid_point_x = self.button_location[0] + (self.button_size[0]/2)
        mid_point_y = self.button_location[1] + (self.button_size[1]/2)

        self.txt_loc = (mid_point_x - (txt_width/2), mid_point_y - (txt_height/2))


    def __init__(self, colour, button_location, button_size = None):        

        self.button_location = button_location
        self.colour = colour

        if button_size != None :
            self.button_size = button_size
        else:
            self.button_size = [50, 25]

        self.light_colour = (colour[0] - 25, colour[1] - 25, colour[2] - 25)
        

    def draw(self):

        self.rect = pygame.draw.rect(gameDisplay, self.colour, (self.button_location[0], self.button_location[1], self.button_size[0], self.button_size[1]), 2)
    

    def hover(self):

        pygame.draw.rect(gameDisplay, self.light_colour, (self.button_location[0], self.button_location[1], self.button_size[0], self.button_size[1]), 2)



def play_music(file_name):

    music = pygame.mixer.music

    music.load(file_name)
    music.play(-1)
    music.set_volume(0.25)


def animate(animation_obj):

    if type(animation_obj.anim_prog) == str:
        gameDisplay.blit(animation_obj.surface, animation_obj.current_point)
        animation_obj.current_point = animation_obj.getNextPoint()
    elif animation_obj.anim_prog == 'finish':
        gameDisplay.blit(animation_obj.surface, animation_obj.destination)
        return True
    else:
        return True
        


def take_input():
    pass
    


def game_intro():

##    play_music('music/intro_music.mp3')

    welcome_surf = pygame.image.load('images/welcome.png')
    welcome_obj = animation(welcome_surf, [130, 75], 'top', 5)

    start_button = Button(grey, (335, 450), (100, 50))
    start_button.setText('Start')
    start_button.draw()

    intro = True

    while intro:
	
        gameDisplay.fill(white)

        if animate(welcome_obj):
            
            gameDisplay.blit(start_button.txt_surf, start_button.txt_loc)

            for event in pygame.event.get():
                print(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                mouse_position = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    if start_button.rect.collidepoint(mouse_position):
                        start_button.hover()
                                                                       
                if event.type == pygame.MOUSEBUTTONUP:
                    if start_button.rect.collidepoint(mouse_position):
                        intro = False
            
        pygame.display.update()
        clock.tick(30)
		
    return True


def start_game():

    pygame.mixer.fadeout(2000)

##  play_music('music/game_music.mp3')

    ok_text_surf = game_font.render('OK!', True, black)
    ok_text = animation(ok_text_surf, [375, 50], 'top', 3)
	
    set_text_surf = game_font.render('Set the length of the word  ', True, black)
    set_text = animation(set_text_surf, [225,130])

    button_location = set_text.getSize()
    input_button = Button(grey, (set_text.destination[0] + button_location[0], set_text.destination[1]))

    started = False

    while not started:

        gameDisplay.fill(white)

        if animate(ok_text):
            animate(set_text)
            input_button.draw()

            for event in pygame.event.get():
                print(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                mouse_position = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    if input_button.rect.collidepoint(mouse_position):
                        input_button.hover()  
                                                                   
                if event.type == pygame.MOUSEBUTTONUP:
                    if input_button.rect.collidepoint(mouse_position):
                        take_input()
                        started = True
                    
			
        pygame.display.update()
        clock.tick(30)
	
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

game_font = pygame.font.Font(None, 35)
clock = pygame.time.Clock()

game_intro()
start_game()
#play()