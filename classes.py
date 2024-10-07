import pygame
class character:
	def __init__(self, pos=[0,0],draw_color=(0,0,0)):
		self.pos = pos
		self.draw_color = draw_color
		self.character = pygame.Rect(self.pos[0],self.pos[1],50,100)
	def draw(self,screen):
        pygame.draw.rect(screen,self.draw_color,self.character)