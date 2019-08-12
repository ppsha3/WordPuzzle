"""
Changes to make:
1) string out of range in reveal_word
2) Separate Classes to different files
3) Create event handler

"""

import pygame
import random


class Cursor():

    def blink(self):

        self.draw()


    def firstCursorPos(self):

        start_x = self.button.button_location[0] + 6
        start_y = self.button.button_location[1] + 6

        self.start_point = [start_x, start_y]

        end_x = start_x
        end_y = start_y + self.button.button_size[1] - 12

        self.end_point = [end_x, end_y]


    def updateCursorPos(self, input_text):

        input_surf = game_font.render(input_text, True, black)
        text_area = input_surf.get_size()

        start_x = self.start_point[0] + text_area[0] + 2
        start_y = self.start_point[1]

        self.start_point = (start_x, start_y)

        self.end_point[0] = start_x
#	    self.end_point[1] = self.start_point[1]

        self.draw()

        return True


    def __init__(self, input_button):

        self.button = input_button
        self.firstCursorPos()
        self.cursor_active = False


    def draw(self):

        pygame.draw.aaline(gameDisplay, black, self.start_point, self.end_point)


class Animation():


    def setStartPoint(self):

        current_point = [None, None]

        if self.direction == 'top':
            current_point[0] = self.destination[0]
            current_point[1] = 0

        if self.direction == 'bottom':
            current_point[0] = self.destination[0]
            current_point[1] = display_height

        return current_point


    def __init__(self, surface, destination, direction = None, speed = None):

        self.surface = surface
        self.destination = destination
        self.surface_size = self.surface.get_size()

        if direction == None:
            self.done = True
        else:
            self.direction = direction
            self.current_point = self.setStartPoint()
            self.done = False
            self.speed = speed


    def getNextPoint(self):

        if self.direction == 'top':
            self.current_point[1] = self.current_point[1] + self.speed
            if self.current_point[1] >= self.destination[1]:
                self.current_point[1] = self.destination[1]

        if self.direction == 'bottom':
            self.current_point[1] = self.current_point[1] - self.speed
            if self.current_point[1] <= self.destination[1]:
                self.current_point[1] = self.destination[1]


    def animate(self):

        if not self.done:
            gameDisplay.blit(self.surface, self.current_point)
            self.getNextPoint()
            if self.destination <= self.current_point:
                self.done = True
        else:
            gameDisplay.blit(self.surface, self.destination)

        return self.done


    def updateSurface(self, word):

        new_font = pygame.font.Font(None, 40)
        self.surface = game_font.render(word, True, black)
        self.surface_size = self.surface.get_size()


class Button():


    def setText(self, text, align):

        self.text = text
        self.txt_surf = game_font.render(self.text, True, black)

        txt_width, txt_height = self.txt_surf.get_size()

        if align == 'center':
            x_point = self.button_location[0] + (self.button_size[0]/2) - (txt_width/2)
            y_point = self.button_location[1] + (self.button_size[1]/2) - (txt_height/2)

        if align == 'left':
            x_point = self.button_location[0] + 5
            y_point = self.button_location[1] + 5

        self.txt_loc = (x_point, y_point)

        gameDisplay.blit(self.txt_surf, self.txt_loc)


    def __init__(self, colour, button_location, button_size):

        self.button_location = button_location
        self.colour = colour
        self.button_size = button_size

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


def game_intro():

##    play_music('music/intro_music.mp3')

    welcome_surf = pygame.image.load('images/welcome.png')
    welcome_obj = Animation(welcome_surf, [130, 75], 'top', 5)

    start_button = Button(grey, (335, 450), (100, 50))

    intro = True

    while intro:

        gameDisplay.fill(white)

        if welcome_obj.animate():

            start_button.draw()
            start_button.setText(text='Start', align='center')

            for event in pygame.event.get():
##                print(event)

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


def parseInput(input_text):

    if int(input_text) in range(3,8):
        return True

    return False


def handle_events():

    global input_button, cursor, input_text

    for event in pygame.event.get():
##                print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            if input_button.rect.collidepoint(mouse_position):
                input_button.hover()

        if event.type == pygame.MOUSEBUTTONUP:
            if input_button.rect.collidepoint(mouse_position):
                cursor.cursor_active = True
            else:
                if cursor.cursor_active == True:
                    cursor.cursor_active = False

        if cursor.cursor_active == True and event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name == 'return':
                if parseInput(input_text):
                    cursor.cursor_active = False
                    return True
            elif key_name == 'backspace':
                input_text = ''
                cursor.firstCursorPos()
            elif len(input_text) == 0:
                input_text = key_name
                cursor.updateCursorPos(input_text)
            else:   pass

    return False


def start_game():

    global input_button, cursor, input_text

##  pygame.mixer.fadeout(2000)
##  play_music('music/game_music.mp3')

    ok_text_surf = game_font.render('OK!', True, black)
    ok_text = Animation(ok_text_surf, [375, 50], 'top', 3)

    set_text_surf = game_font.render('Set the length of the word between 3 to 7 ', True, black)
    set_text = Animation(set_text_surf, [170,130])

    text_size = set_text.surface.get_size()
    button_location = (set_text.destination[0] + text_size[0], set_text.destination[1] - 5)
    input_button = Button(grey, button_location, [40, 30])

    cursor = Cursor(input_button)
    input_text = ''

    started = False
    while not started:
        gameDisplay.fill(white)

        if ok_text.animate():
            set_text.animate()

            input_button.draw()

            if handle_events():
                started = True

            if cursor.cursor_active == True:
                cursor.blink()

            if len(input_text) > 0:
                input_button.setText(input_text, align='left')

        pygame.display.update()
        clock.tick(30)

    return input_text


def generate_word(len_word):

    filepath = "words/word" + str(len_word) + ".txt"

    with open("{}".format(filepath),"r") as wordfile:

        words = wordfile.readlines()
        random_word = random.choice(words)

    return random_word


def reveal_word(current_guess, current_word, word):

    new_word = ''

    for i in range(len(word)):
        if current_guess == word[i]:
            current_word = current_word.replace(current_word[i], current_guess, 1)
        new_word = new_word + current_word[i] + ' '

    print(current_word)
    print(new_word)

    return current_word, new_word


def parse_guess(current_guess):

    if current_guess.lower().isalpha():
        return True
    if current_guess == '*':
        reveal_hint()
        return True


def getCenter(obj, width = None, height = None):

    if width == None:
        width = display_width

    if height == None:
        height = display_height

    x_point = width/2 - obj[0]/2
    y_point = height/2 - obj[1]/2

    return (x_point, y_point)


def play(word_len):

    new_font = pygame.font.Font(None, 40)

    word = generate_word(word_len)
    print(word)

    current_word = '*' * word_len
    disp_curr_word = '* ' * word_len
    current_word_text = new_font.render(disp_curr_word, True, black)
    center_point = getCenter(current_word_text.get_size(), height=95)
    current_word_obj = Animation(current_word_text, center_point)

    guess_text = new_font.render('Guess the word', True, black)
    guess_obj = Animation(guess_text, [300, 100])

    input_button = Button(grey, [375, 150], [40, 30])
    cursor = Cursor(input_button)

    previous_guess = []
    current_guess = ''

    play = True

    while play:

        gameDisplay.fill(white)

        pygame.draw.aaline(gameDisplay, black, (0, 75), (display_width, 75))

        current_word_obj.animate()
        guess_obj.animate()

        input_button.draw()

        for event in pygame.event.get():
##            print(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            mouse_position = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                if input_button.rect.collidepoint(mouse_position):
                    input_button.hover()

            if event.type == pygame.MOUSEBUTTONUP:
                if input_button.rect.collidepoint(mouse_position):
                    cursor.cursor_active = True
                else:
                    if cursor.cursor_active == True:
                        cursor.cursor_active = False

            if cursor.cursor_active == True and event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                if key_name == 'return':
                    if parse_guess(current_guess):
                        print(current_guess, current_word, word)
                        current_word, new_word = reveal_word(current_guess, current_word, word)
                        current_word_obj.updateSurface(new_word)
                    current_guess = ''
                    cursor.firstCursorPos()
                elif key_name == 'backspace':
                    current_guess = ''
                    cursor.firstCursorPos()
                elif len(current_guess) == 0:
                    current_guess = key_name
                    cursor.updateCursorPos(current_guess)
                else:   pass


        if cursor.cursor_active == True:
            cursor.blink()

        if len(current_guess) > 0:
            input_button.setText(current_guess, align='left')

        clock.tick(30)
        pygame.display.update()

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

game_font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

game_intro()
word_len = start_game()
play(int(word_len))
