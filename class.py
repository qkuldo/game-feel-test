import pygame
class character:
	def __init__(self, pos=[0,0]):
		self.pos = pos
		self.character = pygame.Rect(self.pos[0],self.pos[1],50,100)
