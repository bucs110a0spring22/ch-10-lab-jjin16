import pygame
class Totem(pygame.sprite.Sprite):
  def __init__(self,x,y,img_file):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(img_file).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.totem_usage= 0
  def revive(self):
    """
    when revive function is called, it checks if it is the first time being called. Then totem object appears on the screen near the hero if the function returns true.
    args: none
    return: True/False
    """
    if self.totem_usage == 0:
      self.totem_usage+=1
      self.rect.x= 50
      self.rect.y= -50
      print("Totem of undying revived you!")
      print("Totem of undying shattered!")
      return True
    else:
      print("There is no more totem of undying to save you!")
      return False