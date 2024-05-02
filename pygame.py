# Import necessary libraries
import pygame  # Import the pygame library for creating the game
import math  # Import the math library for mathematical operations
import time  # Import the time library for time-related functions
import sys  # Import the sys library for system-specific functions
import random  # Import the random library for random number generation
import pygame.mixer  # Import the pygame mixer for handling audio

# Initialize pygame
pygame.init()  # Initialize the pygame library
pygame.mixer.init()  # Initialize the pygame mixer for audio

# Set up a flag to determine if the game has started
game_started = False

# Load and play the background music
pygame.mixer.music.load('ไฟล์ที่ใช้ในเกม/x2mate.com - No Copyright Music _ Cute Background Music (cute, funny, bgm) (128 kbps).mp3')
pygame.mixer.music.play(-1)  # Play the background music in a loop (-1 means loop indefinitely)

# Load custom start music
start_music = pygame.mixer.Sound('ไฟล์ที่ใช้ในเกม/x2mate.com - [no copyright music] cute background music _ funny _ Pick!! (128 kbps).mp3')

# Define the dimensions of the game window
display_width = 490
display_height = 735

# Define color constants
black = (0, 0, 0)
white = (255, 255, 255)

# Create the game display window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pew')  # Set the title of the game window
clock = pygame.time.Clock()  # Create a clock to control the frame rate
crashed = False  # Initialize a flag to track if the game has crashed

# Load and scale player character images
ChaImg = pygame.image.load('ไฟล์ที่ใช้ในเกม/ใช้ตัวนี้ 1.png')
ChaImg = pygame.transform.scale(ChaImg, (100, 100))  # Scale the character image

Cha2Img = pygame.image.load('ไฟล์ที่ใช้ในเกม/ใช้ตัวนี้ 2.png')
Cha2Img = pygame.transform.scale(Cha2Img, (100, 100))  # Scale the character image

Cha3Img = pygame.image.load('ไฟล์ที่ใช้ในเกม/ใช้ตัวนี้ 3.png')
Cha3Img = pygame.transform.scale(Cha3Img, (100, 100))  # Scale the character image

# Load the background image
bgImg = pygame.image.load('ไฟล์ที่ใช้ในเกม/之前的项目《全民水浒》上线了，有些工作图也可以解禁了_HC誠_新浪博客.jpg').convert()

# Load and scale the object image
ObjectImg = pygame.image.load('ไฟล์ที่ใช้ในเกม/object.png')
ObjectImg = pygame.transform.scale(ObjectImg, (100, 100))  # Scale the object image

# Load the start background image and scale it to the display dimensions
start_bgImg = pygame.image.load('ไฟล์ที่ใช้ในเกม/ -3.jpg').convert()
start_bgImg = pygame.transform.scale(start_bgImg, (display_width, display_height))

# Set up scrolling background variables
scroll = 0
bg_height = bgImg.get_height()
tiles = math.ceil(display_height / bg_height) + 1

# Function to generate a random object position
def Object():
    rand_xo = random.randint(1, 3)
    if rand_xo == 1:
        xo = 89
        yo = -100
    elif rand_xo == 2:
        xo = 200
        yo = -100
    elif rand_xo == 3:
        xo = 311
        yo = -100
    return xo, yo

# Function to change the character based on a random number
def Change():
    rand_change = random.randint(1, 12)  # Generate a random number between 1 and 12
    if rand_change % 3 == 0:
        return 0  # Return 0 to indicate no character change
    elif rand_change % 3 == 1:
        return 1  # Return 1 to indicate a character change to the second image
    elif rand_change % 3 == 2:
        return 2  # Return 2 to indicate a character change to the third image

# Get the rectangular object for the player character
rect = ChaImg.get_rect()  # Get the rectangular dimensions of the character image

recto = ObjectImg.get_rect()  # Get the rectangular dimensions of the object image

# Function to draw the character on the screen based on 'a' parameter
def chaDraw(a):
    if a >= 0 and a <= 100:
        gameDisplay.blit(ChaImg, rect)  # Display the first character image
    elif a > 100 and a <= 200:
        gameDisplay.blit(Cha2Img, rect)  # Display the second character image
    elif a > 200 and a <= 300:
        gameDisplay.blit(Cha3Img, rect)  # Display the third character image
    print(rect.x)  # Print the x-coordinate of the character's position

# Function to render text on the screen
def text_objects(text, font):
    text_surface = font.render(text, True, black)  # Render the text with the specified font and color
    return text_surface, text_surface.get_rect()

# Function to display a message on the screen with an optional vertical offset
def message_display(text, y_offset=0):
    largeText = pygame.font.Font('freesansbold.ttf', 30)  # Create a font object
    TextSurf, TextRect = text_objects(text, largeText)  # Render the text and get its rectangular dimensions
    TextRect.center = (display_width * 0.5, display_height * 0.5 + y_offset)  # Center the text on the screen
    gameDisplay.blit(TextSurf, TextRect)  # Display the text on the screen

# Function to check for collision between the character and the object
def is_collision(character_rect, object_rect):
    return character_rect.colliderect(object_rect)  # Check if the character and object rectangles overlap

# Function to handle collision and end the game
def crash():
    message_display('BOOM!')  # Display the 'BOOM!' message on the screen
    print('12312312313')  # Print a message to the console

# Function to display the game start screen
def gamestart():
    gameDisplay.blit(start_bgImg, (0, 0))  # Display the start background image
    font = pygame.font.Font(None, 36)
    start_text = font.render('Click to Start', True, black)  # Render the start text
    text_rect = start_text.get_rect(center=(display_width / 2, display_height / 2))  # Center the text on the screen
    gameDisplay.blit(start_text, text_rect)  # Display the start text
    pygame.display.update()

# Initialize the score variables
score = 0

# Initialize variables for character and object positions
a = 0
xb = 0
yb = 0
x = 200
y = (display_height * 0.75)
rect.topleft = (200, 551.25)  # Set the initial position of the character rectangle

xo = -100
yo = -100  # Set initial position of the object rectangle

x = 200
y = (display_height * 0.75)
rect.topleft = (200, y)  # Set initial position of the character rectangle

# Initialize variables for character movement
can_move_left = True
can_move_right = True  # Initialize variables to control character movement

# Flag to control the game loop
game_over = False  # Initialize a flag to control the game state

# Main game loop
while not crashed and not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and can_move_left:
                rect.move_ip(-111, 0)  # Move the character rectangle to the left
            elif event.key == pygame.K_RIGHT and can_move_right:
                rect.move_ip(111, 0)  # Move the character rectangle to the right

        # Check for mouse click to start the game
        if event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            game_started = True
            pygame.mixer.music.stop()  # Stop the background music
            start_music.play()  # Play the start music

    if not game_started:
        gamestart()  # Display the game start screen
        continue  # Skip the game logic until the player clicks to start

    # Update object and character positions
    yb += 5
    yo += 5
    a += 1

    if yb > bg_height:
        yb = 0

    if yb == bg_height:
        xo, yo = Object()  # Generate a new random object position
        print(xo)
        print(yo)

    if rect.left == 89:
        can_move_left = False
        can_move_right = True
    if rect.left == 200:
        can_move_left = True
        can_move_right = True
    if rect.left == 311:
        can_move_left = True
        can_move_right = False

    # Check for collision with the object
    if is_collision(rect, pygame.Rect(xo, yo, 100, 100)):
        game_over = True
        print('1')  # Print a message to the console indicating a collision

    else:
        score += 1  # Increment the score when there's no collision

    # Draw the background, character, object, and score on the screen
    gameDisplay.blit(bgImg, (xb, yb - bg_height))
    gameDisplay.blit(bgImg, (xb, yb))
    chaDraw(a)  # Draw the character based on the 'a' parameter

    if a > 311:
        a = 0

    gameDisplay.blit(ObjectImg, (xo, yo))  # Draw the object on the screen

    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, white)
    gameDisplay.blit(score_text, (10, 10))  # Display the player's score

    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 frames per second

# Game over loop
while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    message_display('BOOM!', -100)  # Display the 'BO

    pygame.display.update()  # Update the display to show the game over message
    pygame.time.delay(2000)  # Delay the game for 2000 milliseconds (2 seconds)


    message_display(f'Your Score: {score}')  # Display the player's score

    pygame.display.update()  # Update the display to show the high score and player's score
    pygame.time.delay(2000)  # Delay the game for 2000 milliseconds (2 seconds)

