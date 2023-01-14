from pygame.sprite import Sprite
from pygame import Rect

import files_manager

note = files_manager.loadFile('note.png')

class Note(Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        width = 57
        height = 58
        self.image = note
        self.startX = x
        self.startY = y
        self.xvel = speed
        self.rect = Rect(x, y, width, height)

    def update(self, Click):
        if Click == False:           
            self.rect.y += self.xvel
        if Click:
            self.rect.y = 0
            
    def draw(self, screen):      
        screen.blit(self.image, (self.rect.x, self.rect.y))