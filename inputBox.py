import pygame
import sys

class InputBox:
    def __init__(self, ai_game, x, y, width, height):
        self.screen = ai_game.screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.font = pygame.font.SysFont(None, 36)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
            # print("mouse")

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
            # print("key: ", self.text)
        return False

    def input_box_update(self):
        width = max(200, self.font.size(self.text)[0] + 10)
        self.rect.w = width

    def input_box_draw(self):
        txt_surface = self.font.render(self.text, True, self.color)
        width = max(200, txt_surface.get_width()+10)
        self.rect.w = width
        self.screen.blit(txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(self.screen, self.color, self.rect, 2)
        # print("draw")

    def input_box_check_word(self, correct_word):  
        # Color of check word
        black = (0, 0, 0)
        
        # Compare input with correct string
        if self.text == correct_word:
            result_text = "Correct!"
        else:
            result_text = "Wrong!"

        # Render and draw result text
        result_text_render = self.font.render(result_text, True, black)
        self.screen.blit(result_text_render, (360, 60))    

    def input_box_display(self, correct_word):
        
        # white = (255, 255, 255)
        # Clear the screen
        # self.screen.fill(white)

        # Update and draw InputBox
        self.input_box_update()
        self.input_box_draw()
        self.input_box_check_word(correct_word)
