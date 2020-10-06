import pygame


# Class to contain and manage player score
class Score(pygame.sprite.Sprite):

    def __init__(self, p1_score, p2_score):
        # Uses the sprite constructor from pygame
        pygame.sprite.Sprite.__init__(self)

        self.p1_score = p1_score
        self.p2_score = p2_score

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
        if player == 1:
            self.p1_score += 1
        if player == 2:
            self.p2_score += 1

    # Returns current score
    def scores(self, player):
        if player == 1:
            return self.p1_score
        if player == 2:
            return self.p2_score

    # Checks for winner (first to 5 points)
    # Returns True if condition is met
    def has_won(self):
        if self.p1_score == 5:
            return True
        elif self.p2_score == 5:
            return True
        else:
            return False

    # Returns who won
    def who_won(self):
        if self.p1_score == 5:
            return "Player 1"
        elif self.p2_score == 5:
            return "Player 2"
        else:
            return "No one"

    # Updates score on screen
    def update(self, score, p_list):
        # Gets scores
        p1 = self.scores(1)
        p2 = self.scores(2)

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
