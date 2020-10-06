import random
import math
import pygame
from Ball import Ball


# This class inherits from the Ball class
# It will give the player an advantage if obtained
class Powerup(Ball):
    def __init__(self):
        # Calls the ball init
        Ball.__init__(self)
        # Set color to be bluish
        self.image.fill((136, 136, 255))

    # Overrides reflect to instead give the player a powerup
    def reflect(self, player):
        # Calls big paddle method
        player.big_paddle()
        # Kills the powerup sprite
        self.kill()

    # Method to kill sprite
    def kill(self):
        pygame.sprite.Sprite.kill(self)

    # Overrides update method to kill powerup when out of bounds
    def update(self, score, p_list):
        # Mostly the same code from Ball
        rad_angle = math.radians(self._velocity[0])
        delta_y = math.sin(rad_angle) * self._velocity[1]
        delta_x = math.cos(rad_angle) * self._velocity[1]

        self.y_pos += delta_y
        self.x_pos += delta_x

        # Checks if ball is out of bounds
        if self.x_pos <= 0 or self.x_pos >= self.display_width:
            # If so, kill it
            self.kill()

        # Checks if ball hits top/bottom of display, and bounces it off
        if self.y_pos <= 0 or self.y_pos > self.display_height - 10:
            self._velocity[0] = (360 - self._velocity[0]) % 360

        # Makes sure the sprite is alive before updating the position
        if pygame.sprite.Sprite.alive(self):
            # Updates image position of sprite
            self.rect.y = self.y_pos
            self.rect.x = self.x_pos
