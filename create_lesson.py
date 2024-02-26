import pygame
import sys
import openpyxl
import os

from configure_box import ConfigBox
from button import Button
from googletrans import Translator

class CreateLesson:
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.Font(None, 36)

        self.ConfigBoxLesson    = ConfigBox(self, 250, 60, 140, 32, 'Lesson')
        self.ConfigBoxWord      = ConfigBox(self, 250, 160, 140, 32, 'Word')
        self.ButtonCreate       = Button(self, 250, 100, "Create")
        self.ButtonInsert       = Button(self, 250, 200, "Insert")
        self.ButtonFinish       = Button(self, 250, 260, "Finish")

        self.excel_file_name    = 'test.xlsx'


    def create_lesson_draw(self):
        # print("draw lesson windows")
        self.ButtonFinish.draw_button()
        self.ButtonInsert.draw_button()
        self.ButtonCreate.draw_button()

        self.ConfigBoxLesson.config_box_display()
        self.ConfigBoxWord.config_box_display()

    def create_lesson_handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self._check_finish_button(mouse_pos)
            self._check_insert_button(mouse_pos)
            self._check_create_button(mouse_pos)

        self.ConfigBoxLesson.handle_event(event)
        self.ConfigBoxWord.handle_event(event)

    def _check_finish_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.ButtonFinish.rect.collidepoint(mouse_pos)
        
        if button_clicked:
            print("Button Finish")

            # Flag handle game configure done
            self.game_configure_done    = False

    def _check_insert_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.ButtonInsert.rect.collidepoint(mouse_pos)
        
        if button_clicked:
            print("Button insert") 
            word1 = str(self.ConfigBoxWord.text)
            word2 = self.__translate_to_vietnamese(word1)   #'nothing'   #self.__translate_to_vietnamese(word1)
            self._insert_excel_file(word1, word2)  

            self.ConfigBoxWord.text = ''  

    def _check_create_button(self, mouse_pos):
        """Start a new file xlsx to create lesson"""
        button_clicked = self.ButtonCreate.rect.collidepoint(mouse_pos)
        
        if button_clicked:
            print("Button create")
            file_name = str(self.ConfigBoxLesson.text)
            self.open_or_create_excel_file(file_name)
            # self._create_excel_file(file_name + '.xlsx')

    def _create_excel_file(self, file_name):
        # Create a new workbook
        self.workbook = openpyxl.Workbook()

        # Save file name
        self.workbook.save(file_name)

        self.excel_file_name = file_name

    def _insert_excel_file(self, data1, data2):
        # Load excel file
        self.workbook = openpyxl.load_workbook(self.excel_file_name)

        # Select te active sheet
        sheet = self.workbook.active

        print("max row:", sheet.max_row)
        rows_idx = sheet.max_row + 1

        # Insert data
        sheet.cell(row = rows_idx, column = 1, value = data1) 
        sheet.cell(row = rows_idx, column = 2, value = data2) 

        # Save change
        self.workbook.save(self.excel_file_name)

    def __translate_to_vietnamese(self, word):
        translator = Translator()
        translation = translator.translate(word, src='en', dest='vi')
        return translation.text
    
    def open_or_create_excel_file(self, file_name):

        folder_path = "./"
        file_path = os.path.join(folder_path, f"{file_name}.xlsx")

        if os.path.exists(file_path):
            # If the file exists, open it
            workbook = openpyxl.load_workbook(file_path)
            print(f"Opening existing file: {file_name}.xlsx")
        else:
            # If the file doesn't exist, create a new one
            workbook = openpyxl.Workbook()
            workbook.save(file_path)
            print(f"Creating a new file: {file_name}.xlsx")

        self.excel_file_name = file_name + '.xlsx'

        return workbook