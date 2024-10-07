import pygame
class character:
	def __init__(self, pos=[0,0],draw_color=(0,0,0)):
		self.pos = pos
		self.draw_color = draw_color
		self.character = pygame.Rect(self.pos[0],self.pos[1],50,100)
	def update(self):
		self.character.x = self.pos[0]
		self.character.y = self.pos[1]
	def draw(self,screen):
		pygame.draw.rect(screen,self.draw_color,self.character)
class particle:
	def __init__(self,pos,dx,dy,life=300):
		self.pos = pos
		self.dx = dx
		self.dy = dy
		self.life = life
	def update(self,clock):
		self.pos[0] += self.dx
		self.pos[1] += self.dy
		self.life -= clock.get_time()
		if (self.life <= 0):
			return 1
	def draw(self,screen):
		rect = pygame.Rect(self.pos[0],self.pos[1],30,30)
		pygame.draw.rect(screen,(255,255,255),rect)