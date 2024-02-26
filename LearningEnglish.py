# -*- coding: utf-8 -*-
import sys
from time import sleep
import pygame
import random

from settings import Settings
from game_stats import GameStats
# from ReadExcel import ReadExcelFile
# from LearnWindows import LearnWin
from button import Button
# from inputBox import InputBox
# from configure_box import ConfigBox
from combo_box import ComboBox
from create_lesson import CreateLesson
from lesson_chose import LessonChoose

NUM_LEARN_WORDS_DONE        = 1000
# LEARN_MODE_FLASH_CARD       = 0
# LEARN_MODE_FILL_WORD        = 1
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
        # self.ReadExcelFile      = ReadExcelFile()
        # self.LearnWin           = LearnWin(self)
        # self.InputBox           = InputBox(self, 140, 60, 140, 32)
        self.CreateLesson       = CreateLesson(self)
        self.LessonChoose       = LessonChoose(self)

        # Configure learning mode
        # self.ConfigBoxLearnMode     = ConfigBox(self, 250, 60, 140, 32, 'Learn Mode')
        learn_mode_list = ["LESSON CARD", "LESSON FILL", "CREATE LESSON"]
        # learn_letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.ComboBoxLearnMode      = ComboBox(self, learn_mode_list, 250, 60, 200, 32, 'Learn Mode')
        # self.ConfigBoxNumWord       = ConfigBox(self, 250, 140, 140, 32, 'Number Word')
        # self.ConfigBoxLetter        = ConfigBox(self, 250, 220, 140, 32, 'Letter')
        self.Config_button          = Button(self, 240, 260, "Config")

        # Flag handle game configure done
        self.game_configure_done    = False

        # Learing mode flash card 0 or word fill 
        # self.learning_mode          = LEARN_MODE_FILL_WORD
        # self.learning_letter        = 'A'
        # self.learning_number_word   = 20

        # Create a learning list
        # self.list_key_letter    = []
        # self.list_val_letter    = []
        # self.learn_word_key     = []
        # self.learn_word_value   = []
        # self.learn_word_stat    = []
        # self.display_word       = ''
        # self.display_word_idx   = 0
        # self.display_word_key   = 1

        # Make the Play button.
        # self.yes_button         = Button(self, 400, 260, "Yes")
        # self.no_button          = Button(self, 0, 260, "No")
        # self.flip_button        = Button(self, 200, 0, "Flip")

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            self._update_screen()

            self.clock.tick(30)   

    # def __filter_list_letter(self, input_key_list, input_val_list, input_letter):
        
    #     length = len(input_key_list)
    #     for idx in range(0, length - 1):
    #         string = str(input_key_list[idx])
    #         if string.lower().startswith(input_letter.lower()):
    #             # print(string)
    #             self.list_key_letter = self.list_key_letter + [input_key_list[idx]]
    #             self.list_val_letter = self.list_val_letter + [input_val_list[idx]]


    # def _create_learning_list(self):  
    #     """Create a learning list."""    

    #     # find the list start with letter
    #     self.__filter_list_letter(self.ReadExcelFile.list_key, 
    #                                 self.ReadExcelFile.list_value, 
    #                                 self.learning_letter)

    #     # print(self.list_key_letter)
    #     # print(len(self.list_key_letter))

    #     num_word_gen = self.learning_number_word
    #     length = len(self.list_key_letter)

    #     if self.learning_number_word > length:
    #         num_word_gen = length
    #         self.learning_number_word = length

    #     for i in range(0, num_word_gen):
    #         idx                     = random.randint(0, length - 1)
    #         self.learn_word_key     = self.learn_word_key + [self.list_key_letter[idx]]
    #         self.learn_word_value   = self.learn_word_value + [self.list_val_letter[idx]]
    #         self.learn_word_stat    = self.learn_word_stat + [0]
    #         # print(idx, self.learn_word_key[i], self.learn_word_value[i])

    #     self.display_word_idx       = 0
    #     if(self.learning_mode == LEARN_MODE_FLASH_CARD):
    #         self.display_word_key   = 1 
    #         self.display_word       = self.learn_word_key[0]
    #     else:
    #         self.display_word_key   = 0 
    #         self.display_word       = self.learn_word_value[0]

    #     print(self.display_word)        

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
                # else:
                #     if event.type == pygame.KEYDOWN:
                #         self._check_keydown_events(event)
                #     elif event.type == pygame.KEYUP:
                #         self._check_keyup_events(event)   
                #     elif event.type == pygame.MOUSEBUTTONDOWN:
                #         mouse_pos = pygame.mouse.get_pos()
                #         self._check_yes_button(mouse_pos)  
                #         self._check_no_button(mouse_pos) 
                #         self._check_flip_button(mouse_pos) 

                #     if(self.learning_mode == LEARN_MODE_FILL_WORD):
                #         self.InputBox.handle_event(event) 

            else:      
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_config_button(mouse_pos)

                # self.ConfigBoxLearnMode.handle_event(event)
                self.ComboBoxLearnMode.combo_box_handle_event(event)
                # self.ConfigBoxNumWord.handle_event(event)
                # self.ConfigBoxLetter.handle_event(event)         

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
            # else:
            #     self.LearnWin.show_word(str(self.display_word))
                
            #     # Draw the play button in the game.
            #     self.yes_button.draw_button()
            #     self.no_button.draw_button()
            #     self.flip_button.draw_button()

            #     if(self.learning_mode == LEARN_MODE_FILL_WORD):
            #         correct_word = self.learn_word_key[self.display_word_idx]
            #         self.InputBox.input_box_display(correct_word)

        else:
            # self.ConfigBoxLearnMode.config_box_display()
            self.ComboBoxLearnMode.combo_box_display()
            # self.ConfigBoxNumWord.config_box_display()
            # self.ConfigBoxLetter.config_box_display()    
            self.Config_button.draw_button()

        pygame.display.flip()       

    # def _check_flip_button(self, mouse_pos):
    #     """Start a new game when the player clicks Play."""
    #     button_clicked = self.flip_button.rect.collidepoint(mouse_pos)
        
    #     if button_clicked:
    #         if self.display_word_key:
    #             self.display_word_key   = 0  
    #             self.display_word       = self.learn_word_value[self.display_word_idx]
    #         else:
    #             self.display_word_key   = 1  
    #             self.display_word       = self.learn_word_key[self.display_word_idx]
            
    #         # print(self.display_word) 

    # def __find_next_word(self):
    #     num_loop = 0
    #     index_out = self.display_word_idx 
    #     while True:
    #         index_out   = index_out + 1
            
    #         if(index_out >= self.learning_number_word):
    #             index_out = 0
                
    #         # print(index_out, self.learning_number_word)
    #         if self.learn_word_stat[index_out] == 0:
    #             return index_out

    #         num_loop = num_loop + 1

    #         if(num_loop >= self.learning_number_word):
    #             print("All words have been learned!")
    #             self.display_word       = 'finish work!'
    #             return NUM_LEARN_WORDS_DONE
                
    # def _check_yes_button(self, mouse_pos):
    #     """Start a new game when the player clicks Play."""
    #     button_clicked = self.yes_button.rect.collidepoint(mouse_pos)
        
    #     if button_clicked:
    #         if self.display_word_idx < NUM_LEARN_WORDS_DONE:
    #             self.learn_word_stat[self.display_word_idx] = 1

    #         self.display_word_idx   = self.__find_next_word()

    #         if self.display_word_idx < NUM_LEARN_WORDS_DONE:
    #             if(self.learning_mode == LEARN_MODE_FLASH_CARD):
    #                 self.display_word_key   = 1 
    #                 self.display_word       = self.learn_word_key[self.display_word_idx]
    #             else:
    #                 self.display_word_key   = 0 
    #                 self.display_word       = self.learn_word_value[self.display_word_idx]
                
    #         # print(self.display_word)  


    # def _check_no_button(self, mouse_pos):
    #     """Start a new game when the player clicks Play."""
    #     button_clicked = self.no_button.rect.collidepoint(mouse_pos)
        
    #     if button_clicked:
    #         self.display_word_idx   = self.__find_next_word()

    #         if self.display_word_idx < NUM_LEARN_WORDS_DONE:
    #             if(self.learning_mode == LEARN_MODE_FLASH_CARD):
    #                 self.display_word_key   = 1 
    #                 self.display_word       = self.learn_word_key[self.display_word_idx]
    #             else:
    #                 self.display_word_key   = 0 
    #                 self.display_word       = self.learn_word_value[self.display_word_idx]
                
    #         # print(self.display_word)   

    def _check_config_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.Config_button.rect.collidepoint(mouse_pos)
        
        if button_clicked:
            # ["FLASH CARD", "FILL WORD", "LESSON CARD", "LESSON FILL", "CREATE LESSON"]
            # if self.ComboBoxLearnMode.selected_option == "FLASH CARD":
            #     self.learning_mode      = LEARN_MODE_FLASH_CARD
            # elif self.ComboBoxLearnMode.selected_option == "FILL WORD":
            #     self.learning_mode      = LEARN_MODE_FILL_WORD
            # el
            if self.ComboBoxLearnMode.selected_option == "LESSON CARD":
                self.learning_mode      = LEARN_MODE_LESSON_CARD
                self.LessonChoose.choose_lesson_set_learn_mode(LEARN_MODE_LESSON_CARD)
            elif self.ComboBoxLearnMode.selected_option == "LESSON FILL":
                self.learning_mode      = LEARN_MODE_LESSON_WORD
                self.LessonChoose.choose_lesson_set_learn_mode(LEARN_MODE_LESSON_WORD)
            else:
                self.learning_mode      = LEARN_MODE_CREATE_LESSON

            print("Learning mode", self.ComboBoxLearnMode.selected_option, self.learning_mode)

            if self.learning_mode == LEARN_MODE_LESSON_CARD:
                print("LEARN_MODE_LESSON_CARD")
            elif self.learning_mode == LEARN_MODE_LESSON_WORD:
                print("LEARN_MODE_LESSON_WORD")
            elif self.learning_mode == LEARN_MODE_CREATE_LESSON:
                print("Create lesson to learn")
            # else:
            #     self.learning_letter        = str(self.ConfigBoxLetter.text).lower()
            #     self.learning_number_word   = int(self.ConfigBoxNumWord.text)
            #     # Create a learning list
            #     self._create_learning_list()
            
            #     print(self.learning_mode, self.learning_letter, self.learning_number_word)

            # Configure done
            self.game_configure_done    = True
    
    # def _check_keydown_events(self, event):
    #     """Respond to keypresses."""
    #     if event.key == pygame.K_RIGHT:
    #         print("K_RIGHT")
    #         if self.display_word_idx < NUM_LEARN_WORDS_DONE:
    #             self.learn_word_stat[self.display_word_idx] = 1

    #         self.display_word_idx   = self.__find_next_word()

    #         if self.display_word_idx < NUM_LEARN_WORDS_DONE:
    #             self.display_word_key   = 1 
    #             self.display_word       = self.learn_word_key[self.display_word_idx]
            
    #     elif event.key == pygame.K_LEFT:
    #         print("K_LEFT")
    #         self.display_word_idx   = self.__find_next_word()

    #         if self.display_word_idx < NUM_LEARN_WORDS_DONE:
    #             self.display_word_key   = 1 
    #             self.display_word       = self.learn_word_key[self.display_word_idx]
            
    #     elif event.key == pygame.K_UP:  
    #         if self.display_word_key:
    #             self.display_word_key   = 0  
    #             self.display_word       = self.learn_word_value[self.display_word_idx]
    #         else:
    #             self.display_word_key   = 1  
    #             self.display_word       = self.learn_word_key[self.display_word_idx]

    #     elif event.key == pygame.K_q:
    #         sys.exit()   

    # def _check_keyup_events(self, event):
    #     """Respond to key releases."""
    #     if event.key == pygame.K_RIGHT:
    #         print("K_RIGHT1")
    #     elif event.key == pygame.K_LEFT:
    #         print("K_LEFT1")   
    #     elif event.key == pygame.K_UP:
    #         print("K_UP1")

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = LearningEnglish()
    ai.run_game()    