import pygame
from Ball import Ball
from Score import Score
from Player import Player


# Sets and initializes all the variables and objects before starting the game

# Init pygame
pygame.init()

# Set dimensions of the game screen
display_width = 1000
display_height = 800

# Make the display
screen = pygame.display.set_mode((display_width, display_height))
# Sets caption of the window
pygame.display.set_caption('pypong')

# Make score
score = Score(0, 0)

# Make ball
ball = Ball()

# Make players
p1 = Player("Left")
p2 = Player("Right")

# Makes list of sprites to add to pygame sprite group
sprites = pygame.sprite.Group()
# Adds our objects to the group so we can call the draw method
sprites.add(p1)
sprites.add(p2)
sprites.add(ball)
sprites.add(score)

# Creates pygame clock object to manage framerate
clock = pygame.time.Clock()

# Sets game state
running = True

# Main loop that runs the game
while not score.has_won() and running:

    # Refreshes the screen
    screen.fill((0, 0, 0))

    # Ends pygame if reached
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updates all the objects on screen
    sprites.update(score)

    # Checks for collision between ball and player
    if (pygame.sprite.collide_rect(p1, ball) or
       pygame.sprite.collide_rect(ball, p2)):
        ball.reflect()

    # Draws all the objects
    sprites.draw(screen)
    # Updates the whole display
    pygame.display.flip()

    # Increments clock at 60 frames per second
    clock.tick(60)

# When someone has won, the loop will end
# Displays the winner
font = pygame.font.Font(None, 69)
text = font.render(
    f"{score.who_won()} is the winner!", True, (255, 255, 255)
    )

# Gets position of text string centered around the specified spot
text_rect = text.get_rect(
    center=(display_width // 2, display_height // 2)
    )
# Updates to the screen
screen.blit(text, text_rect)
pygame.display.flip()

# Quits pygame
pygame.quit()
