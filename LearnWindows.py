# -*- coding: utf-8 -*-
import pygame.font
from pygame.sprite import Group

class LearnWin:
    """A class to display english words."""

    def __init__(self, ai_game):
        """Initialize english words attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        # self.font = pygame.font.SysFont(None, 48)
        self.font = pygame.font.SysFont('arial', 36) # Display Vietnamese in pygame ok

        # Prepare the initial score image.
        self.prep_word("Nothing")

    def prep_word(self, word_learn):
        """Turn the word into a rendered image."""
        self.word_image = self.font.render(word_learn, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.word_rect = self.word_image.get_rect()
        
        self.word_rect.center = self.screen_rect.center       

    def show_word(self, word):
        """Draw scores, ships and level to the screen."""
        # self.prep_word(word)
        # self.screen.blit(self.word_image, self.word_rect) 
        # Define the rect area for text
        text_rect = pygame.Rect(300, 160, 380, 220)   
        
        self.word_rect.center = self.screen_rect.center

        self.draw_text(word, text_rect)

    # Custom text wrapping function
    def draw_text(self, text, rect):
        words = text.split()
        space_width, _ = self.font.size(' ')
        x, y = rect.topleft
        line_spacing = self.font.get_linesize()

        for word in words:
            word_width, word_height = self.font.size(word)

            if x + word_width > rect.right:
                x = rect.left
                y += line_spacing

            # self.word_image = self.font.render(word_learn, True, self.text_color, self.settings.bg_color)
            self.screen.blit(self.font.render(word, True, self.text_color, self.settings.bg_color), (x, y))
            x += word_width + space_width    