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
    if self.totem_usage == 0:
      self.totem_usage+=1
      print("Totem of undying revived you!")
      print("Totem of undying shattered!")
      return True
    else:
      print("There is no more totem of undying to save you!")
      return False