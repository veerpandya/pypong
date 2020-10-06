import random
import math
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, side):

        # Uses the sprite constructor from pygame
        pygame.sprite.Sprite.__init__(self)

        # Variable for length of paddle
        self.__pad_length = 100

        # Sets variable to tell if paddle is already big
        self.__is_big = False

        # Sets size and color of paddle
        self.image = pygame.Surface([20, self.__pad_length])
        self.image.fill((250, 250, 250))

        # This gets the image dimensions and then lets us set the position
        self.rect = self.image.get_rect()

        # Assigns variables for the game window's width and height
        self.display_width = pygame.display.get_surface().get_width()
        self.display_height = pygame.display.get_surface().get_height()

        # Initialize y position of paddle
        self.y_pos = (self.display_height / 2) - 50

        # Sets up Left or Right player
        if side == "Left":
            self.up_key = pygame.K_w
            self.down_key = pygame.K_s
            self.x_pos = 10
        if side == "Right":
            self.up_key = pygame.K_UP
            self.down_key = pygame.K_DOWN
            self.x_pos = self.display_width - 30

        # Updates image position of sprite
        self.rect.y = self.y_pos
        self.rect.x = self.x_pos

    # Return big if true
    def is_big(self):
        return self.__is_big

    # Modifies paddle size to be bigger
    def big_paddle(self):
        # Checks if paddle is already big
        if not self.__is_big:
            # Make paddle bigger by a random amount
            self.__pad_length = random.randrange(125, 200)
            self.image = pygame.Surface([20, self.__pad_length])
            self.image.fill((250, 250, 250))
            # Gets new dimensions
            self.rect = self.image.get_rect()
            # Updates __is_big
            self.__is_big = True

    # Resets the paddle back
    def pad_reset(self):
        # Checks if the paddle is big and then resets it
        if self.__is_big:
            self.__pad_length = 100
            self.image = pygame.Surface([20, self.__pad_length])
            self.image.fill((250, 250, 250))
            # Gets new dimensions
            self.rect = self.image.get_rect()
            # Updates __is_big
            self.__is_big = False

    # Overrides update method from sprite
    # Checks for keyboard input and updates the location of paddle
    def update(self, score, p_list):

        # Gets bool list of all keys
        keys = pygame.key.get_pressed()

        # Checks if up or down is pressed and sets modifier
        delta_y = 0
        if keys[self.up_key]:
            delta_y -= 10
        if keys[self.down_key]:
            delta_y += 10

        # Updates y position with the new delta
        self.y_pos = int(self.y_pos + delta_y)

        # Keeps the paddle on the screen
        if self.y_pos <= 0:
            self.y_pos = 0
        if self.y_pos >= self.display_height - self.__pad_length:
            self.y_pos = self.display_height - self.__pad_length

        # Updates the image position of the sprite
        self.rect.y = self.y_pos
        self.rect.x = self.x_pos
