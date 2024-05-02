import pygame

class Sprite(pygame.sprite.Sprite): # Cookie is a subclass/child class of Sprite
  def __init__(self, x, y, img = "assets/start.png", scale = 1.0):
    """This 

    Args:
        x (int): This stores the x coordinate of top left corner of the sprite rectangle.
        y (int): This stores the y coordinate of top left corner of the sprite rectangle.
        img (str, optional): This stores a sprite image from the assets folder. Defaults to "assets/start.png".
        scale (float, optional): This stores a scale for the size of the game sprite. Defaults to 1.0.
    """
    super().__init__()
    self.image = pygame.image.load(img)
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.image = pygame.transform.smoothscale(self.image, (self.width*scale, self.height*scale))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
