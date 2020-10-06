import pygame
import random
from Ball import Ball
from Score import Score
from Player import Player
from Powerup import Powerup


# Init pygame
pygame.init()

# Set dimensions of the game screen
# Proctected because the display is set to a good value for the game
# But can be changed if desired
_display_width = 1000
_display_height = 800

# Make the display
screen = pygame.display.set_mode((_display_width, _display_height))
# Sets caption of the window
pygame.display.set_caption('pypong')


# Main loop that runs the game
def game():
    # Sets all the variables and objects before starting the game

    # Make ball
    ball = Ball()
    # Makes group of ball sprites to allow for powerups
    balls = pygame.sprite.Group()
    balls.add(ball)

    # Makes the powerup object
    powerup = Powerup()

    # Make players
    p1 = Player("Left")
    p2 = Player("Right")

    # Make score
    score = Score(p1, p2)

    # List of players for paddle reset
    p_list = [p1, p2]

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
    while not score.has_won() and running:

        # Refreshes the screen
        screen.fill((0, 0, 0))

        # Ends pygame if reached
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Checks to see if both players already have a powerup
        # If they do, then don't release another one
        if not p1.is_big() or not p2.is_big():
            # Checks to see if a powerup already exists
            # Randomly makes powerup object with 1% chance per frame
            if not sprites.has(powerup) and random.random() < 0.01:
                # Makes a new powerup object
                powerup = Powerup()
                # If not, add it to the ball group
                balls.add(powerup)
                # Add it to the sprite group
                sprites.add(powerup)

        # Checks for collision between ball and player
        if pygame.sprite.spritecollide(p1, balls, False):
            # Gets list of collided balls
            collide_balls = pygame.sprite.spritecollide(p1, balls, False)
            # Calls their reflect method
            for ball in collide_balls:
                ball.reflect(p1)
        # Do the same for p2
        if pygame.sprite.spritecollide(p2, balls, False):
            # Gets list of collided balls
            collide_balls = pygame.sprite.spritecollide(p2, balls, False)
            # Calls their reflect method
            for ball in collide_balls:
                ball.reflect(p2)

        # Updates all the objects on screen
        sprites.update(score, p_list)

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
        center=(_display_width // 2, _display_height // 2)
        )
    # Updates to the screen
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Ends running state
    running = False

    # Calls restart method to play again
    restart(False)


# Restart method to play another game
def restart(first_game):
    in_game = False
    while not in_game:
        for event in pygame.event.get():
            # Tells player to press space to start if on first game
            if first_game:
                font = pygame.font.Font(None, 69)
                text = font.render(
                    "Press Space to Start!", True, (255, 255, 255)
                    )

                # Gets position of string centered around the specified spot
                text_rect = text.get_rect(
                    center=(_display_width // 2, _display_height // 2)
                    )
                # Updates to the screen
                screen.blit(text, text_rect)
                pygame.display.flip()
            # Exits pygame if true
            if event.type == pygame.QUIT:
                pygame.quit()
            # Waits for spacebar press to start
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                in_game = True
                # Starts a new game
                game()


# Waits for user input before starting game
restart(True)
