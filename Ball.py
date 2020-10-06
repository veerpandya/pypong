import random
import math
import pygame


# This class is inherited from the pygame Sprite class
class Ball(pygame.sprite.Sprite):

    def __init__(self):

        # Uses the sprite constructor from pygame
        pygame.sprite.Sprite.__init__(self)

        # Size of ball
        self.image = pygame.Surface([10, 10])
        # Color of ball
        self.image.fill((255, 255, 255))

        # This gets the image dimensions and then lets us set the position
        self.rect = self.image.get_rect()
        # Initialize position of ball
        self.x_pos = 0
        self.y_pos = 0

        # Variable for angle and speed of the ball [angle, speed]
        self.velocity = [0, 0]

        # Assigns variables for the game window's width and height
        self.display_width = pygame.display.get_surface().get_width()
        self.display_height = pygame.display.get_surface().get_height()

        # Configures a new ball state
        self.new_ball()

    # Sets values for a new ball to be created
    def new_ball(self):
        # Sets x position to half the width of the game screen
        self.x_pos = self.display_width / 2
        # Sets y position to a random spot inside the height of the screen
        self.y_pos = random.randrange(200, self.display_height - 200)

        # Determines starting direction of ball randomly
        if random.random() < 0.5:
            # Set initial angle somewhere facing right
            self.velocity[0] = random.randrange(-60, 60)
            # Set initial speed
            self.velocity[1] = random.randrange(5, 8)
        else:
            # Set initial angle somewhere facing left
            self.velocity[0] = random.randrange(120, 240)
            # Set initial speed
            self.velocity[1] = random.randrange(5, 8)

    # Reflects ball off objects
    def reflect(self, player):
        # Adds a bit of randomness to it
        rand = random.randrange(-10, 10)
        # Sets ball angle to the opposite of what it is
        self.velocity[0] = (180 + rand - self.velocity[0]) % 360
        # Makes ball speed up random amount
        self.speed(random.uniform(1, 1.2))

    # Speeds up the ball by the given multiplier
    def speed(self, multiplier):
        self.velocity[1] *= multiplier

    # Updates the position of the ball based on the speed and direction
    # Overrides Sprite parent method
    def update(self, score, p_list):
        # To figure out how far the ball goes in a given direction we use
        # trigonometry, SOH CAH TOA, in this case we know the hypotenuse
        # Python uses radians so we convert our angle
        rad_angle = math.radians(self.velocity[0])

        # For the opposite side (change in y_pos) we use sin(θ) * speed
        delta_y = math.sin(rad_angle) * self.velocity[1]
        # For the adjacent side (change in x_pos) we use cos(θ) * speed
        delta_x = math.cos(rad_angle) * self.velocity[1]

        # Updates ball position
        self.y_pos += delta_y
        self.x_pos += delta_x

        # Checks if ball is out of bounds on left side
        if self.x_pos <= 0:
            # Gives point to player 2
            score.increment(p_list[1])
            # Makes new ball
            self.new_ball()
            # Resets paddle state for player 2
            p_list[1].pad_reset()
        # Checks if ball is out of bounds on right side
        if self.x_pos >= self.display_width:
            # Gives point to player 1
            score.increment(p_list[0])
            # Makes new ball
            self.new_ball()
            # Resets paddle state for player 1
            p_list[0].pad_reset()

        # Checks if ball hits top/bottom of display, and bounces it off
        if self.y_pos <= 0 or self.y_pos > self.display_height - 10:
            self.velocity[0] = (360 - self.velocity[0]) % 360

        # Updates image position of sprite
        self.rect.y = self.y_pos
        self.rect.x = self.x_pos
