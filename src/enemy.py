import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
      """
      Makes the enemy object move randomly by randomly altering the x & y coordinates of the enemy object in the step of 1.
      args: none
      return: none
      """
      random_x= random.randrange(-1,1)
      random_y= random.randrange(-1,1)
      self.rect.x+=random_x
      self.rect.y+=random_y
      #print("'Update me,' says " + self.name)
