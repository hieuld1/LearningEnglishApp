import pygame
import sys

class ConfigBox:

    def __init__(self, ai_game, x, y, width, height, config_mode):
        self.screen = ai_game.screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.font = pygame.font.SysFont(None, 36)
        self.active = False
        self.config_mode = config_mode

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        return False            

    def config_box_update(self):
        width = max(200, self.font.size(self.text)[0] + 10)
        self.rect.w = width

    def config_box_draw(self):
        txt_surface = self.font.render(self.text, True, self.color)
        width = max(200, txt_surface.get_width()+10)
        self.rect.w = width
        self.screen.blit(txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(self.screen, self.color, self.rect, 2)

    def config_box_header_word(self):  
        # Color of configuration word
        black = (0, 0, 0)

        # Render and draw result text
        result_text_render = self.font.render(self.config_mode, True, black)
        self.screen.blit(result_text_render, (self.rect.x - 200, self.rect.y))    

    def config_box_display(self):

        # Update and draw InputBox
        self.config_box_update()
        self.config_box_draw()
        self.config_box_header_word()
