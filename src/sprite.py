import pygame

class Sprite(pygame.sprite.Sprite): # Cookie is a subclass/child class of Sprite
  def __init__(self, x, y, img = "./../assets/start.png", scale = 1.0):
    super().__init__()
    self.image = pygame.image.load(img)
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.image = pygame.transform.scale(self.image, (self.width*scale, self.height*scale))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
