import pygame


# Class to contain and manage player score
class Score(pygame.sprite.Sprite):

    def __init__(self, p1, p2):
        # Uses the sprite constructor from pygame
        pygame.sprite.Sprite.__init__(self)

        # Assigns the players
        # Composition with the player class
        self.p1 = p1
        self.p2 = p2

        # Initializes the scores
        # Private because we don't want it to be changed anywhere outside
        self.__p1_score = 0
        self.__p2_score = 0

        # Sets font
        self.font = pygame.font.Font(None, 69)

        # Sets image size
        self.image = pygame.Surface([100, 100])
        self.rect = self.image.get_rect()

        # Gets display dimensions
        self.display_width = pygame.display.get_surface().get_width()
        self.display_height = pygame.display.get_surface().get_height()

    # Adds a point to the correct player
    def increment(self, player):
        if player == self.p1:
            self.__p1_score += 1
        if player == self.p2:
            self.__p2_score += 1

    # Returns current score
    def scores(self, player):
        if player == self.p1:
            return self.__p1_score
        if player == self.p2:
            return self.__p2_score

    # Checks for winner (first to 5 points)
    # Returns True if condition is met
    def has_won(self):
        if self.__p1_score == 5:
            return True
        elif self.__p2_score == 5:
            return True
        else:
            return False

    # Returns who won
    def who_won(self):
        if self.__p1_score == 5:
            return "Player 1"
        elif self.__p2_score == 5:
            return "Player 2"
        else:
            return "No one"

    # Updates score on screen
    def update(self, score, p_list):
        # Gets scores
        p1 = self.scores(p_list[0])
        p2 = self.scores(p_list[1])

        # Makes and renders string to be displayed
        text = self.font.render(
            f"{p1}          vs          {p2}", True, (255, 255, 255)
            )
        # Gets position of text string centered around the specified spot
        text_rect = text.get_rect(
            center=(self.display_width // 2, self.display_height - 50)
            )

        # Sets the score to the screen
        pygame.display.get_surface().blit(text, text_rect)
