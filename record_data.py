# -*- coding: utf-8 -*-
import pygame.font
import sqlite3

from datetime import datetime

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

class RecordData:
    """A class to display record data."""

    def __init__(self, ai_game):
        """Initialize record."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('arial', 16) # Display Vietnamese in pygame ok

        self.connection     = sqlite3.connect('learn_records.db')
        self.start_time     = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.stop_time      = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.learn_lesson   = ''

        # Create the table if it doesn't exist
        self.record_data_create_table()

    def record_data_set_start_time(self, start_time):
        self.start_time = start_time

    def record_data_set_stop_time(self, stop_time):
        self.stop_time = stop_time

    def record_data_set_learn_lesson(self, learn_lesson):
        self.learn_lesson = learn_lesson    

    def record_data_create_table(self):

        cursor = self.connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS program_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_time TEXT,
                exit_time TEXT,
                learn_lesson TEXT
            )
        ''')
        self.connection.commit()

    def record_data_save_execution(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO program_records (start_time, exit_time, learn_lesson) VALUES (?, ?, ?)
        ''', (self.start_time, self.stop_time, self.learn_lesson))
        self.connection.commit()
        # print(f"Start Time: {self.start_time}, Exit Time: {self.stop_time}, Lesson: {self.learn_lesson}")

    def record_data_read_records(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM program_records')
        records = cursor.fetchall()

        for record in records:
            print(f"Start Time: {record[1]}, Exit Time: {record[2]}, Lesson: {record[3]}")

    def record_data_read_last_20_records(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM program_records ORDER BY id DESC LIMIT 20')
        records = cursor.fetchall()

        # print("Record data:")

        for i, record in enumerate(records):
            # print(f"Start Time: {record[1]}, Exit Time: {record[2]}, Lesson: {record[3]}")
            text = f"Start Time: {record[1]}, Exit Time: {record[2]}, Lesson: {record[3]}"
            text_render = self.font.render(text, True, self.text_color)
            self.screen.blit(text_render, (20, i * 20 + 120))

    def record_data_save(self):
        # update time stop learning and save in database 
        self.stop_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.record_data_save_execution()


