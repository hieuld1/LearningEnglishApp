# -*- coding: utf-8 -*-
import sys
from time import sleep
import pygame
import random

from settings import Settings
from game_stats import GameStats
from button import Button
from combo_box import ComboBox
from create_lesson import CreateLesson
from lesson_chose import LessonChoose

NUM_LEARN_WORDS_DONE        = 1000
LEARN_MODE_LESSON_CARD      = 2
LEARN_MODE_LESSON_WORD      = 3
LEARN_MODE_CREATE_LESSON    = 4

class LearningEnglish:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock              = pygame.time.Clock()
        self.settings           = Settings()
        self.screen             = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Learning English")

        self.stats              = GameStats(self)
        self.CreateLesson       = CreateLesson(self)
        self.LessonChoose       = LessonChoose(self)

        # Configure learning mode
        learn_mode_list = ["LESSON CARD", "LESSON FILL", "CREATE LESSON"]
        self.ComboBoxLearnMode      = ComboBox(self, learn_mode_list, 250, 60, 200, 32, 'Learn Mode')
        self.Config_button          = Button(self, 240, 260, "Config")

        # Flag handle game configure done
        self.game_configure_done    = False

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            self._update_screen()

            self.clock.tick(30)    

    def _check_events(self):
        """Respond to keypresses and mouse events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit() 

            if(self.game_configure_done):
                if self.learning_mode == LEARN_MODE_LESSON_CARD:
                    # print("LEARN_MODE_LESSON_CARD")
                    self.LessonChoose.choose_lesson_handle_event(event)
                elif self.learning_mode == LEARN_MODE_LESSON_WORD:
                    # print("LEARN_MODE_LESSON_WORD")
                    self.LessonChoose.choose_lesson_handle_event(event)
                elif self.learning_mode == LEARN_MODE_CREATE_LESSON:
                    # print("LEARN_MODE_CREATE_LESSON")
                    self.CreateLesson.create_lesson_handle_event(event)

            else:      
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_config_button(mouse_pos)

                self.ComboBoxLearnMode.combo_box_handle_event(event)    

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        if self.game_configure_done:
            if self.learning_mode == LEARN_MODE_LESSON_CARD:
                # print("LEARN_MODE_LESSON_CARD")
                self.LessonChoose.choose_lesson_draw()
            elif self.learning_mode == LEARN_MODE_LESSON_WORD:
                # print("LEARN_MODE_LESSON_WORD")
                self.LessonChoose.choose_lesson_draw()
            elif self.learning_mode == LEARN_MODE_CREATE_LESSON:
                # print("LEARN_MODE_CREATE_LESSON Update")
                self.CreateLesson.create_lesson_draw()

        else:
            self.ComboBoxLearnMode.combo_box_display() 
            self.Config_button.draw_button()

        pygame.display.flip()       

    def _check_config_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.Config_button.rect.collidepoint(mouse_pos)
        
        if button_clicked:
            if self.ComboBoxLearnMode.selected_option == "LESSON CARD":
                self.learning_mode      = LEARN_MODE_LESSON_CARD
                self.LessonChoose.choose_lesson_set_learn_mode(LEARN_MODE_LESSON_CARD)
            elif self.ComboBoxLearnMode.selected_option == "LESSON FILL":
                self.learning_mode      = LEARN_MODE_LESSON_WORD
                self.LessonChoose.choose_lesson_set_learn_mode(LEARN_MODE_LESSON_WORD)
            else:
                self.learning_mode      = LEARN_MODE_CREATE_LESSON

            print("Learning mode", self.ComboBoxLearnMode.selected_option, self.learning_mode)

            # if self.learning_mode == LEARN_MODE_LESSON_CARD:
            #     print("LEARN_MODE_LESSON_CARD")
            # elif self.learning_mode == LEARN_MODE_LESSON_WORD:
            #     print("LEARN_MODE_LESSON_WORD")
            # elif self.learning_mode == LEARN_MODE_CREATE_LESSON:
            #     print("Create lesson to learn")

            # Configure done
            self.game_configure_done    = True

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = LearningEnglish()
    ai.run_game()    