# pip install pygame
import pygame

# Import random for random numbers
import random

# pip install pyserial 
import serial
import json

# change the port as necessary by your OS
ser = serial.Serial('/dev/cu.usbserial-02301AC2', 9600)

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# initialization
pygame.init()
pygame.mixer.init()

# play music on loop
pygame.mixer.music.load('alexander-nakarada-space-ambience.mp3')
pygame.mixer.music.play(-1)

# -- PLAYER CLASS -- #
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    
    # Move the sprite based on hardware movement
    def update(self, movement):
        paused = 0

        vY = int(movement['vY']) * (-1)
        vX = int(movement['vX'])
        button = int(movement['button'])
        
        # pause if button pressed
        if (button == 0):
            paused = 1
            return paused

        # move player up/down
        if vY:
            self.rect.move_ip(0, vY)

        # move player right/left
        if vX:
            self.rect.move_ip(vX, 0)


        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        # returns status of whether or not game is paused
        return paused

# -- ENEMY CLASS -- #
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()

        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self, movement):

        # change direction and speed of enemies
        dial = int(movement['dial'])

        if dial:
            self.rect.move_ip(-(self.speed+(dial)), 0)
        else:
            self.rect.move_ip(-self.speed, 0)

        if self.rect.right < 0:
            self.kill()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set screen size
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Run until the user asks to quit
running = True
while running:

    # Get current movement of hardware
    string = str(ser.readline().strip(), 'ascii')

    # Prints hardware input to console
    print()
    print(string)
    print()

    # fix bad inputs
    if (len(string) == 0):
        continue

    while (string[0] != '{' and string[0] != '}'):
        string = string[1:]
        continue
    
    if (string[0] == '}'):
        continue

    input = json.loads(string)
    button = input['button']
    dial = input['dial']
    vY = input['vY']
    vX = input['vX']
    switch = input['switch']

    # Check if user clicked the window close button
    for event in pygame.event.get():

        # check if user hit a key
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    
    # Update player position based on hardware input
    paused = player.update(input)

    # Pause game if button is pressed
    if (paused == 1):
        continue
    
    # Update enemy position and speed based on hardware input
    enemies.update(input)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Used for testing purposes
    #   - Set invincible to 1 to turn make player unable to die
    invincible = 0

    # Check if any enemies have collided with the player
    if (pygame.sprite.spritecollideany(player, enemies) and invincible == 0): 
        # If so, then remove the player and stop the loop
        running = False

        # kill all sprites
        for entity in all_sprites:
            entity.kill()

        # List of end quotes
        quotes = ["So much universe and so little time.", 
        "The Earth is the cradle of humanity, but mankind cannot stay in the cradle forever.", 
        "Space exploration is a force of nature unto itself that no other force in society can rival.",
        "Exploration is not a choice really; it's an imperative.",
        "Remember to look up at the stars and not down at your feet.",
        "When I first looked back at the Earth, standing on the Moon, I cried.",
        "To confine our attention to terrestial matters would be to limit the human spirit.",
        "I didn't feel like a giant. I felt very, very small."]

        # List of corresponding end quote citations
        citations = ["-Terry Pratchett",
                    "-Konstantin Tsiolkovsky",
                    "-Neil deGrasse Tyson",
                    "-Michael Collins, Apollo 11 Astronaut",
                    "-Stephen Hawking",
                    "-Alan Shepard",
                    "-Stephen Hawking",
                    "-Neil Armstrong"]

        # random selection of end quote and corresponding citation
        selection = random.randint(0, len(quotes)-1)
        
        # size based on selection
        size = 22
        if selection == 1 or selection == 2 or selection == 6:
            size = 18

        # draw end quote onto screen
        font = pygame.font.Font('freesansbold.ttf', size)
        text_surface1 = font.render(quotes[selection], True, (0, 255, 255))
        text_surface2 = font.render(citations[selection], True, (0, 255, 255))
        text_rect1 = text_surface1.get_rect()
        text_rect2 = text_surface2.get_rect()
        text_rect1.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-20)
        text_rect2.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+15)
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)
        pygame.display.flip()

        # wait for 6 seconds before quitting
        pygame.time.wait(6000)


    # Update the display
    pygame.display.flip()

pygame.quit()
