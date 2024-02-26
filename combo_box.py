import pygame
import sys

class ComboBox:
    def __init__(self, ai_game, options, x, y, width, height, header):
        self.screen = ai_game.screen
        self.options = options
        self.selected_option = None
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, 30)
        self.is_open = False
        self.header = header
        
    def combo_box_draw(self):
        pygame.draw.rect(self.screen, (200, 200, 200), self.rect)
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.rect.x + self.rect.width - 20, self.rect.centery - 5),
                                                (self.rect.x + self.rect.width - 10, self.rect.centery - 5),
                                                (self.rect.x + self.rect.width - 15, self.rect.centery + 5)])

        selected_text = self.font.render(self.selected_option if self.selected_option else "Select Option", True, (0, 0, 0))
        self.screen.blit(selected_text, (self.rect.x + 10, self.rect.y + self.rect.height // 2 - selected_text.get_height() // 2))

        if self.is_open:
            for i, option in enumerate(self.options):
                option_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.height * (i + 1), self.rect.width, self.rect.height)
                pygame.draw.rect(self.screen, (200, 200, 200), option_rect)
                text = self.font.render(option, True, (0, 0, 0))
                self.screen.blit(text, (option_rect.x + 10, option_rect.y + option_rect.height // 2 - text.get_height() // 2))

    def combo_box_handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.is_open = not self.is_open
                elif self.is_open:
                    for i, option in enumerate(self.options):
                        option_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.height * (i + 1),
                                                 self.rect.width, self.rect.height)
                        if option_rect.collidepoint(event.pos):
                            self.selected_option = option
                            self.is_open = False


    def combo_box_header_word(self):  
        # Color of configuration word
        black = (0, 0, 0)

        # Render and draw result text
        result_text_render = self.font.render(self.header, True, black)
        self.screen.blit(result_text_render, (self.rect.x - 200, self.rect.y ))    

    def combo_box_display(self):

        # Update and draw ComboBox
        self.combo_box_draw()
        self.combo_box_header_word()